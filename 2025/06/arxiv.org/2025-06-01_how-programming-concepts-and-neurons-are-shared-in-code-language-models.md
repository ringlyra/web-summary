<!-- metadata -->

- **title**: How Programming Concepts and Neurons Are Shared in Code Language Models
- **source**: https://arxiv.org/abs/2506.01074
- **author**: Amir Hossein Kargaran, Yihong Liu, François Yvon, Hinrich Schütze
- **published**: 2025-06-01T00:00:00Z
- **fetched**: 2025-06-04T04:42:50Z
- **tags**: codex, llm, programming languages, code analysis, neurons
- **image**: https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

複数PLと英語の概念空間の共有を調査。中間層の埋め込み解析で英語キーワードが優勢となり、各PL専用ニューロンは上層に分布するなど構造的傾向を示した。

## 本文 / Article

[Submitted on 1 Jun 2025]

# Title:How Programming Concepts and Neurons Are Shared in Code Language Models

Authors:[Amir Hossein Kargaran](https://arxiv.org/search/cs?searchtype=author&query=Kargaran,+A+H), [Yihong Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Y), [François Yvon](https://arxiv.org/search/cs?searchtype=author&query=Yvon,+F), [Hinrich Schütze](https://arxiv.org/search/cs?searchtype=author&query=Sch%C3%BCtze,+H)

View a PDF of the paper titled How Programming Concepts and Neurons Are Shared in Code Language Models, by Amir Hossein Kargaran and 3 other authors

[View PDF](https://arxiv.org/pdf/2506.01074)
[HTML (experimental)](https://arxiv.org/html/2506.01074v1)

> Abstract:Several studies have explored the mechanisms of large language models (LLMs) in coding tasks, but most have focused on programming languages (PLs) in a monolingual setting. In this paper, we investigate the relationship between multiple PLs and English in the concept space of LLMs. We perform a few-shot translation task on 21 PL pairs using two Llama-based models. By decoding the embeddings of intermediate layers during this task, we observe that the concept space is closer to English (including PL keywords) and assigns high probabilities to English tokens in the second half of the intermediate layers. We analyze neuron activations for 11 PLs and English, finding that while language-specific neurons are primarily concentrated in the bottom layers, those exclusive to each PL tend to appear in the top layers. For PLs that are highly aligned with multiple other PLs, identifying language-specific neurons is not feasible. These PLs also tend to have a larger keyword set than other PLs and are closer to the model's concept space regardless of the input/output PL in the translation task. Our findings provide insights into how LLMs internally represent PLs, revealing structural patterns in the model's concept space. Code is available at [this https URL](https://github.com/cisnlp/code-specific-neurons).

|           |                                                                                               |
| --------- | --------------------------------------------------------------------------------------------- |
| Comments: | ACL Findings 2025                                                                             |
| Subjects: | Computation and Language (cs.CL); Programming Languages (cs.PL); Software Engineering (cs.SE) |
| Cite as:  | [arXiv:2506.01074](https://arxiv.org/abs/2506.01074) [cs.CL]                                  |
|           | (or [arXiv:2506.01074v1](https://arxiv.org/abs/2506.01074v1) [cs.CL] for this version)        |
|           | <https://doi.org/10.48550/arXiv.2506.01074> Focus to learn more arXiv-issued DOI via DataCite |
