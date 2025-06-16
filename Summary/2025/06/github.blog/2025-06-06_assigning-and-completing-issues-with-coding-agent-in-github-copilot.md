---
title: Assigning and completing issues with coding agent in GitHub Copilot
source: https://github.blog/ai-and-ml/github-copilot/assigning-and-completing-issues-with-coding-agent-in-github-copilot/
author:
- Alexandra Lietzke
published: '2025-06-06T16:00:00+00:00'
fetched: '2025-06-07T11:04:04Z'
tags:
- codex
- ai
- github
- automation
image: https://github.blog/wp-content/uploads/2025/04/wallpaper_copilot_generic_logo.png?fit=1920%2C1080
---

## 要約

GitHub Copilotの新しい**コーディングエージェント**は、Issueを割り当てるだけでテスト済みのPRを作成してくれる非同期のソフトウェアエージェントです。GitHub Actions上で動作し、関連IssueやPRの情報、リポジトリのカスタム指示を利用してコードを生成します。エージェントモードがIDE内でリアルタイムに協調するのに対し、コーディングエージェントはIssueを受け取ってバックグラウンドで作業を進めます。Issueには背景や期待する結果、技術的詳細、フォーマット規則などを明確に記載することが成功の鍵です。エージェントは作業計画、コード生成、テスト実行、PR作成、レビュー依頼まで行い、最終承認は人間が行います。小規模タスクから始めて、問題があればコメントで指示するなどの工夫が推奨されます。AIとLLMは急速に進化しており、コーディングエージェントは既に実用的です。まずはサンプルリポジトリで試し、独自のワークフロー構築に活用してみましょう。

## 本文

You’ve used GitHub Copilot to help you write code in your IDE. Now, imagine assigning Copilot an issue, just like you would a teammate—and getting a fully tested pull request in return.

That’s the power of the new [coding agent in GitHub Copilot](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/). Built directly into GitHub, this agent starts working as soon as you assign it a GitHub Issue or prompt it in VS Code. Keeping you firmly in the pilot’s seat, the coding agent builds pull requests based on the issues you assign it.

This isn’t just autocomplete. It’s a new class of software engineering agents that work asynchronously to help you move faster, clean up tech debt, and focus on the work that really matters. Let’s explore how this coding agent works and how it can help you find new ways of working faster. ✨

Oh, and if you’re a visual learner we have you covered. 👇

