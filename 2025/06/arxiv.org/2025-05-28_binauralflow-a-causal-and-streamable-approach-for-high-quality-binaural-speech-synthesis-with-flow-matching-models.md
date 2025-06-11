<!-- metadata -->

- **title**: BinauralFlow: A Causal and Streamable Approach for High-Quality Binaural Speech Synthesis with Flow Matching Models
- **source**: https://arxiv.org/abs/2505.22865
- **author**: Liang, Susan, Markovic, Dejan, Gebru, Israel D., Krenn, Steven, Keebler, Todd, Sandakly, Jacob, Yu, Frank, Hassel, Samuel, Xu, Chenliang, Richard, Alexander
- **published**: 2025-05-28
- **fetched**: 2025-06-04T04:41:53.009201Z
- **tags**: codex, ai
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

単声から高品質なバイノーラル音声を生成する**BinauralFlow**を提案。**フローマッチング**と因果**U-Net**でストリーミング推論を実現、従来法より高品質。

## 本文 / Article

> Abstract:Binaural rendering aims to synthesize binaural audio that mimics natural hearing based on a mono audio and the locations of the speaker and listener. Although many methods have been proposed to solve this problem, they struggle with rendering quality and streamable inference. Synthesizing high-quality binaural audio that is indistinguishable from real-world recordings requires precise modeling of binaural cues, room reverb, and ambient sounds. Additionally, real-world applications demand streaming inference. To address these challenges, we propose a flow matching based streaming binaural speech synthesis framework called BinauralFlow. We consider binaural rendering to be a generation problem rather than a regression problem and design a conditional flow matching model to render high-quality audio. Moreover, we design a causal U-Net architecture that estimates the current audio frame solely based on past information to tailor generative models for streaming inference. Finally, we introduce a continuous inference pipeline incorporating streaming STFT/ISTFT operations, a buffer bank, a midpoint solver, and an early skip schedule to improve rendering continuity and speed. Quantitative and qualitative evaluations demonstrate the superiority of our method over SOTA approaches. A perceptual study further reveals that our model is nearly indistinguishable from real-world recordings, with a $42\%$ confusion rate.

|           |                                                                                               |
| --------- | --------------------------------------------------------------------------------------------- |
| Comments: | ICML 2025, 18 pages                                                                           |
| Subjects: | Sound (cs.SD); Artificial Intelligence (cs.AI); Audio and Speech Processing (eess.AS)         |
| Cite as:  | [arXiv:2505.22865](https://arxiv.org/abs/2505.22865) [cs.SD]                                  |
|           | (or [arXiv:2505.22865v1](https://arxiv.org/abs/2505.22865v1) [cs.SD] for this version)        |
|           | <https://doi.org/10.48550/arXiv.2505.22865> Focus to learn more arXiv-issued DOI via DataCite |
