<!-- metadata -->

- **title**: Changelog
- **source**: https://jules.google/docs/changelog
- **author**: jules.google
- **published**:
- **fetched**: 2025-06-08T17:31:25.876866Z
- **tags**: codex
- **image**:

## 要約

JulesのChangelogでは、2025年5月19日のローンチ以降の更新内容が時系列でまとめられている。6月6日の更新では、パフォーマンスの改善、コードを直接コピー・ダウンロードできるボタンの追加、複数タスクを開始できるモーダル、コードパネル幅の調整機能が追加された。
5月30日はGitHub同期の信頼性向上と利用制限の更新により失敗ケースを3分の1まで削減。5月22日はキューシステムの刷新やUI改善、モバイル関連のバグ修正で更なる安定化を図った。5月19日の初公開では、GitHubリポジトリ上でタスクを自動実行しテストやPR作成まで行う **AI coding agent Jules** の概要と能力が説明されている。

## 本文

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

- Updated our limits to 60 tasks per day, 5 concurrent.
- We substantially improved the reliability of the GitHub sync. Export to GitHub should also be fixed on previously created tasks.
- Weâve decreased the number of failure cases by 2/3

Learn more [about usage limits.](./../usage-limits)

**May 22, 2025**

Weâve been heads down improving stability and fixing bugsâbig and smallâto make Jules faster, smoother, and more reliable for you.

**Hereâs whatâs fixed:**

- Upgraded our queuing system and added more compute to reduce wait times during peak usage
- Publish Branch button is now part of the summary UI in the activity feed so itâs easier to find
- Bug vixes for task status and mobile

[Learn more](https://jules.google/docs/code/#pushing-to-github) about how to publish a branch on GitHub.

**May 19, 2025**

![Jules dashboard](https://jules.google/docs/_astro/jules-changelog-og-image.CksfgUSk_1wDNHc.webp)

Today, weâre launching [**Jules,**](https://jules.google.com) a new AI coding agent.

Jules helps you move faster by working asynchronously on tasks in your GitHub repo. It can fix bugs, update dependencies, migrate code, and add new features.

Once you give Jules a task, it spins up a fresh dev environment in a VM, installs dependencies, writes tests, makes the changes, runs the tests, and opens a pull request. Jules shows its work as it makes progress, so you never have to guess what code itâs writing, or what itâs thinking.

**What Jules can do today**

- Fix bugs with test verified patches
- Handle version bumps and dependency upgrades
- Perform scoped code transformations
- Migrate code across languages or frameworks
- Ship isolated, scoped, features
- Open PRs with runnable code and test results

[Get started with the Jules documentation](/), and visit [jules.google.com](https://jules.google.com) to run your first Jules task.
