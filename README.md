# AI Engineering Bootcamp

<div align="center">

<img src="assets/images/O'Reilly_Logo.png" alt="O'Reilly Logo" width="300">

**From theory to production with evaluations, prompting, RAG, and agents**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/ammarmohanna/)
[![Website](https://img.shields.io/badge/Website-Visit-green?style=flat)](https://www.ammarmohanna.ai)

</div>

---

## 📖 Book Reference

This bootcamp is based on the book **AI Engineering** by Chip Huyen. For additional resources, examples, and supporting materials:

- 📚 [Official Book GitHub Repository](https://github.com/chiphuyen/aie-book)
- 📖 [Read AI Engineering on O'Reilly](https://learning.oreilly.com/library/view/ai-engineering/9781098166298/)

---

## 📚 Course Overview

The AI engineering field is moving beyond model-centric ML to a product-centric approach that brings foundation models into production. This two-day, hands-on bootcamp distills the essentials of building applications with foundation models, following a "production first" philosophy: start simple, optimize instructions and context before touching the model, and always tie model behavior to user experience and product value.

### What You'll Learn

- **Foundation Models**: Understand the anatomy of foundation models and how to control their behavior through generation settings
- **Evaluation Methods**: Design systematic evaluation pipelines combining AI-as-a-judge metrics with human review
- **Prompt Engineering**: Master prompt design principles, few-shot prompting, and implement guardrails to mitigate attacks
- **RAG & Agents**: Build context through retrieval-augmented generation and tool-based agents
- **Fine-Tuning**: Decide when and how to fine-tune models versus relying on prompts and retrieval
- **Data Engineering**: Source, annotate, synthesize, and process data to support adaptation and evaluation
- **Inference Optimization**: Optimize latency and cost at the model, hardware, and service layers

### Prerequisites

- Python programming experience
- Familiarity with basic machine learning concepts
- Prior exposure to large language models (helpful but not required)

---

## 👨‍🏫 Instructor

**Ammar Mohanna**  
AI Consulting, Delivery, and Teaching

- 🔗 [LinkedIn](https://www.linkedin.com/in/ammarmohanna/)
- 🌐 [Personal Website](https://www.ammarmohanna.ai)

Ammar works across consulting and academia as AI Engineering Lead at EDT&Partners, Lecturer at the American University of Beirut, and Expert Contributor at O'Reilly. He helps companies, universities, and investors scope, evaluate, and build AI systems that are useful, measurable, and technically defensible.

His work covers technical scoping, architecture, evaluation design, agentic workflows, MLOps/LLMOps, production reliability, and independent review. He holds a PhD in edge artificial intelligence from the University of Genoa, Italy.

---

## 🎓 Other Courses by Ammar Mohanna

- **MLOps/LLMOps Bootcamp** (Live Course) - [View Course](https://learning.oreilly.com/live-events/mlopsllmops-bootcamp/0642572182861/)
- **Hand-On Agentic GraphRAG** (Live Course) - [View Course](https://learning.oreilly.com/live-events/-/0642572339340/)
- **Testing AI Systems: Crafting Trust, Quality, and Performance** (On-Demand Course) - [View Course](https://learning.oreilly.com/course/testing-ai-systems/0642572060008/)

---

## 📅 Course Schedule

### Day 1: AI Engineering Fundamentals

| Session | Topic | Colab Notebook |
|---------|-------|----------------|
| 1 | From Model Training to Model Steering | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%201/1.From%20Model%20Training%20to%20Model%20Steering.ipynb) |
| 2 | Exploring LLM Behavior with Configurations | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%201/2.Exploring%20LLM%20Behavior%20with%20Configurations.ipynb) |
| 3 | Evaluating AI-Generated Text: Automatic Metrics vs. Human Judgments | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%201/3.Evaluating%20AI-Generated%20Text_%20Automatic%20Metrics%20vs.%20Human%20Judgments.ipynb) |
| 4 | LLM Application Evaluation Pipeline: Qwen Translation Model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%201/4.LLM%20Application%20Evaluation%20Pipeline_%20Qwen%20Translation%20Model.ipynb) |
| 5 | Safe Prompt Engineering & Guardrails | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%201/5.Safe%20Prompt%20Engineering%20%26%20Guardrails%20.ipynb) |

**Day 1 Topics:**
- Introduction to AI engineering and foundation model applications
- The anatomy of foundation models and decoding strategies
- Evaluation methods and metrics for generative models
- Evaluation pipeline design and observability
- Prompt engineering principles and security

📊 [Day 1 Slide Deck](https://drive.google.com/file/d/1qjbclEOO8h4piYVQKCO7y83KSYpJtQKK/view?usp=sharing)

---

### Day 2: Advanced Techniques and Full Stack Development

| Session | Topic | Colab Notebook |
|---------|-------|----------------|
| 6 | Hands-On: RAG & Agents with Gemini | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%202/6.Hands%E2%80%91On_%20RAG%20%26%20Agents%20with%20Gemini.ipynb) |
| 7 | Hands-on: Fine-Tuning Qwen with QLoRA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%202/7.Hands-on_%20Fine-Tuning%20Qwen%20with%20QLoRA.ipynb) |
| 8 | Hands-on: Synthetic Dataset Creation - Topic Classification | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%202/8.Hands-on_%20Synthetic%20Dataset%20Creation%20-%20Topic%20Classification.ipynb) |
| 9 | Hands-on: LLM Inference Optimization with Batching and Caching | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%202/9.Hands-on_%20LLM%20Inference%20Optimization%20with%20Batching%20and%20Caching.ipynb) |
| 10 | Hands-on: Building an End-to-End LLM Travel Assistant | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AmmarMohanna/oreilly-ai-engineering/blob/main/Day%202/10.Hands-on_%20Building%20an%20End-to-End%20LLM%20Travel%20Assistant.ipynb) |

