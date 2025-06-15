---
title: Using Projects in ChatGPT | OpenAI Help Center
source: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt
author: help.openai.com
published: ''
fetched: '2025-06-13T00:10:22.006442+00:00'
tags:
- codex
- ChatGPT
- workspace
- productivity
- project-management
image: ''
---

## 要約

プロジェクト機能は長期的なタスクを効率化するChatGPTのワークスペースで、チャット履歴や参照ファイル、カスタム指示をひとまとめにして管理できる。サイドバーのNew projectから目的別に作成し、既存チャットをドラッグするだけで移動可能。PDFや表計算シート、画像など20件までアップロードでき、削除すると復元できない。TeamやEnterprise契約では管理者設定やコンプライアンスAPIが適用され、メモリを有効にするとプロジェクト内の過去会話を参照して回答の精度を高められる。料金は通常利用と同じで追加費用はなく、プランに応じたレート制限があり、不要になったプロジェクトは削除すれば全てのデータが完全に消去される。

## 本文

## Overview

Projects are smart workspaces that keep everything related to a long‑running effort in one place. Group together chats, upload reference files, and add custom instructions so ChatGPT remembers what matters and stays on‑topic. With memory, context, and flexible tools, they’re ideal for repeated and evolving work such as writing, research, planning, and more.

## What’s new (June 2025)

## Getting started

## Creating a project

Click **New project** in the sidebar and give it a clear, goal‑oriented name like _“Wedding Planning”_ or _“Mobile‑App Redesign.”_

## Add context or files

Upload PDFs, spreadsheets, or images in **Files**, and add **project instructions** to guide tone or role (e.g., “Act like my marketing mentor”). Instructions set in your project will not interact with any chats outside of your project, and will supersede custom instructions set in your ChatGPT account. [Learn more about Custom Instructions on ChatGPT](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions-faq).

## Moving existing chats into a project

From the chat list in the left sidebar, drag any chat onto your desired project, or onto **New project** to create a new project. You can also click on the chat’s menu and select **Move to project or Create New Project**.

Once you move the chat into the project, the chat can now continue in the context of the project. This means that any Custom Instructions and files in your project will impact responses from ChatGPT for that chat.

You can remove a chat from your project by clicking on the chat’s menu and selecting **Remove,**or by dragging it out of the project.

## Chat, research, iterate

Use your favorite ChatGPT tools right inside of a project:

## Deleting projects

You can delete your project by selecting the dots next to your project name and selecting Delete project. This will delete your files, chats, and custom instructions in the project. Once they are deleted, they cannot be recovered.

## Plans & limits

Users can create unlimited projects, each supporting up to 20 files, subject to rate limits.

## Admin controls, data, and compliance API

## Workspace-level feature controls

Projects inherit all toggles and restrictions that apply to your Team, Enterprise, or Edu workspace:

## Compliance API

The current Compliance API endpoints and behavior for chats in projects remain unchanged. For details, see the[Compliance API reference](https://chatgpt.com/admin/api-reference#tag/Projects).

## Data Retention & Residency

All messages created in a project inherit the retention duration and residency region configured for your workspace. No separate retention policy is required, and deleted projects purge their chats, files, and custom instructions within 30 days.

## FAQ

## Does using projects change how my data is handled?

For ChatGPT Team, Enterprise, and Edu customers, we do not use information accessed from projects to train our modes. Please see our [Enterprise Privacy page](https://openai.com/enterprise-privacy/) for information on how we use business data.

For ChatGPT Free, Plus, and Pro users, we may use information accessed from projects to train our models if your “Improve the model for everyone” setting is on. You can read more about how your data is stored and used in this article in our help center: [Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq)

## How does memory work in projects?

In addition to saved memories, ChatGPT can reference previous chats within a project to deliver more relevant, focused responses. When you ask a question in a project, ChatGPT prioritizes the project chats and files.

If memory for your account is enabled, it remains active across all interactions.

## Do projects cost extra?

No, access to projects is included with every qualifying ChatGPT plan. Any credits or usage charges—such as those for models or tools—apply to project chats the same as they do to regular chats.

## What happens if I hit my file limit?

Remove older or unnecessary uploads, combine file data, or split work into multiple projects.

## Are connectors supported in projects?

Connectors are currently not supported.

## How can I search for a chat I had within a project?

Use the [search chats](https://help.openai.com/en/articles/10056348-how-do-i-search-my-chat-history-in-chatgpt) feature to locate past chats within a project. It lets you quickly find and revisit discussions you've had in that project, and others.

## Are there any rate limits for chats within projects?

Rate limits are based on your subscription level.

---

Related Articles

[ChatGPT Capabilities Overview](https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview)[ChatGPT Team - Release Notes](https://help.openai.com/en/articles/11391654-chatgpt-team-release-notes)[ChatGPT Record](https://help.openai.com/en/articles/11487532-chatgpt-record)[Connectors in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)[Admin Controls, Security, and Compliance in Connectors (Enterprise, Edu, and Team)](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-connectors-enterprise-edu-and-team)
