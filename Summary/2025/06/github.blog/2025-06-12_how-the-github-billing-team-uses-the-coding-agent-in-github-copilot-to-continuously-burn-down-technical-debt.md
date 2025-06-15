---
title: How the GitHub billing team uses the coding agent in GitHub Copilot to continuously
  burn down technical debt
source: https://github.blog/ai-and-ml/github-copilot/how-the-github-billing-team-uses-the-coding-agent-in-github-copilot-to-continuously-burn-down-technical-debt/
author: Brittany Ellich
published: '2025-06-12T16:00:00+00:00'
fetched: '2025-06-13T04:03:17.589200+00:00'
tags:
- codex
- github
- ai
image: https://github.blog/wp-content/uploads/2024/07/maxresdefault-1.jpg?fit=1280%2C720
---

## 要約

ソフトウェアは常に進化する一方で、過去の決定や応急処置が積み重なって技術的負債が膨らむ。GitHubの課金チームはGitHub Copilotのコーディングエージェントを利用し、リファクタリングや依存関係更新などの単調な作業を自動化することで、通常の開発フローを妨げず継続的に負債を解消している。成果を最大化するには、リポジトリ用のCopilotインストラクションを整備し、小さな単位で課題を切り出し、的確なプロンプトと徹底したコードレビューを行うことが重要だ。AIエージェントと人間の役割を分担することで、より迅速な開発と安定したシステムを実現できる。エンジニアが本来注力すべき設計判断や複雑な業務ロジックは人間が担い、繰り返しの作業はAIに任せることで、長期的な再開発を避け安定的な成長が可能となる。

## 本文

One of the beautiful things about software is that it’s always evolving. However, each piece carries the weight of past decisions made when it was created. Over time, quick fixes, “temporary” workarounds, and deadline compromises compound into tech debt. Like financial debt, the longer you wait to address it, the more expensive it becomes.

It’s challenging to prioritize tech debt fixes when deadlines loom and feature requests keep streaming in. Tech debt work feels like a luxury when you’re constantly in reactive mode. Fixing what’s broken today takes precedence over preventing something from possibly breaking tomorrow. Occasionally that accumulated tech debt even results in full system rewrites, which are time-consuming and costly, just to achieve parity with existing systems.

Common approaches to managing tech debt, like gardening weeks (dedicated sprints for tech debt) and extended feature timelines, don’t work well. Gardening weeks treat tech debt as an exception rather than ongoing maintenance, often leaving larger problems unaddressed while teams postpone smaller fixes. Extended timelines create unrealistic estimates that can break trust between engineering and product teams.

The fundamental problem is treating tech debt as something that interrupts normal development flow. What if instead you could chip away at tech debt continuously, in parallel with regular work, without disrupting sprint commitments or feature delivery timelines?

## Using AI agents to routinely tackle tech debt

