<!-- metadata -->

- **title**: RARE: Retrieval-Aware Robustness Evaluation for Retrieval-Augmented Generation Systems
- **source**: https://arxiv.org/abs/2506.00789
- **author**: Yixiao Zeng, Tianyu Cao, Danqing Wang, Xinran Zhao, Zimeng Qiu, Morteza Ziyadi, Tongshuang Wu, Lei Li
- **published**: 2025-06-01T00:00:00Z
- **fetched**: 2025-06-04T04:43:15Z
- **tags**: codex, rag, evaluation, robustness, retrieval
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

**RAG**システムの頑健性を評価する**RARE**フレームワークと大規模ベンチマークを提案。クエリ・文書の攪乱に強さを測定し、マルチホップ質問でより脆弱と報告。

## 本文

[Submitted on 1 Jun 2025]

# Title:RARE: Retrieval-Aware Robustness Evaluation for Retrieval-Augmented Generation Systems

Authors:[Yixiao Zeng](https://arxiv.org/search/cs?searchtype=author&query=Zeng,+Y), [Tianyu Cao](https://arxiv.org/search/cs?searchtype=author&query=Cao,+T), [Danqing Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+D), [Xinran Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+X), [Zimeng Qiu](https://arxiv.org/search/cs?searchtype=author&query=Qiu,+Z), [Morteza Ziyadi](https://arxiv.org/search/cs?searchtype=author&query=Ziyadi,+M), [Tongshuang Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+T), [Lei Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+L)

View a PDF of the paper titled RARE: Retrieval-Aware Robustness Evaluation for Retrieval-Augmented Generation Systems, by Yixiao Zeng and 7 other authors

[View PDF](/pdf/2506.00789)

> Abstract:Retrieval-Augmented Generation (RAG) enhances recency and factuality in answers. However, existing evaluations rarely test how well these systems cope with real-world noise, conflicting between internal and external retrieved contexts, or fast-changing facts. We introduce Retrieval-Aware Robustness Evaluation (RARE), a unified framework and large-scale benchmark that jointly stress-tests query and document perturbations over dynamic, time-sensitive corpora. One of the central features of RARE is a knowledge-graph-driven synthesis pipeline (RARE-Get) that automatically extracts single and multi-hop relations from the customized corpus and generates multi-level question sets without manual intervention. Leveraging this pipeline, we construct a dataset (RARE-Set) spanning 400 expert-level time-sensitive finance, economics, and policy documents and 48,322 questions whose distribution evolves as the underlying sources change. To quantify resilience, we formalize retrieval-conditioned robustness metrics (RARE-Met) that capture a model's ability to remain correct or recover when queries, documents, or real-world retrieval results are systematically altered. Our results show that RAG systems exhibit surprising vulnerability to perturbations, with document robustness consistently being the weakest point regardless of generator size or architecture. RAG systems consistently show lower robustness on multi-hop queries than single-hop queries across all domains.

|           |                                                                                               |
| --------- | --------------------------------------------------------------------------------------------- |
| Subjects: | Computation and Language (cs.CL)                                                              |
| Cite as:  | [arXiv:2506.00789](https://arxiv.org/abs/2506.00789) [cs.CL]                                  |
|           | (or [arXiv:2506.00789v1](https://arxiv.org/abs/2506.00789v1) [cs.CL] for this version)        |
|           | <https://doi.org/10.48550/arXiv.2506.00789> Focus to learn more arXiv-issued DOI via DataCite |