**Day 2 Topics:**
- Context construction through RAG and agent architectures
- Fine-tuning strategies and parameter-efficient techniques
- Data engineering for AI applications
- Inference optimization and cost reduction
- End-to-end application development

📊 [Day 2 Slide Deck](https://drive.google.com/file/d/1nSk8Dv7pBHMpab2NQGvmcjIxP9DSbuiD/view?usp=sharing)

---

## 🚀 Getting Started

All course materials are designed to run in **Google Colab**. Simply click on the "Open In Colab" badges above to launch each notebook in your browser. No local setup required!

The badges open the notebooks from this repository, so GitHub fixes are also available in Colab. Use a fresh runtime and run the dependency cell first. Select a **T4 GPU** for notebooks 3, 4, 7, 9, and 10; QLoRA in notebook 7 requires CUDA.

For Gemini exercises, add `GOOGLE_API_KEY` to Colab Secrets and enable notebook access. `GEMINI_API_KEY` is accepted as an alternative. Public Hugging Face datasets and models do not require an HF token. The default Gemini model is `gemini-3.5-flash-lite`; set `GEMINI_MODEL` in the environment to choose another supported model. Notebook 1 defaults to the local sentiment model and includes an optional Gemini mode.

Notebook 10 includes sample documents when no PDFs have been uploaded. Its Gradio interface is constructed during **Run all**; the final cell explains how to launch it deliberately.

### Notebook validation

Component regression checks (no API calls or model downloads):

```bash
python -m pip install pytest nbformat ipython numpy pandas torch matplotlib seaborn scipy
python -m pytest tests -q
```

Full execution uses a separate fresh kernel and working directory for each notebook. It retains executed notebooks, package versions, source hashes, and a JSON result summary under `validation-results/`. Provide `GOOGLE_API_KEY` in the environment and use a CUDA GPU:

```bash
python -m pip install nbformat nbclient ipykernel
python scripts/validate_notebooks.py --gemini-branch
```

Use `--only 2 5 8` to run selected labs. A failed notebook produces a nonzero exit status. Component tests alone do not establish that API calls, model downloads, or GPU training work.

### Quick Links

- 📖 [Course on O'Reilly Learning](https://learning.oreilly.com/live-events/ai-engineering-bootcamp/0642572259280/)
- 📚 Recommended Reading:
  - *AI Engineering* by Chip Huyen - [Read on O'Reilly](https://learning.oreilly.com/library/view/ai-engineering/9781098166298/)
  - *Designing Machine Learning Systems* by Chip Huyen - [Read on O'Reilly](https://learning.oreilly.com/library/view/designing-machine-learning/9781098107956/)
  - *LLMOps* by Abi Aryan - [Read on O'Reilly](https://learning.oreilly.com/library/view/llmops/9781098154196/)

---

## 📝 Course Philosophy

This course follows a **"production first"** approach:

1. **Start Simple**: Begin with basic implementations before optimizing
2. **Optimize Instructions and Context**: Leverage prompting and RAG before fine-tuning
3. **Tie to User Experience**: Always connect model behavior to product value
4. **Continuous Evaluation**: Implement feedback loops for continuous improvement

---

## 🤝 Contributing

This repository contains course materials for the O'Reilly AI Engineering Bootcamp. For questions or feedback, please reach out through the course platform or connect with the instructor on LinkedIn.
