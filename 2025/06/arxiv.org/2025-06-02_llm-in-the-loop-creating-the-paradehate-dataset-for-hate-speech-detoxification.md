<!-- metadata -->

- **title**: LLM in the Loop: Creating the PARADEHATE Dataset for Hate Speech Detoxification
- **source**: https://arxiv.org/abs/2506.01484
- **author**: Yuan, Shuzhou, Nie, Ercong, Kouba, Lukas, Kangen, Ashish Yashwanth, Schmid, Helmut, Schutze, Hinrich, Farber, Michael
- **published**: 2025-06-02T00:00:00Z
- **fetched**: 2025-06-04T01:37:48Z
- **tags**: codex, dataset, nlp, ai
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

LLM-in-the-loop を活用してヘイトスピーチを無害化するデータセットPARADEHATEを生成。GPT-4o-miniで注釈を自動化し、BARTなどで検証、デトックス性能向上を示す。8kペアを公開。

## 本文 / Article

[Submitted on 2 Jun 2025]

# Title:LLM in the Loop: Creating the PARADEHATE Dataset for Hate Speech Detoxification

Authors:[Shuzhou Yuan](https://arxiv.org/search/cs?searchtype=author&query=Yuan,+S), [Ercong Nie](https://arxiv.org/search/cs?searchtype=author&query=Nie,+E), [Lukas Kouba](https://arxiv.org/search/cs?searchtype=author&query=Kouba,+L), [Ashish Yashwanth Kangen](https://arxiv.org/search/cs?searchtype=author&query=Kangen,+A+Y), [Helmut Schmid](https://arxiv.org/search/cs?searchtype=author&query=Schmid,+H), [Hinrich Schutze](https://arxiv.org/search/cs?searchtype=author&query=Schutze,+H), [Michael Farber](https://arxiv.org/search/cs?searchtype=author&query=Farber,+M)

View a PDF of the paper titled LLM in the Loop: Creating the PARADEHATE Dataset for Hate Speech Detoxification, by Shuzhou Yuan and 6 other authors

[View PDF](/pdf/2506.01484)
[HTML (experimental)](https://arxiv.org/html/2506.01484v1)

> Abstract:Detoxification, the task of rewriting harmful language into non-toxic text, has become increasingly important amid the growing prevalence of toxic content online. However, high-quality parallel datasets for detoxification, especially for hate speech, remain scarce due to the cost and sensitivity of human annotation. In this paper, we propose a novel LLM-in-the-loop pipeline leveraging GPT-4o-mini for automated detoxification. We first replicate the ParaDetox pipeline by replacing human annotators with an LLM and show that the LLM performs comparably to human annotation. Building on this, we construct PARADEHATE, a large-scale parallel dataset specifically for hatespeech detoxification. We release PARADEHATE as a benchmark of over 8K hate/non-hate text pairs and evaluate a wide range of baseline methods. Experimental results show that models such as BART, fine-tuned on PARADEHATE, achieve better performance in style accuracy, content preservation, and fluency, demonstrating the effectiveness of LLM-generated detoxification text as a scalable alternative to human annotation.

|           |                                                                                               |
| --------- | --------------------------------------------------------------------------------------------- |
| Subjects: | Computation and Language (cs.CL)                                                              |
| Cite as:  | [arXiv:2506.01484](https://arxiv.org/abs/2506.01484) [cs.CL]                                  |
|           | (or [arXiv:2506.01484v1](https://arxiv.org/abs/2506.01484v1) [cs.CL] for this version)        |
|           | <https://doi.org/10.48550/arXiv.2506.01484> Focus to learn more arXiv-issued DOI via DataCite |
