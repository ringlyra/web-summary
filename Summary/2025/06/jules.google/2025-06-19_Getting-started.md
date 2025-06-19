---
title: 'Getting started'
source: https://jules.google/docs/
author:
  - jules.google
published: ''
fetched: '2025-06-19T07:56:55.397947+00:00'
tags:
  - codex
  - jules
  - getting-started
  - documentation
  - ai-coding-agent
  - github
  - setup
  - tutorial
image:
---

## 要約

Julesは、バグ修正、ドキュメント追加、新機能構築を支援する実験的な**コーディングエージェント**です。**GitHub**と連携し、コードベースを理解して**非同期**に動作するため、タスクを任せて他の作業を進められます。このガイドでは、Julesのセットアップから最初のタスク実行までを説明します。主な手順は、Googleアカウントでのサインイン、GitHubリポジトリへの接続、リポジトリとブランチの選択、明確なプロンプトの記述、そして「**Give me a plan**」のクリックです。Julesがプランを生成後、レビューと承認を経てコード変更が実行されます。作業中はブラウザ通知で進捗確認が可能です。

## 本文

Jules is an experimental coding agent that helps you fix bugs, add documentation, and build new features. It integrates with GitHub, understands your codebase, and works **asynchronously** â so you can move on while it handles the task.

This guide will walk you through setting up Jules and running your first task.

1. Visit [jules.google.com](https://jules.google.com)
2. Sign in with your Google account.
3. Accept the privacy notice (oneâtime).

Jules needs access to your repositories in order to work.

1. Click **Connect toÂ GitHubÂ account.**
2. Complete the login flow.
3. Choose *all* or specific repos that you want to connect to Jules.
4. You will be redirected back to Jules. If not, try refreshing the page.

Once connected, youâll see a **repo selector** where you can select the repo you want Jules to work with, and a prompt input box.

Jules runs in a virtual machine where it clones your code, installs dependencies, and modifies files.

1. Pick a repository from the repo selector.
2. Choose the branch you want Jules to work on. The default branch will be selected already. You do not have to modify this unless you want Jules to work on a specific branch.
3. Write a clear, specific prompt. For example, `Add a test for "parseQueryString` function in utils.js
4. (Optional) Add environment setup scripts.
5. Click **Give me a plan**

Once you submit a task, Jules will generate a plan. You can review and approve it before any code changes are made.

![Screenshot of prompt](https://jules.google/docs/_astro/starting_a_task1.B_FC3NW0_Nxkrg.webp)

You are free to leave Jules while it is running. To stay informed:

1. When prompted, enable browser notifications.
2. Go to **Settings â> notifications** at any time to enable or disable notifications.

Youâll be notified when the task completes or needs your input.

![Notifications](https://jules.google/docs/_astro/notifications.C0W_9Pe7_dT6e0.webp)

Want to dive into real-world use cases? Check out the [Jules Awesome Prompts repo](https://github.com/google-labs-code/jules-awesome-list).