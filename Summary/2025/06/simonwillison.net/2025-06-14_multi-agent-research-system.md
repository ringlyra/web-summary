<!-- metadata -->
- **title**: Anthropic: How we built our multi-agent research system
- **source**: https://simonwillison.net/2025/Jun/14/multi-agent-research-system/
- **author**: Simon Willison
- **published**: 2025-06-14T00:00:00+00:00
- **fetched**: 2025-06-14T23:38:55.183295+00:00
- **tags**: codex, multi-agent, llm
- **image**: 

## 要約

Anthropicが開発したマルチエージェント型リサーチシステム『Claude Research』の仕組みを解説した記事。ユーザーからの問いをリードエージェントが解析して複数のサブエージェントに分割し、並列に情報収集させることで効率的かつ広範な検索を実現する。初期段階ではエージェントが大量のトークンを消費したり過度にサブエージェントを生成したりする問題があったが、プロンプト設計やツールテストによって改善された。評価にはLLMによる判定と人手のチェックを組み合わせ、信頼性を高めている。特に最大20万トークンの制限を回避し大量情報を扱う点や、OODAループを採用した継続的な最適化がポイント。多くの教訓が盛り込まれており実践的な参考になる。

## 本文

**[Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)**. OK, I'm sold on multi-agent LLM systems now.

I've been pretty skeptical of these until recently: why make your life more complicated by running multiple different prompts in parallel when you can usually get something useful done with a single, carefully-crafted prompt against a frontier model?

This detailed description from Anthropic about how they engineered their "Claude Research" tool has cured me of that skepticism.

[Reverse engineering Claude Code](https://simonwillison.net/2025/Jun/2/claude-trace/) had already shown me a mechanism where certain coding research tasks were passed off to a "sub-agent" using a tool call. This new article describes a more sophisticated approach.

They start strong by proving a clear definition of how they'll be using the term "agent" - it's the "tools in a loop" variant:

> A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together. Our Research feature involves an agent that plans a research process based on user queries, and then uses tools to create parallel agents that search for information simultaneously.

Why use multiple agents for a research system?

> The essence of search is compression: distilling insights from a vast corpus. Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent. [...]
>
> Our internal evaluations show that multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously. We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval. For example, when asked to identify all the board members of the companies in the Information Technology S&P 500, the multi-agent system found the correct answers by decomposing this into tasks for subagents, while the single agent system failed to find the answer with slow, sequential searches.

As anyone who has spent time with Claude Code will already have noticed, the downside of this architecture is that it can burn *a lot* more tokens:

> There is a downside: in practice, these architectures burn through tokens fast. In our data, agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats. For economic viability, multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance. [...]
>
> We’ve found that multi-agent systems excel at valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools.

The key benefit is all about managing that 200,000 token context limit. Each sub-task has its own separate context, allowing much larger volumes of content to be processed as part of the research task.

Providing a "memory" mechanism is important as well:

> The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan.

The rest of the article provides a detailed description of the prompt engineering process needed to build a truly effective system:

> Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates. Since each agent is steered by a prompt, prompt engineering was our primary lever for improving these behaviors. [...]
>
> In our system, the lead agent decomposes queries into subtasks and describes them to subagents. Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries.

They got good results from having special agents help optimize those crucial tool descriptions:

> We even created a tool-testing agent—when given a flawed MCP tool, it attempts to use the tool and then rewrites the tool description to avoid failures. By testing the tool dozens of times, this agent found key nuances and bugs. This process for improving tool ergonomics resulted in a 40% decrease in task completion time for future agents using the new description, because they were able to avoid most mistakes.

Sub-agents can run in parallel which provides significant performance boosts:

> For speed, we introduced two kinds of parallelization: (1) the lead agent spins up 3-5 subagents in parallel rather than serially; (2) the subagents use 3+ tools in parallel. These changes cut research time by up to 90% for complex queries, allowing Research to do more work in minutes instead of hours while covering more information than other systems.

There's also an extensive section about their approach to evals - they found that LLM-as-a-judge worked well for them, but human evaluation was essential as well:

> We often hear that AI developer teams delay creating evals because they believe that only large evals with hundreds of test cases are useful. However, it’s best to start with small-scale testing right away with a few examples, rather than delaying until you can build more thorough evals. [...]
>
> In our case, human testers noticed that our early agents consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources like academic PDFs or personal blogs. Adding source quality heuristics to our prompts helped resolve this issue.

There's so much useful, actionable advice in this piece. I haven't seen anything else about multi-agent system design that's anywhere near this practical.

They even added [some example prompts](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents/prompts) from their Research system to their open source prompting cookbook. Here's [the bit](https://github.com/anthropics/anthropic-cookbook/blob/46f21f95981e3633d7b1eac235351de4842cf9f0/patterns/agents/prompts/research_lead_agent.md?plain=1#L135-L137) that encourages parallel tool use:

> `<use_parallel_tool_calls> For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially. Call tools in parallel to run subagents at the same time. You MUST use parallel tool calls for creating multiple subagents (typically running 3 subagents at the same time) at the start of the research, unless it is a straightforward query. For all other queries, do any necessary quick initial planning or investigation yourself, then run multiple subagents in parallel. Leave any extensive tool calls to the subagents; instead, focus on running subagents in parallel efficiently. </use_parallel_tool_calls>`

And an interesting description of [the OODA research loop](https://github.com/anthropics/anthropic-cookbook/blob/46f21f95981e3633d7b1eac235351de4842cf9f0/patterns/agents/prompts/research_subagent.md?plain=1#L10) used by the sub-agents:

> `Research loop: Execute an excellent OODA (observe, orient, decide, act) loop by (a) observing what information has been gathered so far, what still needs to be gathered to accomplish the task, and what tools are available currently; (b) orienting toward what tools and queries would be best to gather the needed information and updating beliefs based on what has been learned so far; (c) making an informed, well-reasoned decision to use a specific tool in a certain way; (d) acting to use this tool. Repeat this loop in an efficient way to research well and learn based on new results.`
