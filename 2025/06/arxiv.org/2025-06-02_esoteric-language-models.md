<!-- metadata -->

- **title**: Esoteric Language Models
- **source**: https://arxiv.org/abs/2506.01928
- **author**: arxiv.org
- **published**: 2025-06-02T00:00:00Z
- **fetched**: 2025-06-04T04:40:56Z
- **tags**: codex, ai, language model, diffusion
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

拡散型LMとARモデルを融合した**Eso-LMs**を提案。**KVキャッシュ**を導入し、従来比**65倍高速**かつ高精度な生成を実現。

## 本文 / Article

> Diffusion-based language models offer a compelling alternative to autoregressive (AR) models by enabling parallel and controllable generation. Among this family of models, Masked Diffusion Models (MDMs) achieve the strongest performance but still underperform AR models in perplexity and lack key inference-time efficiency features--most notably, KV caching. In this work, we introduce Eso-LMs, a new family of models that fuses AR and MDM paradigms, enabling smooth interpolation between their perplexities while overcoming their respective limitations. Eso-LMs set a new state of the art on standard language modeling benchmarks. Crucially, we are the \*\*first to introduce KV caching for MDMs\*\* while preserving parallel generation, significantly improving inference efficiency. Combined with an optimized sampling schedule, our method achieves up to \*\*65x\*\* faster inference than standard MDMs and \*\*4x\*\* faster inference than prior semi-autoregressive approaches. We provide the code and model checkpoints on the project page: [http://s-sahoo.github.io/Eso-LMs](http://s-sahoo.github.io/Eso-LMs)
