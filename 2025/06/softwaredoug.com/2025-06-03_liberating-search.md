<!-- metadata -->
- **title**: Liberating search from the search engine
- **source**: https://softwaredoug.com/blog/2025/06/03/liberating-search.html
- **author**: Doug Turnbull
- **published**: 
- **fetched**: 2025-06-04T11:47:55.547776Z
- **tags**: codex
- **image**: https://softwaredoug.com//assets/media/2025/top1000.jpg

## 概要 / Summary
　この記事は Doug Turnbull によるブログ投稿で、検索エンジンの複雑なクエリDSLに頼るのではなく、エンジンからトップN件の候補だけを取得し、アプリケーション側のAPIでリランキングやブーストを行うべきだと論じている。エンジンはシンプルな取得(L0)に徹し、BM25やトークナイズ、ページングなどをクライアントライブラリで扱えば、Pythonなど馴染みのツールを用いて柔軟な検索ロジックを実装できるという主張。

### ディスカッション履歴 / Discussion
- ユーザー: DSL とは何ですか？
- アシスタント: Domain-Specific Language について説明
- ユーザー: なんの記事なのかが分からないので説明を入れて
- アシスタント: 記事の目的を追記
- ユーザー: URL を提示
- アシスタント: クリッピングを作成


## 本文 / Article
Modern search engines push waaay too much complexity into the engine. Frustrating search practitioners. Let’s stop doing that.

Let’s just get the top N from the search engine, and boost/rerank/etc in our API code. Using tools we know and love.

Elasticsearch, Vespa, Weaviate, and friends all have sophisticated under-the-hood DSLs for matching, boosting, and rescoring. They rerank with ML models, perform vector inference, tokenize text, and track global statistics about search terms.

But its OK. We can just get the top 1000 candidates from the search engine and manipulate the ranking.

![/assets/media/2025/top1000.jpg](/assets/media/2025/top1000.jpg)

For years I thought of this as a dirty hack. After all, you’d need to reimplement much of the search engine yourself: paging, aggregations, etc.

Nevertheless the upside of total control are numerous:

* Predictable / reliable search engine query load with dumber L0 queries
* Less lock-in to some search engine DSL
* Ubiquitous Python ML tooling over search-engine specific tooling when reranking
* Easier to understand implementation of business logic for boosting / filtering

Further, we can plan for this layer to fail, and have a clean fallback to the basic top 1000 or so candidates.

**We need to embrace API control of search rather than shun it. It needs to be the best practice, not the “hack”**

Yet the search community, unfortunately, doesn’t support this path. We don’t have out of the box, client-side open source tools to build search APIs that help us. Such a tool that does this would need to:

1. Stream candidates into a top N set for paging into a result set
2. Regenerate matches / scores to keyword and vector searches for boosting / reranking models
3. Track global index statistics like document frequency in the client for BM25
4. Let an ML model or business logic access this set for reranking as needed

For example, in Python-esque, wouldn’t it be great to just:

```
query = 'red shoes'

# RETRIEVAL (ie call Elasticsearch)
top_n = get_top_n(... retrieval query..., n=1000)

# BOOST
top_n_name_bm25 = bm25(top_n, 'product_name', query)  # compute BM25 of matches
top_n[top_n_name_bm25 > 0] += (10 * top_n_name_bm25)  # boost by 10 times name match

# CACHE FOR LATER PAGING
key = top_n.cache(ttl=120) # cache for paging for 120 seconds

# FETCH TOP N (also return paging key)
return key, top_n.fetch(start=0, page_size=10)  

```

If we had this, we could refocus our call to Elasticsearch, etc on simpler, predictable retrieval. Maybe if we’re a news site that means a basic embedding retrieval, but with a bias towards recency? If we’re e-commerce, maybe some basic product image + description matching with some basic prefiltering down to the category?

### Staying in a tokenized view

I original built [SearchArray](https://github.com/softwaredoug/searcharray) with this pattern in mind. But what I learned was building / maintaining an index for retrieval - ie what SearchArray does - is quite a different task than the top K manipulations you need.

What I think we actually need is a Python library that looks more like [search engine highlighting](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/highlighting) or maybe [Elasticsearch’s percolator](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-percolate-query.html)

Highlighting works by

1. Taking a pretokenized view of the documents (or tokenizing if not available)
2. Finding matches for a query
3. Scoring matches to “sell” me the documents

We can apply the same idea to streaming documents back and scoring the top N. Except, when we score them, we record those scores to allow the user to manipulate the ranking — boosting results up and down as needed, passing onto a ranking model, or whatever.

### Search engine should work with tokens, not tokenizers

Bullet (1) above hopes that we get a pretokenized view of the document from the backend to speed up the APIs boosting / reranking etc.

Indeed, we probably dont want tokenization hidden in the search engine. In lexical search, tokenization holds a lot of the domain-specific implementation. People implement legal taxonomies and fashion knowledge graphs in tokenizers. Dictionary lookups into a specific language are often needed to correctly tag documents MID tokenization.

One feature I’ve begun to see in search systems like Turbopuffer is the ability to [ship the raw tokens over to the engine](https://turbopuffer.com/docs/schema#tokenizers-for-full-text-search). Then YOU figure out how to tokenize query and documents on your side. Elasticsearch lets us [get the term vectors back](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-reindex-rethrottle), but what if we could SHIP term vectors to Elastic?

This way you rarely interact with search with the direct text (except perhaps for document hydration). You instead stay in a token space as much as possible. Keeping index / query load predictable at the engine and giving your search developers full control.

### Remembering document frequency

The first question that comes to mind with this for lexical use cases: can we keep the global state of document frequency need for BM25 / TFIDF scoring?

I’d argue we can do a decent enough job tracking this as tokenized terms come back. As we stream back our tokenized documents, we can count document frequency and update a counter somewhere (ie redis). This means when we query / score later we’ll need to lookup the handful of query terms we need to store for their document frequency. It’s also possible if the search engine gives us a tokenized response, it can include this information for us.

Sure this might be less accurate than the search engine, but the search engine itself already injects inaccuracies with sharding etc.

### Paging

We also need to rebuild paging for our top N candidates. This means maintaining a stateful cache of the L0 response for a query, and reusing that instead of hitting the L0

Redis / valkey conveniently have a few data structures for maintaining a heap. We can use [ZADD](https://valkey.io/commands/zadd/) to add a document identifier along with a key. Then [ZPOPMAX](https://valkey.io/commands/zpopmax/) to pop the top N off on each paging event. And we can expire this sorted array if the user doesn’t come back. But there’s a million other ways of maintaining a stateful heap in our search API.

In the end, I suspect such a client-side library would be able to manage this state for us as well. With a tool like Redis, or without.

### Put together

I feel we can / should be building something more like this in our search services. If we build this way, we can have reliable L0 retrieval and give our search engineers more power at the application layer to do their work.

Do libraries like this exist and I’m not seeing it? Should search engine client libraries help us here? Maybe that would be a better use than more complexity in the search engine itself?

### Enjoy softwaredoug in training course form!

![Cheat at Search with LLMs](/assets/media/2025/cheat-at-search-social.png)

I hope you join me at [Cheat at Search with LLMs](https://maven.com/softwaredoug/cheat-at-search) to learn how to apply LLMs to search applications. Check out [this post](https://github.com/softwaredoug/softwaredoug.com/edit/master/_includes/post.html) for a sneak preview.