[![video](https://github.blog/wp-content/uploads/2025/06/Screenshot-2025-06-05-at-11.22.28%E2%80%AFAM.png)](https://github.blog/wp-content/uploads/2025/06/Copilot-Coding-Agent-Overview-v3-Burned.mp4)

## Coding agent in GitHub Copilot 101

This new coding agent, which is our first asynchronous software engineering agent, is built on GitHub Actions and works like a teammate. You assign it an issue, let it do the work, and then review its outputs before changing or accepting them. It also incorporates context from related issues or PR discussions and can follow custom repository instructions that your team has already set.

You assign Copilot an issue and it plans the work, opens a pull request, writes the code, runs the tests, and then asks for your review. If you leave feedback, it’ll revise the PR and keep going until you approve.

The process isn’t instant—it takes a little time to compute and run. But it’s already helping developers work faster and more efficiently.

## What’s the difference between the coding agent and agent mode?

**Agent mode is a synchronous collaborator that pairs with you as you work**: It works inside your IDE of choice, whether VS Code or JetBrains, Eclipse, and Xcode, as a real-time collaborator that iterates on code, runs tests, and fixes its own mistakes in real time.

**Coding agent is an asynchronous collaborator and works on your behalf like a teammate**: It is an SWE agent that runs inside GitHub Actions, picks up issues you assign, explores the repo for context, writes code, passes tests, and opens a pull request for your review.

**BTW**: Both use [Copilot premium requests](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests), and coding agent uses [GitHub Actions minutes](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions), so plan and budget accordingly with your teams.

According to Brittany Ellich, Senior Software Engineer at GitHub, traditional advice for devs has been to do one thing at a time, and do it well. But with the new coding agent, GitHub can now help you do **more** things well, like:

- Offloading repetitive, boilerplate tasks like adding and extending unit tests
- Maintaining better issue hygiene and documentation with quick typo fixes and small refactors
- Improving user experience by fixing bugs, updating user interface features, and bolstering accessibility

By assigning these low- to medium-complexity tasks to the coding agent, you may finally have the bandwidth to focus on higher-level problem solving and design, tackle that tech debt that’s been piling up, learn new skills, and more.

Even though Copilot is doing the work, you’re in control the entire time: You decide what to assign, what to approve, and what should be changed.

## Need help building issues? Copilot’s at the ready.

Copilot can also build issues with the preview of Copilot’s Create Issue flow. This new feature enables you to build multiple issues quickly by drawing on the full context of your prompt and project.

[Learn more >](https://github.blog/developer-skills/github/how-to-create-issues-and-pull-requests-in-record-time-on-github/)

### How to get the coding agent to complete an issue

#### Step one: Write and assign the issue to Copilot

This is where you’ll be most involved—and this step is crucial for success. Think of writing the issue like briefing a team member: The more context you give, the better the results (like any other [prompt](https://github.blog/ai-and-ml/github-copilot/github-for-beginners-how-to-get-llms-to-do-what-you-want/#what-is-prompt-engineering)).

Make sure to include:

- **Relevant background info**: Why this task matters, what it touches, and any important history or context.
- **Expected outcome**: What “done” looks like.
- **Technical details**: File names, functions, or components involved.
- **Formatting or linting rules**: These are especially important if you use custom scripts or auto-generated files. You can add these [instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) for Copilot so it’s automatically reflected in every issue.

Once you’ve written the issue, it’s time to assign it to Copilot—just like you would a teammate. You can do this via [github.com](http://github.com/), the GitHub Mobile app, or through the GitHub CLI.

Copilot works best with well-scoped tasks, but it can handle larger ones. It just might take a little bit longer. You don’t have to assign only one issue; you can batch-assign multiple issues, which is great for tasks like increasing test coverage or updating documentation.

Here are a few tips and tricks that we’ve found helpful:

- You can use [issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) with fields like “description” and “acceptance criteria” to make writing issues easier and more consistent across your team.
- If your repo includes custom instructions (such as which files are auto-generated or how to run formatters), Copilot will use these to improve its output.
- The agent can actually see images included in its assigned issues on GitHub, so you can easily share images of what you want your new feature to look like, and the agent can run with it.

#### Step two: Copilot plans the code

Once you assign Copilot an issue, it will add an 👀 emoji reaction. Then it will kick off an agent session using GitHub Actions, which powers the [integrated, secure, and fully customizable](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot) environment the coding agent is built on.

This environment is where Copilot can explore and analyze your codebase, run tests, and make changes. The coding agent will simultaneously open both a branch and a pull request, which will evolve as Copilot works.

Copilot will read your issue and break it down into a checklist of tasks, then update the pull request with this checklist. As it completes each task, Copilot checks it off and pushes commits to the branch. You can watch the session live, view the session logs later, or refresh the PR to see how Copilot is reasoning through the task. These are updated regularly for increased visibility, so you can easily spot problems if they arise.

#### Step three: Copilot writes the code

This is where the magic happens. Once you see the “Copilot started work” event in the pull request timeline, you’ll know the wheels are turning. Here’s what happens next:

- Copilot modifies your codebase based on the issue.
- It runs automated tests and linters if they’re present in your repo and updates or generates tests as needed.
- Copilot will also push commits iteratively as it completes tasks.

You can see the work happening in real time, and if you notice that something looks off, you can step in at any point to make sure things are going in the right direction before Copilot passes it back to you.

#### Step four: Review and merge the pull request

This is another stage where you’ll need to be involved. Once Copilot finishes the work, it will tag you for review. You can either:

- Approve the pull request
- Leave comments
- Ask for changes

Copilot will automatically request reviewers based on the rules you’ve set in your repo. And if needed, you can go through multiple review cycles until you get your desired outcome—just like with a human teammate.

Once the pull request is approved:

- The change can now follow your repo’s merge and deploy process.
- The agent session will end.
- If needed, a human can take over from the branch at any time.

🚨One important thing to note: The person who created the issue can’t be the final approver. You’ll need a peer, manager, or designated reviewer to give the green light. This promotes collaboration and ensures unreviewed or unsafe code doesn’t get merged.

**And you’re done!** ✅

Like any other tool (or teammate), Copilot’s coding agent might need a little prodding to deliver exactly the output you want. Remember, the biggest factor to success starts with how you write the issue ([Copilot can also help you write those faster](https://github.blog/changelog/2025-05-19-creating-issues-with-copilot-on-github-com-is-in-public-preview/)).

Here are a few tips on how to get the most out of Copilot:

- **Write comprehensive issues**: Clear, scoped, and well-documented issues lead to better results.
- **Start small**: Try using the agent for tests, docs, or simple refactors.
- **Troubleshooting**: If Copilot gets stuck, tag it in a comment and add more context. Iterating and refining the issue requirements can also help.

## Take this with you

AI and LLMs are improving at a rapid pace. “The models we’re using today are the worst ones we’ll ever use—because they’re only getting better,” says Ellich. And coding agents are already proving useful in real workflows.

Try using the coding agent on a sample repo. See what it can do. And start building your own agentic workflows. Happy coding!

[**Visit the Docs**](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/about-assigning-tasks-to-copilot) to get started with the coding agent in GitHub Copilot.
