<!-- metadata -->

- **title**: OpenAI slams court order to save all ChatGPT logs, including deleted chats
- **source**: https://simonwillison.net/2025/Jun/5/openai-court-order/
- **author**: Simon Willison
- **published**: 2025-06-05T14:20:06Z
- **fetched**: 2025-06-05T19:00:44Z
- **tags**: codex, ai-ethics, generative-ai, openai, new-york-times, ai, law, llms
- **image**:

## 要約

**OpenAI** が **ChatGPT** のログをすべて保存するよう求められた裁判所命令に強く反発。削除済みも含めたログ保管は多数の **プライバシー法** に抵触すると主張するが、判事は証拠保全の必要性を優先するとして命令を出した。これにより OpenAI の API 利用者が他社に移る可能性も懸念されている。

## 本文

**[OpenAI slams court order to save all ChatGPT logs, including deleted chats](https://arstechnica.com/tech-policy/2025/06/openai-says-court-forcing-it-to-save-all-chatgpt-logs-is-a-privacy-nightmare/)** ([via](https://news.ycombinator.com/item?id=44185913 "Hacker News")) This is very worrying. The New York Times v OpenAI lawsuit, now in its 17th month, includes accusations that OpenAI's models can output verbatim copies of New York Times content - both from training data and from implementations of RAG.

(This may help explain why Anthropic's Claude [system prompts for their search tool](https://simonwillison.net/2025/May/25/claude-4-system-prompt/#seriously-don-t-regurgitate-copyrighted-content) emphatically demand Claude not spit out more than a short sentence of RAG-fetched search content.)

A few weeks ago the judge ordered OpenAI to start preserving the logs of _all_ potentially relevant output - including supposedly [temporary private chats](https://help.openai.com/en/articles/8914046-temporary-chat-faq) and API outputs served to paying customers, which previously had a 30 day retention policy.

The May 13th court order itself is [only two pages](https://cdn.arstechnica.net/wp-content/uploads/2025/06/NYT-v-OpenAI-Preservation-Order-5-13-25.pdf) - here's the key paragraph:

> Accordingly, OpenAI is **NOW DIRECTED to preserve and segregate all output log data that would otherwise be deleted on a going forward basis until further order of the Court** (in essence, the output log data that OpenAI has been destroying), whether such data might be deleted at a user’s request or because of “numerous privacy laws and regulations” that might require OpenAI to do so.
>
> **SO ORDERED.**

That "numerous privacy laws and regulations" line refers to OpenAI's argument that this order runs counter to a whole host of existing worldwide privacy legislation. The judge here is stating that the potential need for future discovery in this case outweighs OpenAI's need to comply with those laws.

Unsurprisingly, I have seen plenty of bad faith arguments online about this along the lines of
"Yeah, but that's what OpenAI really wanted to happen" - the fact that OpenAI are fighting this order runs counter to the common belief that they aggressively train models on all incoming user data no matter what promises they have made to those users.

I still see this as a massive competitive disadvantage for OpenAI, particularly when it comes to API usage. Paying customers of their APIs may well make the decision to switch to other providers who can offer retention policies that aren't subverted by this court order!