**Managing tech debt is a big opportunity for AI agents like the coding agent in [GitHub Copilot](https://github.com/features/copilot).**

With AI agents like the [coding agent in GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/), tech debt items no longer need to go into the backlog to die. While you’re focusing on the new features and architectural changes that you need to bring to your evolving codebase, you can assign GitHub Copilot to complete tech debt tasks at the same time.

Here are some examples of what the coding agent can do:

- **Improve code test coverage**: Have limited code testing coverage but know you’ll never get the buy-in to spend time writing more tests? Assign issues to GitHub Copilot to increase test coverage. The agent will take care of it and ping you when the tests are ready to review.
- **Swap out dependencies**: Need to swap out a mocking library for a different one, but know it will be a long process? Assign the issue to swap out the library to GitHub Copilot. It can work through that swap while you’re focusing your attention elsewhere.
- **Standardize patterns across codebases**: Are there multiple ways to return and log errors in your codebase, making it hard to investigate issues when they occur and leading to confusion during development? Assign an issue to GitHub Copilot to standardize a single way of returning and logging errors.
- **Optimize frontend loading patterns**: Is there an area where you are making more API calls than your application really needs? Ask GitHub Copilot to change the application to only make those API calls when the data is requested, instead of on every page load.
- **Identify and eliminate dead code**: Is there anywhere in your project where you may have unused functions, outdated endpoints, or stale config hanging out? Ask GitHub Copilot to look for these and suggest ways to safely remove them.

If those examples sound very specific, it’s because they are. These are all real changes that my team has tackled using GitHub Copilot coding agent—and these changes probably wouldn’t have occurred without it. **The ability for us to tackle tech debt continuously while delivering features has grown exponentially**, and working AI agents into our workflow has proven to be incredibly valuable. We’ve been able to reduce the time it takes to remove tech debt from weeks of intermittent, split focus to a few minutes of writing an issue and a few hours reviewing and iterating on a pull request.

### What’s the difference between agent mode and coding agent in GitHub Copilot?

While they’re both AI agents, they’re tuned for different parts of your day-to-day workflows. [See how to use them both](https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot/) to work more efficiently.

This isn’t about replacing human engineers; it’s about amplifying what we do best. While agents handle the repetitive, time-consuming work of refactoring legacy code, updating dependencies, and standardizing patterns across codebases, we can focus on architecture decisions, feature innovation, and solving complex business problems. The result is software that stays healthier over time, teams that ship faster, and engineers who spend their time on work that actually energizes them.

## When AI is your copilot, you still have to do the work

The more I learn about AI, the more I realize just how critical humans are in the entire process. AI agents excel at well-defined, repetitive tasks, the kind of tech debt work that’s important but tedious. But when it comes to larger architectural decisions or complex business logic changes, human judgment is still irreplaceable.

Since we are engineers, we know the careful planning and tradeoff considerations that come with our craft. One wrong semicolon, and the whole thing can come crashing down. This is why every prompt requires careful consideration and each change to your codebase requires thorough review.

Think of it as working with a brilliant partner that can write clean code all day but needs guidance on what actually matters for your application. The AI agent brings speed and consistency; it never gets tired, never cuts corners because it’s Friday afternoon, and can maintain focus across hundreds of changes. But you bring the strategic thinking: knowing which tech debt to tackle first, understanding the business impact of different approaches, and recognizing when a “quick fix” might create bigger problems down the line.

The magic happens in the interaction between human judgment and AI execution. You define the problem, set the constraints, and validate the solution. The agent handles the tedious implementation details that would otherwise consume hours of your time. This partnership lets you operate at a higher level while still maintaining quality and control.

## Tips to make the most of the coding agent in GitHub Copilot

Here’s what I’ve learned from using the coding agent in GitHub Copilot for the past few months:

1. **Write** [**Copilot Instructions**](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) **for your repository.** This results in a much better experience. You can even ask your agent to write the instructions for you to get started, which is how I did it! Include things like the scripts that you need to run during development to format and lint (looking at you, `go fmt`).
2. **Work in digestible chunks.** This isn’t necessarily because the agent needs to work in small chunks. I learned the hard way that it will make some pretty ambitious, sweeping changes if you don’t explicitly state which areas of your codebase you want changed. However, reviewing a 100+-file pull request is not my idea of a good time, so working in digestible chunks generally makes for a better experience for me as the reviewer. What this looks like for me is instead of writing an issue that says “Improve test coverage for this application”, I create multiple issues assigned to GitHub Copilot that “improve test coverage for file X” or “improve test coverage for folder Y”, to better scope the changes that I need to review.
3. **Master the art of effective prompting.** The quality of what you get from AI agents depends heavily on how well you communicate your requirements. Be specific about the context, constraints, and coding standards you want the agent to follow.
4. **Always review the code thoroughly.** While AI agents can handle repetitive tasks well, they don’t understand business logic like you do. Making code review a central part of your workflow ensures quality while still benefiting from the automation. This is one of the reasons why I love the GitHub Copilot coding agent. It uses the same code review tools that I use every day to review code from my colleagues, making it incredibly easy to fit into my workflow.

We’re at a pivotal moment in software engineering. For too long, tech debt has been the silent productivity killer. It’s the thing we all know needs attention but rarely gets prioritized until it becomes a crisis. AI coding agents are giving us the opportunity to change that equation entirely.

The engineers who learn to effectively collaborate with AI agents—the ones who master the art of clear prompting, thoughtful code review, and strategic task delegation—will have a massive advantage. They’ll be able to maintain codebases that their peers struggle with, tackle tech debt that others avoid, and potentially eliminate the need for those expensive, time-consuming rewrites that have plagued our industry for decades.

But this transformation requires intentional effort. You need to experiment with these tools, learn their strengths and limitations, and integrate them into your workflow. The technology is ready; the question is whether you’ll take advantage of it.

If you haven’t started exploring how AI agents can help with your tech debt, now is the perfect time to begin. Your future self, who is more productive, less frustrated, and focused on the creative aspects of engineering, will thank you. More importantly, so will your users, who’ll benefit from a more stable, well-maintained application that continues to evolve instead of eventually requiring significant downtime for a complete rebuild.

Assign your tech debt to [GitHub Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/enabling-copilot-coding-agent) in your repositories today!

## Written by

Brittany is a software engineer at GitHub, working in Platform and Enterprise.
