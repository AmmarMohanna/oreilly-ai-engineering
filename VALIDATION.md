# Colab validation — 12 October 2026

All 10 notebooks passed live execution on a Colab Tesla T4. The retained evidence contains 11 runs and 108 executed code cells: notebook 1 was run in both modes, and notebook 10 was also tested through its live Gradio page. **40 component regression checks passed in Colab.**

Tested notebook source commit: `1291ff8c2e80f1283199cdaa82a3b06064cffdab`. Each retained source hash was checked against the repaired repository. The documentation commit that adds this record does not change notebook sources.

## Execution results

Each notebook used a fresh kernel and working directory on the same Colab VM. Timings include dependency installation and vary with model caches and API latency. The links below open the exact tested notebook versions.

| Notebook | Mode | Cells executed | Seconds | Result |
|---|---|---:|---:|---|
| [1.From Model Training to Model Steering](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%201/1.From%20Model%20Training%20to%20Model%20Steering.ipynb) | default | 6/6 | 83.7 | Pass |
| [1.From Model Training to Model Steering](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%201/1.From%20Model%20Training%20to%20Model%20Steering.ipynb) | gemini | 6/6 | 42.8 | Pass |
| [2.Exploring LLM Behavior with Configurations](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%201/2.Exploring%20LLM%20Behavior%20with%20Configurations.ipynb) | default | 4/4 | 29.7 | Pass |
| [3.Evaluating AI-Generated Text_ Automatic Metrics vs. Human Judgments](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%201/3.Evaluating%20AI-Generated%20Text_%20Automatic%20Metrics%20vs.%20Human%20Judgments.ipynb) | default | 13/13 | 66.4 | Pass |
| [4.LLM Application Evaluation Pipeline_ Qwen Translation Model](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%201/4.LLM%20Application%20Evaluation%20Pipeline_%20Qwen%20Translation%20Model.ipynb) | default | 6/6 | 59.1 | Pass |
| [5.Safe Prompt Engineering & Guardrails ](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%201/5.Safe%20Prompt%20Engineering%20%26%20Guardrails%20.ipynb) | default | 8/8 | 14.6 | Pass |
| [6.Hands‑On_ RAG & Agents with Gemini](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%202/6.Hands%E2%80%91On_%20RAG%20%26%20Agents%20with%20Gemini.ipynb) | default | 17/17 | 57.1 | Pass |
| [7.Hands-on_ Fine-Tuning Qwen with QLoRA](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%202/7.Hands-on_%20Fine-Tuning%20Qwen%20with%20QLoRA.ipynb) | default | 15/15 | 296.8 | Pass |
| [8.Hands-on_ Synthetic Dataset Creation - Topic Classification](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%202/8.Hands-on_%20Synthetic%20Dataset%20Creation%20-%20Topic%20Classification.ipynb) | default | 10/10 | 21.9 | Pass |
| [9.Hands-on_ LLM Inference Optimization with Batching and Caching](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%202/9.Hands-on_%20LLM%20Inference%20Optimization%20with%20Batching%20and%20Caching.ipynb) | default | 12/12 | 108.1 | Pass |
| [10.Hands-on_ Building an End-to-End LLM Travel Assistant](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/1291ff8c2e80f1283199cdaa82a3b06064cffdab/Day%202/10.Hands-on_%20Building%20an%20End-to-End%20LLM%20Travel%20Assistant.ipynb) | interactive | 11/11 | 47.6 | Pass |

## Behavior checked

- Real Gemini completions and structured judging; both notebook 1 modes.
- English/French translations and multilingual similarity scores.
- Prompt-injection refusal and category-output validation.
- RAG retrieval and a real LangChain agent tool call.
- All 60 QLoRA optimizer steps, saved adapter, and post-training predictions. The final examples produce `positive`, `negative`, and `neutral`. The initial run's blank predictions were caught by output inspection and repaired with consistent Qwen chat formatting and completion-only decoding.
- Synthetic JSON generation, filtering, duplicate removal and dataset export.
- Batched generation and warm-cache hits, including paraphrased queries.
- Travel routing, including the corrected landmark example. Browser requests returned a grounded Japan answer, refused a prompt-injection request, and declined an unrelated question. The temporary public Gradio server and its kernel were then shut down.
- Final evaluation plots inspected visually; invalid scores, constant correlations and overlapping labels covered by regression checks.

## Environment and limits

Python 3.13.15; PyTorch 2.11.0+cu130; Tesla T4; Transformers 4.57.6; google-genai 1.75.0; OpenAI SDK 2.54.0; LangChain 1.4.3; langchain-google-genai 4.3.7; PEFT 0.21.1; bitsandbytes 0.50.2; Gradio 6.17.3.

The default Gemini model tested was `gemini-3.5-flash-lite`; notebook 1 also used `gemini-3.8-flash`. Gemini calls used the authorized `GOOGLE_API_KEY` secret. Public Hugging Face models and datasets required no HF login. Credentials are absent from committed sources and exported evidence.

These checks establish execution and the documented examples, not general model accuracy or production-grade guardrail security. Notebook 3's human ratings are explicitly illustrative. Notebook 10 uses sample documents by default and launches a public Gradio link only when `LAUNCH_UI=True` is set deliberately.

Run the checks again using the commands in the [README](README.md#notebook-validation). `scripts/validate_notebooks.py` preserves executed notebooks, source hashes, package versions and a JSON summary; API/model availability can change after this validation date.
