<!-- metadata -->
- **title**: Codex Changelog | OpenAI Help Center
- **source**: https://help.openai.com/en/articles/11428266-codex-changelog
- **author**: help.openai.com
- **published**: 2025-06-03T00:00:00Z
- **fetched**: 2025-06-04T02:05:05Z
- **tags**: codex, changelog, openai
- **image**: https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553073411/18a74d8b76049eebb1a9bb2ec5e6/image.png

## 要約

Codex の更新情報。**インターネットアクセス**を付与して依存関係をインストール可能になり、既存**PRの更新**や**音声入力**対応、環境設定の改善、iOS版**ChatGPT**への統合などが行われた。

## 本文 / Article

New features, fixes, and improvements to Codex in ChatGPT

Updated today

Table of contents

June 3, 2025
------------

Agent internet access
---------------------

[![Image 1](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553073411/18a74d8b76049eebb1a9bb2ec5e6/image.png?expires=1749081600&signature=b0cbeeed1207d5199cab9cd08dba8a37e43dafc8b53fc9eded52f8a79e45d9c2&req=dSUiFcl5noVeWPMW3nq%2BgSQ3pOda30yHh92hIQ1M07rljOQNc%2FIFnzVZC7Vm%0ACrVXhIPlHa3jt8HI%2Flk1TZKT1J0%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553073411/18a74d8b76049eebb1a9bb2ec5e6/image.png?expires=1749081600&signature=b0cbeeed1207d5199cab9cd08dba8a37e43dafc8b53fc9eded52f8a79e45d9c2&req=dSUiFcl5noVeWPMW3nq%2BgSQ3pOda30yHh92hIQ1M07rljOQNc%2FIFnzVZC7Vm%0ACrVXhIPlHa3jt8HI%2Flk1TZKT1J0%3D%0A)

Now you can give Codex access to the internet during task execution to install dependencies, upgrade packages, run tests that need external resources, and more.

Internet access is off by default. Plus, Pro, and Team users can enable it for specific environments, with granular control of which domains and HTTP methods Codex can access. Internet access for Enterprise users is coming soon.

Learn more about usage and risks in the [docs](https://platform.openai.com/docs/codex/agent-network).

Update existing PRs
-------------------

[![Image 2](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553074623/9f704e142234f8079bd3b98d4a72/image.png?expires=1749081600&signature=25d82158b5cde643ef9419be5634e3c60c52bf2abf0eb7b8ee70668dc885e2b7&req=dSUiFcl5mYddWvMW3nq%2BgXVjw7Df%2BeGMaXtbAqsaQl63vnW9noggfuWjYUNK%0AnzPqGSRb2zibaNkSudELTK1mcWY%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553074623/9f704e142234f8079bd3b98d4a72/image.png?expires=1749081600&signature=25d82158b5cde643ef9419be5634e3c60c52bf2abf0eb7b8ee70668dc885e2b7&req=dSUiFcl5mYddWvMW3nq%2BgXVjw7Df%2BeGMaXtbAqsaQl63vnW9noggfuWjYUNK%0AnzPqGSRb2zibaNkSudELTK1mcWY%3D%0A)

Now you can update existing pull requests when following up on a task.

Voice dictation
---------------

[![Image 3](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553117217/0b13e5141d7eacc829a3d9ffde27/voice-dictation.gif?expires=1749081600&signature=8fc69fc96babfa8c001917567411b5f78fd74c5e61af7d35f3d42f685b6a031f&req=dSUiFch%2FmoNeXvMW3nq%2BgfDMQtRumLuSGRbZtdoVNxWMN2Vqm%2FVWq%2F59Us%2BD%0AayuRDXt4eRNpCrmmYmkiL0mupTw%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1553117217/0b13e5141d7eacc829a3d9ffde27/voice-dictation.gif?expires=1749081600&signature=8fc69fc96babfa8c001917567411b5f78fd74c5e61af7d35f3d42f685b6a031f&req=dSUiFch%2FmoNeXvMW3nq%2BgfDMQtRumLuSGRbZtdoVNxWMN2Vqm%2FVWq%2F59Us%2BD%0AayuRDXt4eRNpCrmmYmkiL0mupTw%3D%0A)

Now you can dictate tasks to Codex.

Fixes & improvements
--------------------

May 22, 2025
------------

Reworked environment page
-------------------------

[![Image 4](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1536499162/bee5c11f5abb79372b21fb1631a0/image.png?expires=1749081600&signature=d6fbb44ca0fa5217e8116d15b2ba460c1d7aa1fd0be721ca3976a8bf91a89288&req=dSUkEM13lIBZW%2FMW3nq%2BgRxdvvFvBRXXXveioSdMBc5ixf%2B7sUiS6%2BZVnMfx%0ASZNZPgrHWCQVDHh3ct3%2Bblee2d4%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1536499162/bee5c11f5abb79372b21fb1631a0/image.png?expires=1749081600&signature=d6fbb44ca0fa5217e8116d15b2ba460c1d7aa1fd0be721ca3976a8bf91a89288&req=dSUkEM13lIBZW%2FMW3nq%2BgRxdvvFvBRXXXveioSdMBc5ixf%2B7sUiS6%2BZVnMfx%0ASZNZPgrHWCQVDHh3ct3%2Bblee2d4%3D%0A)

It’s now easier and faster to set up Code execution.

Fixes & improvements
--------------------

May 19, 2025
------------

Codex in the ChatGPT iOS app
----------------------------

[![Image 5](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1536501361/9f379dd30677230c790774c397a9/ios.png?expires=1749081600&signature=bc33e6645cb5a6ae83a2920b9d6c697f1d88712e64f420ac4e70dc22e7bd0738&req=dSUkEMx%2BnIJZWPMW3nq%2BgRd00%2F8CE0qa%2BLYbdhx6f1%2B0zp0TaV1vitllR%2B6d%0Ab25Z0IZAWCY1APn%2BYAnMn68aACk%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1536501361/9f379dd30677230c790774c397a9/ios.png?expires=1749081600&signature=bc33e6645cb5a6ae83a2920b9d6c697f1d88712e64f420ac4e70dc22e7bd0738&req=dSUkEMx%2BnIJZWPMW3nq%2BgRd00%2F8CE0qa%2BLYbdhx6f1%2B0zp0TaV1vitllR%2B6d%0Ab25Z0IZAWCY1APn%2BYAnMn68aACk%3D%0A)

Start tasks, view diffs, and push PRs—while you're away from your desk.

* * *

Related Articles

[ChatGPT Enterprise & Edu - Release Notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes)[OpenAI Codex CLI – Getting Started](https://help.openai.com/en/articles/11096431-openai-codex-cli-getting-started)[Codex in ChatGPT](https://help.openai.com/en/articles/11369540-codex-in-chatgpt)
