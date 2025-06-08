<!-- metadata -->
- **title**: GitHub - tensorzero/tensorzero: TensorZero creates a feedback loop for optimizing LLM applications — turning production data into smarter, faster, and cheaper models.
- **source**: https://github.com/tensorzero/tensorzero
- **author**: tensorzero
- **published**: 2025-06-04T18:18:34Z
- **fetched**: 2025-06-08T16:17:36Z
- **tags**: codex, LLM, optimization, open-source
- **image**: https://repository-images.githubusercontent.com/829640443/26b7c5c4-c12c-4e89-beaf-a4233f1dac87

## 要約
TensorZeroはLLMアプリケーションの運用データを活用し、モデルを継続的に改善するためのオープンソース基盤です。各種LLMプロバイダーを統一的に扱えるゲートウェイ、実行状況やフィードバックを取り込むオブザーバビリティ、プロンプトやモデル、推論設定を自動最適化する仕組み、効果検証のための評価・実験機能を備え、A/Bテストやルーティング、フォールバックも可能です。セルフホストで無料で利用でき、公式ドキュメントには5分で始められるクイックスタートが提供されています。
![TensorZero Logo](https://github.com/user-attachments/assets/47d67430-386d-4675-82ad-d4734d3262d9)

## 本文
TensorZero
==========

**TensorZero creates a feedback loop for optimizing LLM applications — turning production data into smarter, faster, and cheaper models.**

1. Integrate our model gateway
2. Send metrics or feedback
3. Optimize prompts, models, and inference strategies
4. Watch your LLMs improve over time

It provides a
**data & learning flywheel for LLMs**
by unifying:

* **Inference:**
  one API for all LLMs, with <1ms P99 overhead
* **Observability:**
  inference & feedback → your database
* **Optimization:**
  from prompts to fine-tuning and RL
* **Evaluations:**
  compare prompts, models, inference strategies
* **Experimentation:**
  built-in A/B testing, routing, fallbacks

---

**[Website](https://www.tensorzero.com/)**
·
**[Docs](https://www.tensorzero.com/docs)**
·
**[Twitter](https://www.x.com/tensorzero)**
·
**[Slack](https://www.tensorzero.com/slack)**
·
**[Discord](https://www.tensorzero.com/discord)**
  
  
**[Quick Start (5min)](https://www.tensorzero.com/docs/quickstart)**
·
**[Comprehensive Tutorial](https://www.tensorzero.com/docs/gateway/tutorial)**
·
**[Deployment Guide](https://www.tensorzero.com/docs/gateway/deployment)**
·
**[API Reference](https://www.tensorzero.com/docs/gateway/api-reference)**
·
**[Configuration Reference](https://www.tensorzero.com/docs/gateway/deployment)**

---



|  |  |
| --- | --- |
| **What is TensorZero?** | TensorZero is an open-source framework for building production-grade LLM applications. It unifies an LLM gateway, observability, optimization, evaluations, and experimentation. |
| **How is TensorZero different from other LLM frameworks?** | 1. TensorZero enables you to optimize complex LLM applications based on production metrics and human feedback.   2. TensorZero supports the needs of industrial-scale LLM applications: low latency, high throughput, type safety, self-hosted, GitOps, customizability, etc.   3. TensorZero unifies the entire LLMOps stack, creating compounding benefits. For example, LLM evaluations can be used for fine-tuning models alongside AI judges. |
| **Can I use TensorZero with \_\_\_?** | Yes. Every major programming language is supported. You can use TensorZero with our Python client, any OpenAI SDK, or our HTTP API. |
| **Is TensorZero production-ready?** | Yes. Here's a case study: **[Automating Code Changelogs at a Large Bank with LLMs](https://www.tensorzero.com/blog/case-study-automating-code-changelogs-at-a-large-bank-with-llms)** |
| **How much does TensorZero cost?** | Nothing. TensorZero is 100% self-hosted and open-source. There are no paid features. |
| **Who is building TensorZero?** | Our technical team includes a former Rust compiler maintainer, machine learning researchers (Stanford, CMU, Oxford, Columbia) with thousands of citations, and the chief product officer of a decacorn startup. We're backed by the same investors as leading open-source projects (e.g. ClickHouse, CockroachDB) and AI labs (e.g. OpenAI, Anthropic). |
| **How do I get started?** | You can adopt TensorZero incrementally. Our **[Quick Start](https://www.tensorzero.com/docs/quickstart)** goes from a vanilla OpenAI wrapper to a production-ready LLM application with observability and fine-tuning in just 5 minutes. |



---

Features
--------

### 🌐 LLM Gateway

> **Integrate with TensorZero once and access every major LLM provider.**

|
|  |
| **Model Providers** | **Features** |
| The TensorZero Gateway natively supports:   * **[Anthropic](https://www.tensorzero.com/docs/gateway/guides/providers/anthropic)** * **[AWS Bedrock](https://www.tensorzero.com/docs/gateway/guides/providers/aws-bedrock)** * **[AWS SageMaker](https://www.tensorzero.com/docs/gateway/guides/providers/aws-sagemaker)** * **[Azure OpenAI Service](https://www.tensorzero.com/docs/gateway/guides/providers/azure)** * **[DeepSeek](https://www.tensorzero.com/docs/gateway/guides/providers/deepseek)** * **[Fireworks](https://www.tensorzero.com/docs/gateway/guides/providers/fireworks)** * **[GCP Vertex AI Anthropic](https://www.tensorzero.com/docs/gateway/guides/providers/gcp-vertex-ai-anthropic)** * **[GCP Vertex AI Gemini](https://www.tensorzero.com/docs/gateway/guides/providers/gcp-vertex-ai-gemini)** * **[Google AI Studio (Gemini API)](https://www.tensorzero.com/docs/gateway/guides/providers/google-ai-studio-gemini)** * **[Hyperbolic](https://www.tensorzero.com/docs/gateway/guides/providers/hyperbolic)** * **[Mistral](https://www.tensorzero.com/docs/gateway/guides/providers/mistral)** * **[OpenAI](https://www.tensorzero.com/docs/gateway/guides/providers/openai)** * **[Together](https://www.tensorzero.com/docs/gateway/guides/providers/together)** * **[vLLM](https://www.tensorzero.com/docs/gateway/guides/providers/vllm)** * **[xAI](https://www.tensorzero.com/docs/gateway/guides/providers/xai)**   *Need something else? Your provider is most likely supported because TensorZero integrates with **[any OpenAI-compatible API (e.g. Ollama)](https://www.tensorzero.com/docs/gateway/guides/providers/openai-compatible)** .* | The TensorZero Gateway supports advanced features like:   * **[Retries & Fallbacks](https://www.tensorzero.com/docs/gateway/guides/retries-fallbacks)** * **[Inference-Time Optimizations](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations)** * **[Prompt Templates & Schemas](https://www.tensorzero.com/docs/gateway/guides/prompt-templates-schemas)** * **[Experimentation (A/B Testing)](https://www.tensorzero.com/docs/gateway/tutorial#experimentation)** * **[Configuration-as-Code (GitOps)](https://www.tensorzero.com/docs/gateway/configuration-reference)** * **[Batch Inference](https://www.tensorzero.com/docs/gateway/guides/batch-inference)** * **[Multimodal Inference (VLMs)](https://www.tensorzero.com/docs/gateway/guides/multimodal-inference)** * **[Inference Caching](https://www.tensorzero.com/docs/gateway/guides/inference-caching)** * **[Metrics & Feedback](https://www.tensorzero.com/docs/gateway/guides/metrics-feedback)** * **[Multi-Step LLM Workflows (Episodes)](https://www.tensorzero.com/docs/gateway/guides/episodes)** * *& a lot more...*   The TensorZero Gateway is written in Rust 🦀 with **performance** in mind (<1ms p99 latency overhead @ 10k QPS). See **[Benchmarks](https://www.tensorzero.com/docs/gateway/benchmarks)** .  You can run inference using the **TensorZero client** (recommended), the **OpenAI client** , or the **HTTP API** . |

  


**Usage: Python — TensorZero Client (Recommended)**

You can access any provider using the TensorZero Python client.

1. `pip install tensorzero`
2. Optional: Set up the TensorZero configuration.
3. Run inference:

```
from tensorzero import TensorZeroGateway  # or AsyncTensorZeroGateway


with TensorZeroGateway.build_embedded(clickhouse_url="...", config_file="...") as client:
    response = client.inference(
        model_name="openai::gpt-4o-mini",
        # Try other providers easily: "anthropic::claude-3-7-sonnet-20250219"
        input={
            "messages": [
                {
                    "role": "user",
                    "content": "Write a haiku about artificial intelligence.",
                }
            ]
        },
    )
```

See
**[Quick Start](https://www.tensorzero.com/docs/quickstart)**
for more information.



**Usage: Python — OpenAI Client**

You can access any provider using the OpenAI Python client with TensorZero.

1. `pip install tensorzero`
2. Optional: Set up the TensorZero configuration.
3. Run inference:

```
from openai import OpenAI  # or AsyncOpenAI
from tensorzero import patch_openai_client

client = OpenAI()

patch_openai_client(
    client,
    clickhouse_url="http://chuser:chpassword@localhost:8123/tensorzero",
    config_file="config/tensorzero.toml",
    async_setup=False,
)

response = client.chat.completions.create(
    model="tensorzero::model_name::openai::gpt-4o-mini",
    # Try other providers easily: "tensorzero::model_name::anthropic::claude-3-7-sonnet-20250219"
    messages=[
        {
            "role": "user",
            "content": "Write a haiku about artificial intelligence.",
        }
    ],
)
```

See
**[Quick Start](https://www.tensorzero.com/docs/quickstart)**
for more information.



**Usage: JavaScript / TypeScript (Node) — OpenAI Client**

You can access any provider using the OpenAI Node client with TensorZero.

1. Deploy
   `tensorzero/gateway`
   using Docker.
   **[Detailed instructions →](https://www.tensorzero.com/docs/gateway/deployment)**
2. Set up the TensorZero configuration.
3. Run inference:

```
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "http://localhost:3000/openai/v1",
});

const response = await client.chat.completions.create({
  model: "tensorzero::model_name::openai::gpt-4o-mini",
  // Try other providers easily: "tensorzero::model_name::anthropic::claude-3-7-sonnet-20250219"
  messages: [
    {
      role: "user",
      content: "Write a haiku about artificial intelligence.",
    },
  ],
});
```

See
**[Quick Start](https://www.tensorzero.com/docs/quickstart)**
for more information.



**Usage: Other Languages & Platforms — HTTP API**

TensorZero supports virtually any programming language or platform via its HTTP API.

1. Deploy
   `tensorzero/gateway`
   using Docker.
   **[Detailed instructions →](https://www.tensorzero.com/docs/gateway/deployment)**
2. Optional: Set up the TensorZero configuration.
3. Run inference:

```
curl -X POST "http://localhost:3000/inference" \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "openai::gpt-4o-mini",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": "Write a haiku about artificial intelligence."
        }
      ]
    }
  }'
```

See
**[Quick Start](https://www.tensorzero.com/docs/quickstart)**
for more information.

  

### 📈 LLM Optimization

> **Send production metrics and human feedback to easily optimize your prompts, models, and inference strategies — using the UI or programmatically.**

#### Model Optimization

Optimize closed-source and open-source models using supervised fine-tuning (SFT) and preference fine-tuning (DPO).

|
|  |
| **Supervised Fine-tuning — UI** | **Preference Fine-tuning (DPO) — Jupyter Notebook** |
|  |  |

#### Inference-Time Optimization

Boost performance by dynamically updating your prompts with relevant examples, combining responses from multiple inferences, and more.

|
|  |
| **[Best-of-N Sampling](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations#miprov2)** | **[Mixture-of-N Sampling](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations#mixture-of-n-sampling)** |
|  |  |
| **[Dynamic In-Context Learning (DICL)](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations#dynamic-in-context-learning-dicl)** | **[Chain-of-Thought (CoT)](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations#chain-of-thought-cot)** |
|  |  |

*More coming soon...*

  

#### Prompt Optimization

Optimize your prompts programmatically using research-driven optimization techniques.

|
|  |
| **[MIPROv2](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations#miprov2)** | **[DSPy Integration](https://github.com/tensorzero/tensorzero/tree/main/examples/gsm8k-custom-recipe-dspy)** |
| [MIPROv2 diagram](https://github.com/user-attachments/assets/d81a7c37-382f-4c46-840f-e6c2593301db) | TensorZero comes with several optimization recipes, but you can also easily create your own. This example shows how to optimize a TensorZero function using an arbitrary tool — here, DSPy, a popular library for automated prompt engineering. |

*More coming soon...*

  

### 🔍 LLM Observability

> **Zoom in to debug individual API calls, or zoom out to monitor metrics across models and prompts over time — all using the open-source TensorZero UI.**

|
|  |
| **Observability » Inference** | **Observability » Function** |
|  |  |

  

### 📊 LLM Evaluations

> **Compare prompts, models, and inference strategies using TensorZero Evaluations — with support for heuristics and LLM judges.**

|
|  |
| **Evaluation » UI** | **Evaluation » CLI** |
|  | ``` docker compose run --rm evaluations \   --evaluation-name extract_data \   --dataset-name hard_test_cases \   --variant-name gpt_4o \   --concurrency 5 ```  ``` Run ID: 01961de9-c8a4-7c60-ab8d-15491a9708e4 Number of datapoints: 100 ██████████████████████████████████████ 100/100 exact_match: 0.83 ± 0.03 semantic_match: 0.98 ± 0.01 item_count: 7.15 ± 0.39 ``` |

Demo
----

> **Watch LLMs get better at data extraction in real-time with TensorZero!**
>
> **[Dynamic in-context learning (DICL)](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations#dynamic-in-context-learning-dicl)**
> is a powerful inference-time optimization available out of the box with TensorZero.
> It enhances LLM performance by automatically incorporating relevant historical examples into the prompt, without the need for model fine-tuning.



LLM Engineering with TensorZero
-------------------------------

  


  

1. The
   **[TensorZero Gateway](https://www.tensorzero.com/docs/gateway/)**
   is a high-performance model gateway written in Rust 🦀 that provides a unified API interface for all major LLM providers, allowing for seamless cross-platform integration and fallbacks.
2. It handles structured schema-based inference with <1ms P99 latency overhead (see
   **[Benchmarks](https://www.tensorzero.com/docs/gateway/benchmarks)**
   ) and built-in observability, experimentation, and
   **[inference-time optimizations](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations)**
   .
3. It also collects downstream metrics and feedback associated with these inferences, with first-class support for multi-step LLM systems.
4. Everything is stored in a ClickHouse data warehouse that you control for real-time, scalable, and developer-friendly analytics.
5. Over time,
   **[TensorZero Recipes](https://www.tensorzero.com/docs/recipes)**
   leverage this structured dataset to optimize your prompts and models: run pre-built recipes for common workflows like fine-tuning, or create your own with complete flexibility using any language and platform.
6. Finally, the gateway's experimentation features and GitOps orchestration enable you to iterate and deploy with confidence, be it a single LLM or thousands of LLMs.

Our goal is to help engineers build, manage, and optimize the next generation of LLM applications: systems that learn from real-world experience.
Read more about our
**[Vision & Roadmap](https://www.tensorzero.com/docs/vision-roadmap/)**
.

Get Started
-----------

**Start building today.**
The
**[Quick Start](https://www.tensorzero.com/docs/quickstart)**
shows it's easy to set up an LLM application with TensorZero.
If you want to dive deeper, the
**[Tutorial](https://www.tensorzero.com/docs/gateway/tutorial)**
teaches how to build a simple chatbot, an email copilot, a weather RAG system, and a structured data extraction pipeline.

**Questions?**
Ask us on
**[Slack](https://www.tensorzero.com/slack)**
or
**[Discord](https://www.tensorzero.com/discord)**
.

**Using TensorZero at work?**
Email us at
**[hello@tensorzero.com](mailto:hello@tensorzero.com)**
to set up a Slack or Teams channel with your team (free).

**Work with us.**
We're
**[hiring in NYC](https://www.tensorzero.com/jobs)**
.
We'd also welcome
**[open-source contributions](https://github.com/tensorzero/tensorzero/blob/main/CONTRIBUTING.md)**
!

Examples
--------

We are working on a series of
**complete runnable examples**
illustrating TensorZero's data & learning flywheel.

> **[Optimizing Data Extraction (NER) with TensorZero](https://github.com/tensorzero/tensorzero/tree/main/examples/data-extraction-ner)**
>
> This example shows how to use TensorZero to optimize a data extraction pipeline.
> We demonstrate techniques like fine-tuning and dynamic in-context learning (DICL).
> In the end, an optimized GPT-4o Mini model outperforms GPT-4o on this task — at a fraction of the cost and latency — using a small amount of training data.

> **[Agentic RAG — Multi-Hop Question Answering with LLMs](https://github.com/tensorzero/tensorzero/tree/main/examples/rag-retrieval-augmented-generation/simple-agentic-rag/)**
>
> This example shows how to build a multi-hop retrieval agent using TensorZero.
> The agent iteratively searches Wikipedia to gather information, and decides when it has enough context to answer a complex question.

> **[Writing Haikus to Satisfy a Judge with Hidden Preferences](https://github.com/tensorzero/tensorzero/tree/main/examples/haiku-hidden-preferences)**
>
> This example fine-tunes GPT-4o Mini to generate haikus tailored to a specific taste.
> You'll see TensorZero's "data flywheel in a box" in action: better variants leads to better data, and better data leads to better variants.
> You'll see progress by fine-tuning the LLM multiple times.

> **[Improving LLM Chess Ability with Best-of-N Sampling](https://github.com/tensorzero/tensorzero/tree/main/examples/chess-puzzles/)**
>
> This example showcases how best-of-N sampling can significantly enhance an LLM's chess-playing abilities by selecting the most promising moves from multiple generated options.

> **[Improving Math Reasoning with a Custom Recipe for Automated Prompt Engineering (DSPy)](https://github.com/tensorzero/tensorzero/tree/main/examples/gsm8k-custom-recipe-dspy)**
>
> TensorZero provides a number of pre-built optimization recipes covering common LLM engineering workflows.
> But you can also easily create your own recipes and workflows!
> This example shows how to optimize a TensorZero function using an arbitrary tool — here, DSPy.

*& many more on the way!*
