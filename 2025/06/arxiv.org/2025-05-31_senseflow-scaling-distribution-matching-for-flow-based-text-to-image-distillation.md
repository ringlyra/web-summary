<!-- metadata -->

- **title**: SenseFlow: Scaling Distribution Matching for Flow-based Text-to-Image Distillation
- **source**: https://arxiv.org/abs/2506.00523
- **author**: Ge, Xingtong, Zhang, Xin, Xu, Tongda, Zhang, Yi, Zhang, Xinjie, Wang, Yan, Zhang, Jun
- **published**: 2025-05-31
- **fetched**: 2025-06-04T04:40:02Z
- **tags**: codex, machine-learning, diffusion-model, image-generation
- **image**: https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

Flowベース画像生成モデル向け蒸留を改善する**SenseFlow**を提案。分布整合法とステップ再重み付けを導入し、SD 3.5やFLUXで収束性と性能を向上。

## 本文 / Article

> Abstract:The Distribution Matching Distillation (DMD) has been successfully applied to text-to-image diffusion models such as Stable Diffusion (SD) 1.5. However, vanilla DMD suffers from convergence difficulties on large-scale flow-based text-to-image models, such as SD 3.5 and FLUX. In this paper, we first analyze the issues when applying vanilla DMD on large-scale models. Then, to overcome the scalability challenge, we propose implicit distribution alignment (IDA) to regularize the distance between the generator and fake distribution. Furthermore, we propose intra-segment guidance (ISG) to relocate the timestep importance distribution from the teacher model. With IDA alone, DMD converges for SD 3.5; employing both IDA and ISG, DMD converges for SD 3.5 and FLUX.1 dev. Along with other improvements such as scaled up discriminator models, our final model, dubbed \textbf{SenseFlow}, achieves superior performance in distillation for both diffusion based text-to-image models such as SDXL, and flow-matching models such as SD 3.5 Large and FLUX. The source code will be avaliable at [this https URL](https://github.com/XingtongGe/SenseFlow).
