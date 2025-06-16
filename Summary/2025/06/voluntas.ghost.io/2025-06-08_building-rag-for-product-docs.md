---
title: 自社製品ドキュメント向けの RAG を作ろうとしている
source: https://voluntas.ghost.io/building-rag-for-product-docs/
author:
- voluntas.ghost.io
published: '2025-06-08T13:25:45.000Z'
fetched: '2025-06-08T17:06:21.492855Z'
tags:
- codex
- ai
image: https://static.ghost.org/v5.0.0/images/publication-cover.jpg
---

## 要約

自社製品ドキュメントにRAGを導入する方針を詳述する記事。検索にはDuckDBを用いて日本語全文検索とベクトル検索を組み合わせ、結果をLLMに渡す。LLMはPFNのPLaMoを想定し、まずはPLaMo 2 8Bを自前で運用する。Akamai CloudのGPUで月700ドル程度に抑え、停止しても問題ない方式を採る。ドキュメント取得はHTMLスクレイピングとし、無料公開を目指す。将来はPLaMo APIの従量課金も併用する計画。

## 本文

自社製品のドキュメントはウェブに公開しており、誰でも閲覧できる。さらに [Meilisearch](https://www.meilisearch.com/?ref=voluntas.ghost.io) を利用して日本語の全文検索機能も提供している。この Meilisearch は自前で運用しているため定額 (月 36 ドル) で提供できている。

ただ、やはりもう日本語全文検索だけでは物足りなくなってきている。実際 [Google NotebookLM](https://notebooklm.google/?ref=voluntas.ghost.io) 向けのシングルページを提供したりしているが、やはり RAG がほしい。

そこで RAG をパブリックかつ無料で利用できるような仕組みを提供したいと考えてる。そのため API 利用の従量課金の仕組みではなく、GPU を利用した定額の仕組みを導入を素人ながら色々調べている。

### 前提条件

- オープンかつ無料で提供する
- DuckDB ベースで実現する
- PFN PLaMo のモデルや API を利用する
- Akamai Cloud の GPU インスタンスを利用する
- 落ちても良いサービス
- HTML スクレイピングを採用する
- 予算は月 700 ドル程度に抑える

### DuckDB

まず検索部分は DuckDB をベースとして日本語全文検索 ([DuckDB-FTS](https://github.com/duckdb/duckdb-fts?ref=voluntas.ghost.io) と [Lindera](https://github.com/lindera/lindera?ref=voluntas.ghost.io) の組み合わせ) とベクトル検索 ([DuckDB-VSS](https://github.com/duckdb/duckdb-vss?ref=voluntas.ghost.io) と [PLaMo-Embedding-1B](https://huggingface.co/pfnet/plamo-embedding-1b?ref=voluntas.ghost.io) の組み合わせ)、そしてリランキング(検討中)を用いた仕組みを採用し、それを LLM に要約させて回答を返すといった仕組みを検討している。

### PLaMo

LLM は [PLaMo API](https://plamo.preferredai.jp/api?ref=voluntas.ghost.io) (PLaMo Prime) を検討したが、いったん [PLaMo 2 8B](https://huggingface.co/pfnet/plamo-2-8b?ref=voluntas.ghost.io) を時前で運用してみることにした。理由としては PLaMo 2 8B はなんと売上が 10 億円を超えなければ商用申請をするだけで利用する事ができる。もちろんいつかは 10 億円を超えて利用料を支払いたい、というかそのときは素直に PLaMo API を使おうと思う。

### Akamai Cloud

[Akamai Cloud GPU プラン](https://www.linode.com/pricing/?ref=voluntas.ghost.io#compute-gpu)でインスタンスを 1 台を借りて運用しようと考えている。自社ドキュメント用途だと RAG に障害が発生しても単純に不便になるだけなので、ここは割り切る。

### HTML スクレイピング

ドキュメントの取り込み（チャンキングなど）は基本的に Python で実際のドキュメントをクロール（スクレイピング）して取得することにした。もともと reStructuredText というマイナーな形式を使っている事や、もともと全文検索自体も HTML をクロールしてることから、スクレイピング方式を採用することにした。

### 予算

費用としては最大でも月 700 ドル程度で納めることにする。PLaMo API を使った方が安いのでは ... という気持ちもあるが、とりあえず時前と API 両方利用できるようにしようと考えている。社内で利用するときは PLaMo API を使い、オープンなのは GPU を使うでも良いと考えている。

---

RAG は利益を上げる仕組みではないため、自社でやる場合はコストが一番のボトルネックになる。ただ、今の時代もう製品ドキュメントに質問が出来ないのはかなり厳しいと考え、チャレンジしていきたい。
