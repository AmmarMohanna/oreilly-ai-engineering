"""Regression checks run against real notebook source, with explicit service doubles.

These are component tests, not claims of live LLM/GPU execution.
REPO_DIR selects the original or repaired checkout.
"""
import ast
import contextlib
import io
import json
import os
from pathlib import Path
from types import SimpleNamespace as NS

import numpy as np
import pandas as pd
import pytest

ROOT = Path(os.environ.get("REPO_DIR", Path(__file__).resolve().parents[1]))

def notebook(number):
    return json.loads(next(ROOT.glob(f"Day */{number}.*.ipynb")).read_text())

def source(number, marker):
    return next("".join(c["source"]) for c in notebook(number)["cells"]
                if c["cell_type"] == "code" and marker in "".join(c["source"]))

def functions(number, marker, namespace):
    tree = ast.parse(source(number, marker))
    definitions = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    exec(compile(ast.Module(body=definitions, type_ignores=[]), "notebook", "exec"), namespace)
    return namespace

def completion_client(text='{"categories": ["Technology"]}'):
    calls = []
    def create(**kwargs):
        calls.append(kwargs)
        return NS(choices=[NS(message=NS(content=text))])
    return NS(chat=NS(completions=NS(create=create))), calls

@pytest.mark.parametrize("number", range(1, 11))
def test_notebook_schema_and_syntax(number):
    import nbformat
    from IPython.core.inputtransformer2 import TransformerManager
    n = nbformat.reads(json.dumps(notebook(number)), as_version=4)
    nbformat.validate(n)
    for c in n.cells:
        if c.cell_type == "code":
            compile(TransformerManager().transform_cell(c.source), "notebook", "exec")

def test_top_p_cell_uses_its_declared_temperature():
    client, calls = completion_client('example')
    ns = dict(client=client, model_name="test-model", temp=0.9)
    exec(source(2, "top_ps ="), ns)
    assert [x['temperature'] for x in calls] == [0.5, 0.5, 0.5]

@pytest.mark.parametrize('raw', ['not json', '{}', '{"relevance":"five"}',
                               '{"relevance":6,"justification":"bad"}',
                               '{"relevance":true,"justification":"bad"}', None])
def test_judge_parser_rejects_invalid_scores(raw):
    import re
    ns = functions(3, 'def parse_judge_result', dict(re=re,json=json))
    assert ns['parse_judge_result'](raw)['relevance'] is None

def test_judge_parser_accepts_a_valid_fenced_result():
    import re
    ns = functions(3, 'def parse_judge_result', dict(re=re,json=json))
    assert ns['parse_judge_result']('```json\n{"relevance":4,"justification":"Mostly accurate"}\n```')['relevance'] == 4

def test_judge_comparison_handles_missing_and_constant_scores():
    ns = dict(human_annotations=[{'relevance':5},{'relevance':4},{'relevance':5}],
              parsed_results=[{'relevance':5},{'relevance':None},{'relevance':5}],
              generated_summaries=['a','b','c'],reference_summaries=['a','b','c'])
    exec(source(3, '# Human-annotated relevance scores'), ns)
    assert list(ns['df_relevance']['Summary_ID']) == [1,3]
    assert np.isnan(ns['pearson_corr'])

def test_comparison_plot_keeps_ids_and_hides_zero_pie_slices(monkeypatch):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    monkeypatch.setattr(plt, 'show', lambda: None)
    ns = dict(human_annotations=[{'relevance':5},{'relevance':4},{'relevance':5}],
              parsed_results=[{'relevance':5},{'relevance':None},{'relevance':5}],
              generated_summaries=['a','b','c'],reference_summaries=['a','b','c'])
    exec(source(3, '# Human-annotated relevance scores'), ns)
    exec(source(3, '# Create comprehensive visualizations'), ns)
    assert [t.get_text() for t in ns['axes'][0,1].get_xticklabels()] == ['S1','S3']
    assert len(ns['wedges']) == 1
    assert 'undefined' in ns['axes'][0,0].get_title()
    plt.close(ns['fig'])

def test_guardrail_detects_the_notebooks_own_attack():
    ns = {}
    exec(source(5, 'INJECTION_PATTERNS ='), ns)
    functions(5, 'def is_suspicious', ns)
    exec(source(5, '# ===== System Prompt with Refusal'), ns)
    assert ns['is_suspicious'](ns['user_prompt_injection'])

@pytest.mark.parametrize('raw', ['{}', '{"categories": ["Invented"]}', '{"categories": "Sports"}'])
def test_category_schema_rejects_invalid_results(raw):
    ns = {}
    exec(source(5, 'INJECTION_PATTERNS ='), ns)
    functions(5, 'def is_suspicious', ns)
    assert ns['validate_categories_output'](raw)[0] is False

