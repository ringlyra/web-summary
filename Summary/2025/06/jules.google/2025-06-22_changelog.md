---
title: 'Changelog'
source: https://jules.google/docs/changelog/#jules-agent-update-faster-smarter-more-reliable
author:
  - jules.google
published: ''
fetched: '2025-06-22T08:30:43.636104+00:00'
tags:
  - codex
  - jules
image: 
---

## 要約

2025年6月20日公開の最新アップデートでは、Julesエージェントの内部が刷新され、AGENTS.mdを自動で読み取ってリポジトリごとの設定を理解する機能が導入されました。処理ループが短縮されてパント回数が大幅に減り、体感速度が確実に向上しています。さらに、セットアップスクリプトが常に実行されるよう改良されたため環境構築で失敗することが少なくなり、タスクが途中で止まるケースも激減しました。テスト作成と実行の習慣づけも強化され、自律的にテストを走らせる割合が高まったことで、修正内容の信頼性と再現性が大きく向上しています。数値はまだ公表されていませんが、総合的により迅速で頼れる作業が可能になったと言えるでしょう。

## 本文

**June 20, 2025**

![Jules environment updates](https://jules.google/docs/_astro/agents-md-support.COimRein_13z6cT.webp)

Weâve shipped a big upgrade to the Jules agent under the hood.

Whatâs new:

* **Smarter context.** Jules reads from AGENTS.md if itâs in your repo.
* **Improved performance.** Tasks now complete fasterâno numbers to share just yet, but youâll feel it.
* **Significantly reduced punting.** We tightened the loop to keep Jules moving forward.
* **More reliable setup.** If youâve added an environment setup script, Jules now runs it consistently.
* **Better test habits.** Jules is more likely to write and run tests on its own.

Check out the [Getting Started](https://jules.google/docs/) guide to learn more about AGENTS.md support.

**June 18, 2025**

![Jules environment updates](https://jules.google/docs/_astro/changelog-env-update.C-4Kcp7e_Z1a9xXQ.webp)

Weâve overhauled the Jules development environment to move beyond the default Ubuntu 24.04 LTS packages. This includes:

* Explicitly installing newer versions of key toolchains like Rust, Node, and Python, addressing long-standing version issues.
* Adding finer-grained control over installation steps via custom scripts instead of relying solely on apt.
* Introducing support for multiple runtimes, improved isolation, and version pinning to reduce drift and better match developer expectations.

These changes unblock several issues developers encountered with outdated dependencies and improve alignment with modern project requirements.

[Read about the Jules environment setup to learn more about whatâs pre-installed.](https://jules.google/docs/environment/)

**June 6, 2025**

![Jules code view](https://jules.google/docs/_astro/jules-copy-paste-download.Bh0k6Pa9_ZL8pAP.webp)

**Performance upgrades:** Enjoy a smoother, faster Jules experience with recent under-the-hood improvements.

**Quickly copy and download code:** New copy and download buttons are now available in the code view pane, making it easier to grab your code directly from Jules.

**Stay focused with task modals:** Initiate multiple tasks seamlessly through a new modal option, allowing you to keep your context and workflow intact. [Learn more](https://jules.google/docs/tasks-repos/) about kicking off tasks.

**Adjustable code panel:** Customize your workspace by adjusting the width of the code panel to your preferred viewing experience.

[Check out the docs](https://jules.google/docs/code/) to learn more about how to download code that Jules writes.

**May 30, 2025**

This week, our focus has been on improving reliability, fixing our GitHub integration, and scaling capacity.

**Hereâs whatâs we shipped:**

* Updated our limits to 60 tasks per day, 5 concurrent.
* We substantially improved the reliability of the GitHub sync. Export to GitHub should also be fixed on previously created tasks.
* Weâve decreased the number of failure cases by 2/3

Learn more [about usage limits.](./../usage-limits)

**May 22, 2025**

Weâve been heads down improving stability and fixing bugsâbig and smallâto make Jules faster, smoother, and more reliable for you.

**Hereâs whatâs fixed:**

* Upgraded our queuing system and added more compute to reduce wait times during peak usage
* Publish Branch button is now part of the summary UI in the activity feed so itâs easier to find
* Bug vixes for task status and mobile

[Learn more](https://jules.google/docs/code/#pushing-to-github) about how to publish a branch on GitHub.

**May 19, 2025**

![Jules dashboard](https://jules.google/docs/_astro/jules-changelog-og-image.CksfgUSk_1wDNHc.webp)

Today, weâre launching [**Jules,**](https://jules.google.com) a new AI coding agent.

Jules helps you move faster by working asynchronously on tasks in your GitHub repo. It can fix bugs, update dependencies, migrate code, and add new features.

Once you give Jules a task, it spins up a fresh dev environment in a VM, installs dependencies, writes tests, makes the changes, runs the tests, and opens a pull request. Jules shows its work as it makes progress, so you never have to guess what code itâs writing, or what itâs thinking.

**What Jules can do today**

* Fix bugs with test verified patches
* Handle version bumps and dependency upgrades
* Perform scoped code transformations
* Migrate code across languages or frameworks
* Ship isolated, scoped, features
* Open PRs with runnable code and test results

[Get started with the Jules documentation](https://jules.google/), and visit [jules.google.com](https://jules.google.com) to run your first Jules task.