def test_safe_classifier_applies_output_validation():
    ns = {'model_name': 'test-model'}
    exec(source(5, 'INJECTION_PATTERNS ='), ns)
    functions(5, 'def is_suspicious', ns)
    functions(5, 'def safe_classify', ns)
    client, calls = completion_client('{"categories": ["Invented"]}')
    result = ns['safe_classify'](client, 'Classify only', 'An article about computers.')
    assert isinstance(result, dict) and 'error' in result
    assert len(calls) == 1

def test_rubric_boundaries():
    ns = {}
    functions(4, 'def rubric_score', ns)
    assert [ns['rubric_score'](x) for x in [0.59,0.6,0.7,0.8,0.9,1]] == [1,2,3,4,5,5]

def test_retriever_passes_the_query_and_k():
    calls = []
    store = NS(similarity_search_by_vector=lambda vec,k: calls.append((vec,k)) or ['doc'])
    ns = functions(6, 'def retrieve', {})
    assert ns['retrieve']('question', k=2, vector_store=store,
                          embedding_model=NS(embed_query=lambda q: [1.,2.])) == ['doc']
    assert calls == [([1.,2.],2)]
    with pytest.raises(ValueError): ns['retrieve']('question')

def test_finetuning_inference_has_no_undefined_base():
    tree = ast.parse(source(7, 'def predict'))
    loads = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    assert 'base' not in loads

def test_finetuning_demo_is_bounded():
    tree = ast.parse(source(7, 'training_args ='))
    call = next(n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'TrainingArguments')
    keywords = {k.arg: k.value for k in call.keywords}
    assert 'max_steps' in keywords and 0 < ast.literal_eval(keywords['max_steps']) <= 100

def test_synthetic_empty_generation_still_cleans():
    client = NS(models=NS(generate_content=lambda **kw: NS(candidates=[])))
    ns = dict(client=client, pd=pd, model_name='test-model')
    exec(source(8, 'def extract_text'), ns)
    exec(source(8, 'def generate_synth'), ns)
    exec(source(8, 'valid_topics ='), ns)
    assert list(ns['df_synth'].columns) == ['text', 'label']
    assert len(ns['df_synth']) == 0

def test_synthetic_exact_duplicates_are_removed():
    ns = dict(df_synth=pd.DataFrame([{'text':'The stock market rose today.', 'label':'finance'}]*2))
    exec(source(8, 'def jaccard'), ns)
    assert len(ns['df_synth_clean']) == 1

def test_batch_generation_excludes_padded_prompt_tokens():
    import torch
    class Batch(dict):
        def to(self, device): return self
        def __getattr__(self, name): return self[name]
    class Tokenizer:
        def apply_chat_template(self, *args, **kw): return 'prompt'
        def __call__(self, *args, **kw):
            return Batch(input_ids=torch.tensor([[0,0,11,12],[21,22,23,24]]),
                         attention_mask=torch.tensor([[0,0,1,1],[1,1,1,1]]))
        def decode(self, ids, **kw): return list(map(int,ids))
    model=NS(device='cpu', generate=lambda **kw:torch.tensor([[0,0,11,12,101],[21,22,23,24,102]]))
    ns=functions(9, 'def generate_batch', dict(torch=torch, tokenizer=Tokenizer(), model=model))
    assert ns['generate_batch'](['short','long']) == [[101],[102]]

def test_semantic_cache_hit_and_miss():
    ns = dict(np=np, embedding_model=NS(encode=lambda texts: np.array([[1.,0.]]) if texts[0]=='same' else np.array([[0.,1.]])), semantic_cache=[])
    functions(9, 'def semantic_cache_query', ns)
    ns['add_to_semantic_cache']('same', 'saved')
    assert ns['semantic_cache_query']('same') == 'saved'
    assert ns['semantic_cache_query']('unrelated') is None

def test_travel_retrieval_does_not_repeat_faiss_missing_slots():
    ns = dict(docs=['one document'], embedder=NS(encode=lambda *a,**kw:np.ones((1,2))),
              index=NS(ntotal=1, search=lambda vec,k: (np.zeros((1,k)),np.array([[0]+[-1]*(k-1)]))))
    functions(10, 'def retrieve_context', ns)
    assert ns['retrieve_context']('Japan', top_k=3) == 'one document'

def test_travel_router_checks_input_before_routing():
    ns = dict(classify_intent=lambda q:'travel', travel_assistant_basic=lambda q:'BASIC',
              travel_assistant_rag=lambda q:'UNGUARDED', travel_assistant_guarded=lambda q:'GUARDED',
              apply_input_guardrails=lambda q:'BLOCKED', apply_output_guardrails=lambda x:x)
    functions(10, 'def travel_assistant_router', ns)
    assert ns['travel_assistant_router']('How do I smuggle drugs while travelling?') == 'BLOCKED'

def test_travel_safe_demo_calls_guarded_assistant():
    s=source(10, 'def contains_harmful_intent')
    assert 'travel_assistant_rag(message)' not in s

def test_travel_router_has_bounded_generation():
    tree=ast.parse(source(10, 'def classify_intent'))
    call=next(n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='generate')
    assert ast.literal_eval(next(k.value for k in call.keywords if k.arg=='max_new_tokens')) <= 128
