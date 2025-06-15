---
title: ChatGPT — Release Notes | OpenAI Help Center
source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
author: openai.com
published: '2022-12-15T00:00:00Z'
fetched: '2025-06-08T17:03:52Z'
tags:
- codex
- chatgpt
- release-notes
- updates
- openai
image: ''
---

## 要約

OpenAIが提供するChatGPTの更新履歴をまとめたページ。2025年6月7日の更新では、音声モードの抑揚や自然さが向上し、翻訳機能も追加された。6月4日にはDeep Research向けコネクタがベータ公開され、MCPによるカスタムコネクタも利用可能に。6月3日には無料ユーザーでもメモリ機能が強化された。さらに5月にはDropboxやGitHub連携、GPT‑4.1の提供開始、Sharepoint/OneDriveコネクタ、PDF出力など多数の機能改善が続き、記事末尾には2022年12月からの初期アップデートも含まれている。

## 本文

## June 7, 2025

## Updates to Advanced Voice Mode for paid users

We're upgrading Advanced Voice in ChatGPT for paid users with significant enhancements in intonation and naturalness, making interactions feel more fluid and human-like. When we first launched Advanced Voice, it represented a leap forward in AI speech—now, it speaks even more naturally, with subtler intonation, realistic cadence (including pauses and emphases), and more on-point expressiveness for certain emotions including empathy, sarcasm, and more.

Voice also now offers intuitive and effective language translation. Just ask Voice to translate between languages, and it will continue translating throughout your conversation until you tell it to stop or switch. It’s ready to translate whenever you need it—whether you're asking for directions in Italy or chatting with a colleague from the Tokyo office. For example, at a restaurant in Brazil, Voice can translate your English sentences into Portuguese, and the waiter’s Portuguese responses back into English—making conversations effortless, no matter where you are or who you're speaking with.

This upgrade to Advanced Voice is available for all paid users across markets and platforms—just tap the Voice icon in the message composer to get started.

This update is in addition to improvements we made earlier this year to ensure fewer interruptions and improved accents.

**Known Limitations**

In testing, we've observed that this update may occasionally cause minor decreases in audio quality, including unexpected variations in tone and pitch. These issues are more noticeable with certain voice options. We expect to improve audio consistency over time.

Additionally, rare hallucinations in Voice Mode persist with this update, resulting in unintended sounds resembling ads, gibberish, or background music. We are actively investigating these issues and working toward a solution.

## June 4, 2025

## Connectors in beta for deep research (Plus, Pro, Team, Enterprise, Edu)

ChatGPT Team, Enterprise, and Edu customers globally can use connectors in deep research, as well as Pro and Plus users (excluding users in Switzerland, EEA, and the UK) to generate long-form, cited responses that include your company’s internal tools.

## Custom connectors via Model Context Protocol (Pro, Team, Enterprise, Edu)

Admins and users can now build and deploy custom connectors to proprietary systems using Model Context Protocol (MCP).

Learn more about [building custom connectors with MCP](http://platform.openai.com/docs/mcp). For Team, Enterprise, and Edu plans, only admins can build and deploy custom connectors.

## June 3, 2025

## Memory is now more comprehensive for Free users

Memory improvements are starting to roll out to Free users. In addition to the saved memories that were there before, ChatGPT now references your recent conversations to deliver responses that feel more relevant and tailored to you.

Free users must be logged in and on up-to-date apps (iOS/Android v1.2025.147+).

**Opt‑in reminders**

You can turn off memory anytime in settings. Learn more in our [Memory FAQ](https://help.openai.com/en/articles/8590148).

## May 15, 2025

## Dropbox connector for deep research for Plus/Pro/Team

ChatGPT deep research with Dropbox is available globally to Team users. It is also gradually rolling out to Plus and Pro users, except for those in the EEA, Switzerland, and the UK. Enterprise user access will be announced at a later date.

## GitHub connector for deep research

The GitHub connector is now available globally to Plus/Pro/Team users, including those in the EEA, Switzerland, and the UK.

## May 14, 2025

## Releasing GPT-4.1 in ChatGPT for all paid users

Since its launch in the API in April, GPT-4.1 has become a favorite among developers—by popular demand, we’re making it available directly in ChatGPT.

GPT-4.1 is a specialized model that excels at coding tasks. Compared to GPT-4o, it's even stronger at precise instruction following and web development tasks, and offers an alternative to OpenAI o3 and OpenAI o4-mini for simpler, everyday coding needs.

Starting today, Plus, Pro, and Team users can access GPT-4.1 via the "more models" dropdown in the model picker. Enterprise and Edu users will get access in the coming weeks. GPT-4.1 has the same rate limits as GPT-4o for paid users.

## Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users

GPT-4.1 mini is a fast, capable, and efficient small model, delivering significant improvements compared to GPT-4o mini—in instruction-following, coding, and overall intelligence. Starting today, GPT-4.1 mini replaces GPT-4o mini in the model picker under "more models" for paid users, and will serve as the fallback model for free users once they reach their GPT-4o usage limits. Rate limits remain the same.

Evals for GPT-4.1 and GPT-4.1 mini were originally shared in the [blog post](https://openai.com/index/gpt-4-1/) accompanying their API release. They also went through standard safety evaluations. Detailed results are available in the newly launched [Safety Evaluations Hub](https://openai.com/safety/evaluations-hub/).

## May 12, 2025

## Microsoft Sharepoint and OneDrive connector for deep research for Plus/Pro/Team

ChatGPT deep research with Sharepoint and OneDrive is available globally to Team users. It is also gradually rolling out to Plus and Pro users, except for those in the EEA, Switzerland, and the UK. Enterprise user access will be announced at a later date.

## Export Deep Research as PDF for Plus/Pro/Team

You can now export your deep research reports as well-formatted PDFs—complete with tables, images, linked citations, and sources.

To use, click the share icon and select 'Download as PDF.' It works for both new and past reports.

## May 8, 2025

## GitHub connector for deep research for Plus/Pro/Team

ChatGPT deep research with GitHub is available globally to Team users. It is also gradually rolling out to Plus and Pro users, except for those in the EEA, Switzerland, and the UK. Enterprise user access will be announced at a later date.

## Enhanced Memory in ChatGPT (including EU) on Plus/Pro

Enhanced memory rolling out to all Plus and Pro users (including the EU). The new memory features are available in the EEA (EU + UK), Switzerland, Norway, Iceland, or Liechtenstein. These features are **OFF by default** and must be enabled in **Settings > Personalization > Reference Chat History**.

### Plan differences

• **Saved memories** and **Chat history** are offered only to Plus and Pro accounts.

• Free‑tier users have access to **Saved memories** only.

### Opt‑in reminders

• Outside the European regions listed above, all Plus and Pro accounts that have memory enabled will receive the upgrade automatically.

• If you previously opted out of memory, ChatGPT will not reference past conversations unless you opt back in.

## May 6, 2025

## Mobile UI (iOS/Android) changing on Free/Plus/Pro plans

We've removed the row of individual tool icons from the mobile composer and replaces it with the new sliders‑style icon to open the **Skills** menu; tapping that button opens a bottom‑sheet menu where users can choose tools like Create an image or Search the web.

[![Image 1](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1511581077/6da087e7b74a6ec288aafa38878e/image+%281%29.png?expires=1749403800&signature=ebe84c71dc83d21cd1f2f08143f8144d6c496c70bf2e2d2fe3cea0fac1e59371&req=dSUmF8x2nIFYXvMW1HO4zVfoSYrYayy3TE7fFx0LM4FxNOIBJanS2gQ7%2BFHO%0AcDQEIjC4Z0tNWvhOyQc%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1511581077/6da087e7b74a6ec288aafa38878e/image+%281%29.png?expires=1749403800&signature=ebe84c71dc83d21cd1f2f08143f8144d6c496c70bf2e2d2fe3cea0fac1e59371&req=dSUmF8x2nIFYXvMW1HO4zVfoSYrYayy3TE7fFx0LM4FxNOIBJanS2gQ7%2BFHO%0AcDQEIjC4Z0tNWvhOyQc%3D%0A)

No tools are deprecated—access is simply consolidated to clear space and reduce on‑screen clutter.

## May 1, 2025

## Sunsetting Monday GPT

Launched on April 1 as a one-month surprise, our “Monday” personality (available in both voice and text) has now been sunset. We hope you enjoyed Monday's irreverent style, and we’re already working on new personalities for future use. Please stay tuned for what’s next!

## April 29, 2025

## Updates to GPT-4o

We've reverted the most recent update to GPT-4o due to issues with overly agreeable responses (sycophancy).

We’re actively working on further improvements. For more details, check out our [blog post](https://openai.com/index/sycophancy-in-gpt-4o/) explaining what happened and our initial findings, and [this blog post](https://openai.com/index/expanding-on-sycophancy/) where we expand on what we missed with sycophancy and the changes we're going to make going forward.

## April 25, 2025

## Improvements to GPT-4o

We’re making additional improvements to GPT-4o, optimizing when it saves memories and enhancing problem-solving capabilities for STEM. We’ve also made subtle changes to the way it responds, making it more proactive and better at guiding conversations toward productive outcomes. We think these updates help GPT-4o feel more intuitive and effective across a variety of tasks–we hope you agree!

## April 16, 2025

## **o3 and o4-mini in ChatGPT**

Today, we’re releasing OpenAI **o3** and **o4-mini,** the latest in our o-series of models trained to think for longer before responding. These are the smartest models we’ve released to date, representing a step change in ChatGPT's capabilities for everyone from curious users to advanced researchers. For the first time, our reasoning models can agentically use and combine every tool within ChatGPT—this includes searching the web, analyzing uploaded files and other data with Python, reasoning deeply about visual inputs, and even generating images. Critically, these models are trained to reason about when and how to use tools to produce detailed and thoughtful answers in the right output formats, typically in under a minute, to solve more complex problems. This allows them to tackle multi-faceted questions more effectively, a step toward a more agentic ChatGPT that can independently execute tasks on your behalf. The combined power of state-of-the-art reasoning with full tool access translates into significantly stronger performance across academic benchmarks and real-world tasks, setting a new standard in both intelligence and usefulness.

## Memory with Search

ChatGPT can also use memories to inform search queries when ChatGPT searches the web using third-party search providers. [Learn more about search](https://help.openai.com/en/articles/9237897-chatgpt-search).

## April 15, 2025

## ChatGPT Image Library

All images you create with ChatGPT are now automatically saved to a new [Library](https://help.openai.com/en/articles/11084440-chatgpt-image-library) in the sidebar, giving you one place to browse, revisit, and reuse your work without digging through past conversations. The Library is rolling out today on Web, iOS, and Android for Free, Plus, and Pro users (Enterprise / Edu support coming soon). For now, it displays images generated with 4o Image Generation while we backfill older creations, and you can remove an image by deleting the conversation where it was made.

## April 10, 2025

### **Sunsetting GPT‑4 in ChatGPT**

**_Effective April 30, 2025, GPT‑4 will be retired from ChatGPT and fully replaced by GPT‑4o._**

GPT‑4o is our newer, natively multimodal model. In head‑to‑head evaluations it consistently surpasses GPT‑4 in writing, coding, STEM, and more.

Recent upgrades have further improved GPT‑4o’s instruction following, problem solving, and conversational flow, making it a natural successor to GPT‑4.

GPT-4 will still be available in the API.

GPT‑4 marked a pivotal moment in ChatGPT’s evolution. We’re grateful for the breakthroughs it enabled and for the feedback that helped shape its successor. GPT‑4o builds on that foundation to deliver even greater capability, consistency, and creativity.

## March 27, 2025

We’ve made improvements to GPT-4o—it now feels more intuitive, creative, and collaborative, with enhanced instruction-following, smarter coding capabilities, and a clearer communication style.

#### **Smarter problem-solving in STEM and coding:**

GPT-4o has further improved its capability to tackle complex technical and coding problems. It now generates cleaner, simpler frontend code, more accurately thinks through existing code to identify necessary changes, and consistently produces coding outputs that successfully compile and run, streamlining your coding workflows.

#### **Enhanced instruction-following and formatting accuracy:**

GPT-4o is now more adept at following detailed instructions, especially for prompts containing multiple or complex requests. It improves on generating outputs according to the format requested and achieves higher accuracy in classification tasks.

#### **“Fuzzy” improvements:**

Early testers say that the model seems to better understand the implied intent behind their prompts, especially when it comes to creative and collaborative tasks. It’s also slightly more concise and clear, using fewer markdown hierarchies and emojis for responses that are easier to read, less cluttered, and more focused. We're curious to see if our users also find this to be the case.

This model is now available in ChatGPT and in the API as the newest snapshot of chatgpt-4o-latest. We plan to bring these improvements to a dated model in the API in the coming weeks.

## March 18, 2025

We have been working on a variety of usability and performance improvements and bug fixes across Web, Android, and iOS. Below are a small number of specific callouts. For updates on the ChatGPT macOS app, please see this page.

## **Web and the Windows desktop app**

1. In-line message error retries: If you encounter a message error, you can retry or just continue chatting in the same conversation.

[![Image 2](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233970/a04cd8fc47df3015db5c63496196/AD_4nXdzDpE-gfBWvrTQ87epy-HFIBZldhIjPOvtbEoWmbMHDfT0CBojbDIc3uHIDouK1G5QLc17tafodtwwjozI9OyK56OY9YCh6FPmR3MzaayL19FbP34OlZnSM_4zv0bU0Qw2GQhZOA?expires=1749403800&signature=3d2147778c4abf50b997490c970a5ab03b2369b1f702cef43097934500ccfc5f&req=dSQlH8t9nohYWfMW1HO4zY9T6vB9KGwr%2FuX8z%2FQeJiOYXoqbxWsTGV0uqMVM%0Abo3EPD4NrP0jGHmFAaE%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233970/a04cd8fc47df3015db5c63496196/AD_4nXdzDpE-gfBWvrTQ87epy-HFIBZldhIjPOvtbEoWmbMHDfT0CBojbDIc3uHIDouK1G5QLc17tafodtwwjozI9OyK56OY9YCh6FPmR3MzaayL19FbP34OlZnSM_4zv0bU0Qw2GQhZOA?expires=1749403800&signature=3d2147778c4abf50b997490c970a5ab03b2369b1f702cef43097934500ccfc5f&req=dSQlH8t9nohYWfMW1HO4zY9T6vB9KGwr%2FuX8z%2FQeJiOYXoqbxWsTGV0uqMVM%0Abo3EPD4NrP0jGHmFAaE%3D%0A)

2. o1 and o3-mini now offer Python-powered data analysis in ChatGPT: You can now ask these models to perform tasks like running regressions on test data, visualizing complex business metrics, and conducting scenario-based simulations.

3. Conversation Drafts: Unsubmitted messages in your message prompt will now be saved.

[![Image 3](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429253588/de31e119dccffcce38386fec91d6/convo+drafts.gif?expires=1749403800&signature=d401180b9cd88c04988aab8e4cc144a63a90103c99a1243d4d02b33efb10fd03&req=dSQlH8t7noRXUfMW1HO4zU3ZX1G9Ry2HNKxPMCfWH0ePHONSyVLRBAvPVEPT%0AJpHCHgM0GuJj%2BLCuYwo%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429253588/de31e119dccffcce38386fec91d6/convo+drafts.gif?expires=1749403800&signature=d401180b9cd88c04988aab8e4cc144a63a90103c99a1243d4d02b33efb10fd03&req=dSQlH8t7noRXUfMW1HO4zU3ZX1G9Ry2HNKxPMCfWH0ePHONSyVLRBAvPVEPT%0AJpHCHgM0GuJj%2BLCuYwo%3D%0A)

4. New UI for Temporary Chats: We’ve made accessing and viewing these private conversations more clear.

[![Image 4](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233971/ecd21f8cfbb230ecfc43e2b4bb56/AD_4nXcagUHzhFAJ77sucpXjut4iqJGpQQgnecvFpczN2Z8pb7e8jj3iMRRAQ3VDBtO9whmiwlI7SrycQgB05V0YsGI8Uz6TEHE25VoE6j1-T3Oy16p2dwZU1FFlNGOu7kq5WiqfyWzD?expires=1749403800&signature=00d10dbc1f63971dc25dbe86afc23f472933204aa4fba25e56271d57f930801d&req=dSQlH8t9nohYWPMW1HO4zeGpHVMWaL9VCk9AOBy6vmDE3ucmtCa%2FsF5oA72W%0A3JOYYdv5JmLQ7f5BibY%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233971/ecd21f8cfbb230ecfc43e2b4bb56/AD_4nXcagUHzhFAJ77sucpXjut4iqJGpQQgnecvFpczN2Z8pb7e8jj3iMRRAQ3VDBtO9whmiwlI7SrycQgB05V0YsGI8Uz6TEHE25VoE6j1-T3Oy16p2dwZU1FFlNGOu7kq5WiqfyWzD?expires=1749403800&signature=00d10dbc1f63971dc25dbe86afc23f472933204aa4fba25e56271d57f930801d&req=dSQlH8t9nohYWPMW1HO4zeGpHVMWaL9VCk9AOBy6vmDE3ucmtCa%2FsF5oA72W%0A3JOYYdv5JmLQ7f5BibY%3D%0A)

## **Android App**

1. Increased the default size for in‐line generated images.

[![Image 5](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429277282/78566540bc8b7148c7a66e7fc776/AD_4nXdMb6umeD6hhe5C8CLCWVjjuovVrK2CvIc_pgDMOV14KWP2piNgaXSUPmO3EZ1Kh1V2vreRtSt77uH2Vw6pKsm18Ikw_1Loz53akTT7w6ObJ2F2xrpRRk9C1ls98EbLdeGjBzlAew?expires=1749403800&signature=fb553899b798bca14fcab1276072bcd2bbf44c119b692b6232e211fcbd90cb2b&req=dSQlH8t5moNXW%2FMW1HO4zdXoB9EjM0vGUpkyAVfz67RLM%2F6xbmHlb8HVSIY9%0A%2BOEmlkojca5v6L3HcAc%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429277282/78566540bc8b7148c7a66e7fc776/AD_4nXdMb6umeD6hhe5C8CLCWVjjuovVrK2CvIc_pgDMOV14KWP2piNgaXSUPmO3EZ1Kh1V2vreRtSt77uH2Vw6pKsm18Ikw_1Loz53akTT7w6ObJ2F2xrpRRk9C1ls98EbLdeGjBzlAew?expires=1749403800&signature=fb553899b798bca14fcab1276072bcd2bbf44c119b692b6232e211fcbd90cb2b&req=dSQlH8t5moNXW%2FMW1HO4zdXoB9EjM0vGUpkyAVfz67RLM%2F6xbmHlb8HVSIY9%0A%2BOEmlkojca5v6L3HcAc%3D%0A)

2. More clear and private Incognito keyboard for Temporary Chats.

[![Image 6](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233978/7f9a3933c5c079ef9fddeb2c5432/AD_4nXccArn8klVtK-yRYmHTRf2SAIxhtBeF7HOrqJJRYEPjSzY6_oKWXcKyOu_Mzm1hKgr3QemFA4irLzkqokWC6dYD4xNK8xBncOXBHbeuUfHDvb4c4SImBliYLuf2Glns62H3KnT67g?expires=1749403800&signature=d66d355480cd9f3a9d3d6af1cc05b156b35983734b4d2e931238d56910fd3f09&req=dSQlH8t9nohYUfMW1HO4zQHGXUJagxtWjSDXLvVH3rebck6Yk5C01lMLQoyG%0A2VvTH9a56TT%2FQF8TWu4%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233978/7f9a3933c5c079ef9fddeb2c5432/AD_4nXccArn8klVtK-yRYmHTRf2SAIxhtBeF7HOrqJJRYEPjSzY6_oKWXcKyOu_Mzm1hKgr3QemFA4irLzkqokWC6dYD4xNK8xBncOXBHbeuUfHDvb4c4SImBliYLuf2Glns62H3KnT67g?expires=1749403800&signature=d66d355480cd9f3a9d3d6af1cc05b156b35983734b4d2e931238d56910fd3f09&req=dSQlH8t9nohYUfMW1HO4zQHGXUJagxtWjSDXLvVH3rebck6Yk5C01lMLQoyG%0A2VvTH9a56TT%2FQF8TWu4%3D%0A)

## **iOS App**

1. Improved table-copying functionality out of ChatGPT responses on iOS and macOS.

[![Image 7](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233972/f0dcda442223ca57bb2005f9d436/AD_4nXdKLHEesAx8oF4R4LNwsIgftAV0zc_d72fTxfw_jms5REbzzBa7Qau2In4B2PDlbNl6L4S30pf_Y-7EdoElm6i3KmIeMrwhf03vZZ3L3l0YkgWQhwKVv13qtZyo8sQ5f4P6i9T9BQ?expires=1749403800&signature=1d252c82d4c2035d2f5b7921a693aba7819354107250c5040255db85e8410051&req=dSQlH8t9nohYW%2FMW1HO4zVq2%2FkEmVzp5kOePILzv6CXZEhDLAze6FyzvSVSS%0A6fY3GzIx7%2BDPX5pfZ4A%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233972/f0dcda442223ca57bb2005f9d436/AD_4nXdKLHEesAx8oF4R4LNwsIgftAV0zc_d72fTxfw_jms5REbzzBa7Qau2In4B2PDlbNl6L4S30pf_Y-7EdoElm6i3KmIeMrwhf03vZZ3L3l0YkgWQhwKVv13qtZyo8sQ5f4P6i9T9BQ?expires=1749403800&signature=1d252c82d4c2035d2f5b7921a693aba7819354107250c5040255db85e8410051&req=dSQlH8t9nohYW%2FMW1HO4zVq2%2FkEmVzp5kOePILzv6CXZEhDLAze6FyzvSVSS%0A6fY3GzIx7%2BDPX5pfZ4A%3D%0A)

2. Added long press on your message to open menu actions: Copy, Edit.

[![Image 8](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233974/a16a802f82f79f1b88bdf9869329/AD_4nXeVpORC8zTP-D3ctiYCgHwyW3cINg2DuLzYdAEt3VOK0VKvBAWJQ1lhpz0ThkfcgLNtmQjg1rdQ3LQspcFnrbeAYgZgHN2dTGoj3c7AtHvHLPyTcWkO4JEcJyTPADw1wz7d4HPflQ?expires=1749403800&signature=3739d234ea0422d02f3ef3df54ea825380c653de9fb2e6366456999900f04b1e&req=dSQlH8t9nohYXfMW1HO4zR2oPkq%2Fz1zwSJ0j7C6wAfUEiqfYcpIavWGB9Ajw%0AZ%2BHXKe8rUPxFAMeYli4%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233974/a16a802f82f79f1b88bdf9869329/AD_4nXeVpORC8zTP-D3ctiYCgHwyW3cINg2DuLzYdAEt3VOK0VKvBAWJQ1lhpz0ThkfcgLNtmQjg1rdQ3LQspcFnrbeAYgZgHN2dTGoj3c7AtHvHLPyTcWkO4JEcJyTPADw1wz7d4HPflQ?expires=1749403800&signature=3739d234ea0422d02f3ef3df54ea825380c653de9fb2e6366456999900f04b1e&req=dSQlH8t9nohYXfMW1HO4zR2oPkq%2Fz1zwSJ0j7C6wAfUEiqfYcpIavWGB9Ajw%0AZ%2BHXKe8rUPxFAMeYli4%3D%0A)

3. Improved response display of nested blockquote content.

[![Image 9](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233975/dfa1072589558106377b4cdda68a/AD_4nXdx0xvUMu7k2329Y9KWsEzX-7r6dYFy7XuZFHETFnGWCLWWhPdFrDFzuALMTQwLjAmxpJuFUmSRYkTuG01qn-iJcV5MggMPqwuZs647yXrq4ey6t3xtxf8Ejv_dCB0YYXzrhDiJhA?expires=1749403800&signature=1df679083ab322e8aedf7c97e7455ac9e1a4e2b323df5c5c3a1d6e4d63a497eb&req=dSQlH8t9nohYXPMW1HO4zcZdstgaZDJzLSaIilvVXN2aFVXclA1poVfInuTr%0ADT6aLdISDag8j%2By0uRQ%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233975/dfa1072589558106377b4cdda68a/AD_4nXdx0xvUMu7k2329Y9KWsEzX-7r6dYFy7XuZFHETFnGWCLWWhPdFrDFzuALMTQwLjAmxpJuFUmSRYkTuG01qn-iJcV5MggMPqwuZs647yXrq4ey6t3xtxf8Ejv_dCB0YYXzrhDiJhA?expires=1749403800&signature=1df679083ab322e8aedf7c97e7455ac9e1a4e2b323df5c5c3a1d6e4d63a497eb&req=dSQlH8t9nohYXPMW1HO4zcZdstgaZDJzLSaIilvVXN2aFVXclA1poVfInuTr%0ADT6aLdISDag8j%2By0uRQ%3D%0A)

4. Improved display and faster streaming of conversations and message menu actions.

[![Image 10](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233973/db1e50a4ebe4a7045c48c41e271d/AD_4nXd0p_mRlTA_FnrPiIV0jH_tzHwCId0GfaySOwJW1KcIPxdMybi8lQNl-QvFbfJE2zn0_tzugcvyqArLXeeuxgz05Yrid11hkGVzsRJF-aD4UQkfjjqriR_jgSMhuoX_LTx6rqTN?expires=1749403800&signature=262843d6e8c55fd372a0c6bd56eff87cad9dba91563685fa2bfe88a94551ff65&req=dSQlH8t9nohYWvMW1HO4zQ1vmHeWfSwP3r%2FGvdE5tniUI9hBUmkwsmUYCG8U%0AINmxrY5j7W1szi4iQGE%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1429233973/db1e50a4ebe4a7045c48c41e271d/AD_4nXd0p_mRlTA_FnrPiIV0jH_tzHwCId0GfaySOwJW1KcIPxdMybi8lQNl-QvFbfJE2zn0_tzugcvyqArLXeeuxgz05Yrid11hkGVzsRJF-aD4UQkfjjqriR_jgSMhuoX_LTx6rqTN?expires=1749403800&signature=262843d6e8c55fd372a0c6bd56eff87cad9dba91563685fa2bfe88a94551ff65&req=dSQlH8t9nohYWvMW1HO4zQ1vmHeWfSwP3r%2FGvdE5tniUI9hBUmkwsmUYCG8U%0AINmxrY5j7W1szi4iQGE%3D%0A)

## February 28, 2025

## February 21, 2025

1. iOS widget (see below):

[![Image 11](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1396847443/8f6e6f9964f88b92834d19ffd903/Screenshot+2025-02-25+at+4_24_03%E2%80%AFPM.png?expires=1749403800&signature=3e8a98e39afcf6878a1b1477d5a13cffe311a83c3a6e0a13711f35425fd3b8f3&req=dSMuEMF6moVbWvMW1HO4zQbOCIkfEKU0XtBQ0FMV%2F%2FlsdUOSyMNMiij4T8hB%0A5DzmpMDDTKiPByE2lVM%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1396847443/8f6e6f9964f88b92834d19ffd903/Screenshot+2025-02-25+at+4_24_03%E2%80%AFPM.png?expires=1749403800&signature=3e8a98e39afcf6878a1b1477d5a13cffe311a83c3a6e0a13711f35425fd3b8f3&req=dSMuEMF6moVbWvMW1HO4zQbOCIkfEKU0XtBQ0FMV%2F%2FlsdUOSyMNMiij4T8hB%0A5DzmpMDDTKiPByE2lVM%3D%0A)

2. Text selection improvements: you can now select text across horizontal rulers.3. Performance improvements: Improved model header loading behavior. Conversation history and GPTs show up faster.4. Bug fix for logged-out users: 401s when dismissing tooltips 401s logging out users on Android.

## February 14, 2025

[![Image 12](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1415538447/3b008fa78352bb419d072e749e83/image.png?expires=1749403800&signature=31a2b9a9f61e9822f59a1741036f630f14b792354a30d7408da61885355cf998&req=dSQmE8x9lYVbXvMW1HO4zaA2esnQ7sIspvzbFP%2Fcpbdz6UHxjvu6sV8FhbkB%0A889iZCE67izUQ9EK0Eg%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1415538447/3b008fa78352bb419d072e749e83/image.png?expires=1749403800&signature=31a2b9a9f61e9822f59a1741036f630f14b792354a30d7408da61885355cf998&req=dSQmE8x9lYVbXvMW1HO4zaA2esnQ7sIspvzbFP%2Fcpbdz6UHxjvu6sV8FhbkB%0A889iZCE67izUQ9EK0Eg%3D%0A)

## Canvas sharing (February 6, 2025)

Users can now share a Canvas asset such as rendered React/HTML code, document, or code with another user, similar to how you share a conversation. You can do this from the Canvas toolbar when Canvas is open.

[![Image 13](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1367554251/e0221f8de4f9a80d5ca81219dbeb/canvas-sharing-short.gif?expires=1749403800&signature=cd0f52701efda746455b083ee05a8fe26b6bdd5c9cfce7317dc3861490cab0e9&req=dSMhEcx7mYNaWPMW1HO4zegReujvqgSphZ01xZD%2FCYQ0x%2FD2zbjQitRwfhCo%0ANyjOClV5mN6CFeFvtP8%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1367554251/e0221f8de4f9a80d5ca81219dbeb/canvas-sharing-short.gif?expires=1749403800&signature=cd0f52701efda746455b083ee05a8fe26b6bdd5c9cfce7317dc3861490cab0e9&req=dSMhEcx7mYNaWPMW1HO4zegReujvqgSphZ01xZD%2FCYQ0x%2FD2zbjQitRwfhCo%0ANyjOClV5mN6CFeFvtP8%3D%0A)

For more details about the canvas feature in ChatGPT, check out the following Help Center article!

## More personalization in Custom Instructions (January 17, 2025)

We've updated custom instructions to make it easier to customize how ChatGPT responds to you. With the new UI, you can tell ChatGPT the traits you want it to have, how you want it to talk to you, and any rules you want it to follow.

If you're already using custom instructions, this won't change your current settings.

[![Image 14](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1340441907/e2bfc91a8f8e6e12c38e836f32c1/Custom%2BInstructions%2BUI.png?expires=1749403800&signature=881a2704bca28e678a55b2b3297322508bf09ccbb66e92e80449e86f0c10d43d&req=dSMjFs16nIhfXvMW1HO4zRJ5OxzCB9IkAcXYrffNwAFlnCyIxA1Nt2E8ieDW%0A9Iq6gaAuPpX9GLL517A%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1340441907/e2bfc91a8f8e6e12c38e836f32c1/Custom%2BInstructions%2BUI.png?expires=1749403800&signature=881a2704bca28e678a55b2b3297322508bf09ccbb66e92e80449e86f0c10d43d&req=dSMjFs16nIhfXvMW1HO4zRJ5OxzCB9IkAcXYrffNwAFlnCyIxA1Nt2E8ieDW%0A9Iq6gaAuPpX9GLL517A%3D%0A)

## **January 15, 2025**

## Import from Chat into Canvas

## January 14, 2025

## Scheduled tasks in ChatGPT

Today we’re rolling out a beta version of tasks—a new way to ask ChatGPT to do things for you at a future time. Whether it's one-time reminders or recurring actions, tell ChatGPT what you need and when, and it will automatically take care of it.

Scheduled tasks is in early beta for Plus, Pro, and Teams. Eventually this will be available to anyone with a ChatGPT account.

For details see Scheduled tasks in ChatGPT.

## **December 13, 2024**

## **Projects in ChatGPT**

Projects provide a new way to group files and chats for personal use, simplifying the management of work that involves multiple chats. You can set custom instructions and upload files in your Projects, and any conversations in your Project share context with your uploaded files and custom instructions. Chats in Projects use GPT-4o and support the following features:

## **Dec 12, 2024**

## **Santa Voice and Video and Screen Share in Voice Chats**

Today we started rolling out two updates to voice mode in ChatGPT:

The first time you chat with Santa, your advanced voice limit will reset one time. So, if you’ve already used up your advanced voice limit for the day or the month (based on your subscription plan), you can still chat with Santa for the first time using advanced voice.

[![Image 15](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1295176752/b912b67c65885f1a9b2560b8e5f7/AD_4nXc6Yrl0VAWKWtH0GECNN-FtImdMfgdYXUyrpLVWkA0wLQOlZZ1BnPAF_YhopSPdRZ7B6LwpvwgfoTUBzZXVl5_-L5WpBAYec6oVE4-0-XJ_PPUkx24m3LpAgUAyh3bFIHMzkpRkPA?expires=1749403800&signature=8c3bc1da3830530671c202476567c455baaeab1374a00047e56ac37680cbd31c&req=dSIuE8h5m4ZaW%2FMW1HO4zbPYfXkJB9V2e3ygLyNbSlGg4zlh%2B4npg1I0N9J5%0Aa8sqRj81sfoo9GbXmZg%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1295176752/b912b67c65885f1a9b2560b8e5f7/AD_4nXc6Yrl0VAWKWtH0GECNN-FtImdMfgdYXUyrpLVWkA0wLQOlZZ1BnPAF_YhopSPdRZ7B6LwpvwgfoTUBzZXVl5_-L5WpBAYec6oVE4-0-XJ_PPUkx24m3LpAgUAyh3bFIHMzkpRkPA?expires=1749403800&signature=8c3bc1da3830530671c202476567c455baaeab1374a00047e56ac37680cbd31c&req=dSIuE8h5m4ZaW%2FMW1HO4zbPYfXkJB9V2e3ygLyNbSlGg4zlh%2B4npg1I0N9J5%0Aa8sqRj81sfoo9GbXmZg%3D%0A)

Use the controls at the bottom of the screen, like the camera button below, to get started. You can find screen share and image upload controls under the “...” menu at the bottom of the screen.

[![Image 16](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1295176749/e2bc0e185f8b0b9d2923dfbbeac7/AD_4nXd1o16dhWtMte7xA2AYZXivAghKAI-r-E0Fc60Lb2g6ftbsr9iIzOjshVrXQcTw5aJtZjWlqd1N3KZ91AvJraYi5TlSSX7xRN5ZXN4uN788H28C9TMPlJ4-sjMCDoFRCbxrnJab?expires=1749403800&signature=944a70cdaa177cb73a2c63d4c9f7c54a434495b7d74222973d7847b20717ecbf&req=dSIuE8h5m4ZbUPMW1HO4zWKBL59N7RsB8SfN8m2lMT8wEUO8%2FApGhPNAAMVy%0AnHlFBdsYFbFic2SexrY%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1295176749/e2bc0e185f8b0b9d2923dfbbeac7/AD_4nXd1o16dhWtMte7xA2AYZXivAghKAI-r-E0Fc60Lb2g6ftbsr9iIzOjshVrXQcTw5aJtZjWlqd1N3KZ91AvJraYi5TlSSX7xRN5ZXN4uN788H28C9TMPlJ4-sjMCDoFRCbxrnJab?expires=1749403800&signature=944a70cdaa177cb73a2c63d4c9f7c54a434495b7d74222973d7847b20717ecbf&req=dSIuE8h5m4ZbUPMW1HO4zWKBL59N7RsB8SfN8m2lMT8wEUO8%2FApGhPNAAMVy%0AnHlFBdsYFbFic2SexrY%3D%0A)

## **Dec 10, 2024**

## **Canvas**

Today we made Canvas available in 4o by default for all users, Free and Paid. Additionally, we launched a number of new capabilities for canvas, including:

[![Image 17](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1290290381/7da3a714296f576702ad1f2ada66/AD_4nXc2e7Kf7xmMuaOpFxDvhBrW7VSUCcqSiKmbTWAKl9rXr1yAwEYVe-OBPNVdyIzP9ya4EOM2-ORKGqLGa0ca0c_Xj3BokIFxivnkdWjG5ifss-gznx_93GTfuOd9_JMZ-_msuZz4Lw?expires=1749403800&signature=513663c8cd817656cf81cc95009c006c62ea52dd1dfdc006bbfb6b85b2494932&req=dSIuFst3nYJXWPMW1HO4zfZmbGEJ8aN3hYw6I29FSCqo0JkH6XyXhxbDVXyJ%0A2nXERL8l2%2FXjH9MvwJM%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1290290381/7da3a714296f576702ad1f2ada66/AD_4nXc2e7Kf7xmMuaOpFxDvhBrW7VSUCcqSiKmbTWAKl9rXr1yAwEYVe-OBPNVdyIzP9ya4EOM2-ORKGqLGa0ca0c_Xj3BokIFxivnkdWjG5ifss-gznx_93GTfuOd9_JMZ-_msuZz4Lw?expires=1749403800&signature=513663c8cd817656cf81cc95009c006c62ea52dd1dfdc006bbfb6b85b2494932&req=dSIuFst3nYJXWPMW1HO4zfZmbGEJ8aN3hYw6I29FSCqo0JkH6XyXhxbDVXyJ%0A2nXERL8l2%2FXjH9MvwJM%3D%0A)

[![Image 18](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1290290390/e86e072ce9c9fe4b97c28704bc85/AD_4nXf1UN0qvbHRoZi5V28X86BH614j43lPiYI9VFry3u0RU8oacZc9JyICW0qBzlZl4iUUiMITDsDHoO_fZJ_2N-8TWBsK_1_8YEYIaDEKpukBT8FgaS4KK6aEl4PoJ051VJswVM7JBg?expires=1749403800&signature=3ae8f2cc0f2c4021efac67d26434b2dabbccddaf524b937d5a8d7ee4a5e0d7aa&req=dSIuFst3nYJWWfMW1HO4zcBns9KnV3bCmu%2BhnH8HLCOJ7D7dFVREmXMCw7zD%0AtruuNzv5aXPjLjPMFFI%3D%0A)](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1290290390/e86e072ce9c9fe4b97c28704bc85/AD_4nXf1UN0qvbHRoZi5V28X86BH614j43lPiYI9VFry3u0RU8oacZc9JyICW0qBzlZl4iUUiMITDsDHoO_fZJ_2N-8TWBsK_1_8YEYIaDEKpukBT8FgaS4KK6aEl4PoJ051VJswVM7JBg?expires=1749403800&signature=3ae8f2cc0f2c4021efac67d26434b2dabbccddaf524b937d5a8d7ee4a5e0d7aa&req=dSIuFst3nYJWWfMW1HO4zcBns9KnV3bCmu%2BhnH8HLCOJ7D7dFVREmXMCw7zD%0AtruuNzv5aXPjLjPMFFI%3D%0A)

## **Nov 22, 2024**

## **Updates to the ChatGPT Web experience**

We are rolling out the following updates over the next two weeks to all ChatGPT users.

### **Sidebar redesign**

### **Other updates for ChatGPT on Web**

### **Improved Mobile Web Experience**

## Nov 19, 2024

## Advanced Voice for ChatGPT Web

Starting today, we’re beginning to roll out Advanced Voice Mode on web (already available on mobile and desktop apps). You can now start a voice chat on chatgpt.com on your desktop and have real-time, natural conversations with ChatGPT while doing tasks like shopping, planning, writing, and brainstorming.

We’re starting to roll out to all paid (Plus, Team, Enterprise, and Edu) users today, and expect it to take a few days.

## **Aug 8, 2024**

## DALL·E 3**for ChatGPT Free users**

We’re rolling out the ability for ChatGPT Free users to create up to two images per day with DALL·E 3.

Just ask ChatGPT to create an image for a slide deck, personalize a card for a friend, or show you what something looks like.

## **July 18, 2024**

## **Introducing GPT-4o mini**

We’re introducing GPT-4o mini, the most capable and cost-efficient small model available today. GPT-4o mini surpasses GPT-3.5 Turbo and other small models on academic benchmarks across both textual intelligence and multimodal reasoning and supports the same range of languages as GPT-4o. It also demonstrates strong performance in function calling, which can enable developers to build applications that fetch data or take actions with external systems, and improved long-context performance compared to GPT-3.5 Turbo.

You can read more about GPT-4o mini in the blog announcement here.

## **May 16, 2024**

## **Improvements to data analysis in ChatGPT**

Today, we’re starting to roll out enhancements to data analysis:

Data analysis improvements are available in our new flagship model, GPT-4o, for ChatGPT Plus, Team, and Enterprise users.

## **May 13, 2024**

## **Introducing GPT-4o**

GPT-4o is our newest flagship model that provides GPT-4-level intelligence that is much faster and improves on its capabilities across text, voice, and vision. Currently, only the new text and image capabilities have been rolled out. You can read more about the announcement here.

Plus users will have a message limit that is up to 5x greater than free users, and Team and Enterprise users will have even higher limits.

## **Apr 29, 2024**

## **Memory is now available to Plus users**

Memory is now available to all ChatGPT Plus users, except in Europe Korea where we will be rolling it out soon. Using Memory is easy: just start a new chat and tell ChatGPT anything you’d like it to remember.

Memory can be turned on or off in settings. Team, Enterprise, and GPTs to come.

## **Apr 1, 2024**

## **Start using ChatGPT instantly**

We’re making it easier for people to experience the benefits of AI without needing to sign up. Starting today, you can use ChatGPT instantly, without needing to sign-up. We're rolling this out gradually, with the aim to make AI accessible to anyone curious about its capabilities.

## **Feb 13, 2024**

## **Memory and new controls for ChatGPT**

We’re testing memory with ChatGPT. Remembering things you discuss across all chats saves you from having to repeat information and makes future conversations more helpful.

You're in control of ChatGPT's memory. You can explicitly tell it to remember something, ask it what it remembers, and tell it to forget conversationally or through settings. You can also turn it off entirely.

We are rolling out to a small portion of ChatGPT free and Plus users this week to learn how useful it is. We will share plans for a broader roll out soon.

You can read more about memory and controls here.

## **Jan 10, 2024**

## **Introducing the GPT Store and ChatGPT Team plan**

#### Discover what’s trending in the GPT Store

The store features a diverse range of GPTs developed by our partners and the community. Browse popular and trending GPTs on the community leaderboard, with categories like DALL·E, writing, research, programming, education, and lifestyle.

Explore GPTs at chatgpt.com/gpts.

#### Use ChatGPT alongside your team

We’re launching a new ChatGPT plan for teams of all sizes, which provides a secure, collaborative workspace to get the most out of ChatGPT at work.

ChatGPT Team offers access to our advanced models like GPT-4 and DALL·E 3, and tools like Advanced Data Analysis. It additionally includes a dedicated collaborative workspace for your team and admin tools for team management. As with ChatGPT Enterprise, you own and control your business data — we do not train on your business data or conversations, and our models don’t learn from your usage. More details on our data privacy practices can be found on our privacy page and Trust Portal.

You can learn more about the ChatGPT Team plan here.

## **November 21, 2023**

## **ChatGPT with voice is available to all users**

ChatGPT with voice is now available to all free users. Download the app on your phone and tap the headphones icon to start a conversation.

## **November 6, 2023**

## **Introducing GPTs**

You can now create custom versions of ChatGPT that combine instructions, extra knowledge, and any combination of skills. Learn more here.

We’re rolling out custom versions of ChatGPT that you can create for a specific purpose—called GPTs. GPTs are a new way for anyone to create a tailored version of ChatGPT to be more helpful in their daily life, at specific tasks, at work, or at home—and then share that creation with others. For example, GPTs can help you learn the rules to any board game, help teach your kids math, or design stickers.

Plus and Enterprise users can start creating GPTs this week. Later this month, we’ll launch the GPT Store, so people can feature and make money from their GPTs. We plan to offer GPTs to more users soon.

## **October 17, 2023**

## **Browsing is now out of beta**

Browsing, which we re-launched a few weeks ago, is moving out of beta.

Plus and Enterprise users no longer need to switch the beta toggle to use browse, and are able to choose "Browse with Bing" from the GPT-4 model selector.

## **October 16, 2023**

## **DALL·E 3 is now rolling out in beta**

We’ve integrated DALL·E 3 with ChatGPT, allowing it to respond to your requests with images. From a simple sentence to a detailed paragraph, ask ChatGPT what you want to see and it will translate your ideas into exceptionally accurate images.

To use DALL·E 3 on both web and mobile, choose DALL·E 3 in the selector under GPT-4. The message limit may vary based on capacity.

## **September 27, 2023**

## **Browsing is rolling back out to Plus users**

Browsing is rolling out to all Plus users. ChatGPT can now browse the internet to provide you with current and authoritative information, complete with direct links to sources. It is no longer limited to data before September 2021.

To try it out, enable Browsing in your beta features setting.

Choose Browse with Bing in the selector under GPT-4.

## **September 25, 2023**

## **New voice and image capabilities in ChatGPT**

We are beginning to roll out new voice and image capabilities in ChatGPT. They offer a new, more intuitive type of interface by allowing you to have a voice conversation or show ChatGPT what you’re talking about. Learn more here.

#### Voice (Beta) is now rolling out to Plus users on iOS and Android

You can now use voice to engage in a back-and-forth conversation with your assistant. Speak with it on the go, request a bedtime story, or settle a dinner table debate.

To get started with voice, head to Settings → New Features on the mobile app and opt into voice conversations. Then, tap the headphone button located in the top-right corner of the home screen and choose your preferred voice out of five different voices.

#### Image input will be generally available to Plus users on all platforms

You can now show ChatGPT one or more images. Troubleshoot why your grill won’t start, explore the contents of your fridge to plan a meal, or analyze a complex graph for work-related data. To focus on a specific part of the image, you can use the drawing tool in our mobile app.

To get started, tap the photo button to capture or choose an image. You can also discuss multiple images or use our drawing tool to guide your assistant.

## **September 11, 2023**

## **ChatGPT language support - Alpha on web**

ChatGPT now supports a limited selection of languages in the interface:

If you've configured your browser to use one of these supported languages, you'll see a banner in ChatGPT that enables you to switch your language settings. You can deactivate this option at any time through the settings menu.

This feature is in alpha, requires opting in, and currently can only be used on the web at chatgpt.com. Learn more here.

## August 28, 2023

## Introducing ChatGPT Enterprise

Today we’re launching ChatGPT Enterprise, which offers enterprise-grade security and privacy, unlimited higher-speed GPT-4 access, longer context windows for processing longer inputs, advanced data analysis capabilities, customization options, and much more.

ChatGPT Enterprise also provides unlimited access to Advanced Data Analysis, previously known as Code Interpreter.

Learn more on our website and connect with our sales team to get started.

## August 21, 2023

## Custom instructions are now available to users in the EU & UK

Custom instructions are now available to users in the European Union United Kingdom.

To add your instructions:

## August 9, 2023

## Custom instructions are now available to free users

Custom instructions are now available to ChatGPT users on the free plan, except for in the EU UK where we will be rolling it out soon!

Customize your interactions with ChatGPT by providing specific details and guidelines for your chats.

To add your instructions:

## August 3, 2023

## Updates to ChatGPT

We’re rolling out a bunch of small updates to improve the ChatGPT experience. Shipping over the next week:

1. Prompt examples: A blank page can be intimidating. At the beginning of a new chat, you’ll now see examples to help you get started.

2. Suggested replies: Go deeper with a click. ChatGPT now suggests relevant ways to continue your conversation.

3. GPT-4 by default, finally: When starting a new chat as a Plus user, ChatGPT will remember your previously selected model — no more defaulting back to GPT-3.5.

4. Upload multiple files: You can now ask ChatGPT to analyze data and generate insights across multiple files. This is available with the Code Interpreter beta for all Plus users.

5. Stay logged in: You’ll no longer be logged out every 2 weeks! When you do need to log in, you’ll be greeted with a much more welcoming page.

6. Keyboard shortcuts: Work faster with shortcuts, like ⌘ (Ctrl) + Shift + ; to copy last code block. Try ⌘ (Ctrl) + / to see the complete list.

## July 25, 2023

## Introducing the ChatGPT app for Android

ChatGPT for Android is now available for download in the United States, India, Bangladesh, and Brazil from the Google Play Store.

We plan to expand the rollout to additional countries over the next week. You can track the Android rollout here.

## July 20, 2023

## Custom instructions are rolling out in beta

We’re starting to roll out custom instructions, giving you more control over ChatGPT’s responses. Set your preferences once, and they’ll steer future conversations. You can read more about custom instructions in the blogpost here.

Custom instructions are available to all Plus users and expanding to all users in the coming weeks.

To enable beta features:

To add your instructions:

This feature is not yet available in the UK and EU.

## July 19, 2023

## Higher message limits for GPT-4

We're doubling the number of messages ChatGPT Plus customers can send with GPT-4. Rolling out over the next week, the new message limit will be 40 every 3 hours.

## July 6, 2023

## Code interpreter is now rolling out in beta on web

We’re rolling out code interpreter to all ChatGPT Plus users over the next week.

It lets ChatGPT run code, optionally with access to files you've uploaded. You can ask ChatGPT to analyze data, create charts, edit files, perform math, etc.

We’ll be making these features accessible to Plus users on the web via the beta panel in your settings over the course of the next week.

To enable code interpreter:

## July 3, 2023

## Browsing is temporarily disabled

We've learned that the browsing beta can occasionally display content in ways we don't want, e.g. if a user specifically asks for a URL's full text, it may inadvertently fulfill this request. We are temporarily disabling Browse while we fix this.

## June 22, 2023

## Browsing and search on mobile

We’ve made two updates to the mobile ChatGPT app:

## May 24, 2023

## iOS app available in more countries, shared links in alpha, Bing Plugin, disable history on iOS

#### ChatGPT app for iOS in more countries

Good news! We’re expanding availability of the ChatGPT app for iOS to more countries and regions. Users in 11 countries can now download the ChatGPT app in the Apple App Store including the United States: Albania, Croatia, France, Germany, Ireland, Jamaica, Korea, New Zealand, Nicaragua, Nigeria, and the United Kingdom.

We will continue to roll out to more countries and regions in the coming weeks. You can track the iOS app rollout here.

#### Shared Links

We're excited to introduce a new feature: shared links. This feature allows you to create and share your ChatGPT conversations with others. Recipients of your shared link can either view the conversation or copy it to their own chats to continue the thread. This feature is currently rolling out to a small set of testers in alpha, with plans to expand to all users (including free) in the upcoming weeks.

To share your conversations:

Learn more.

#### Bing Plugin

Browse with Bing. We’ve integrated the browsing feature - currently in beta for paid users - more deeply with Bing. You can now click into queries that the model is performing. We look forward to expanding the integration soon.

#### Disable chat history on iOS

You can now disable your chat history on iOS. Conversations started on your device when chat history is disabled won’t be used to improve our models, won’t appear in your history on your other devices, and will only be stored for 30 days. Similar to the functionality on the web, this setting does not sync across browsers or devices. Learn more.

## May 12, 2023

## Web browsing and Plugins are now rolling out in beta

If you are a ChatGPT Plus user, enjoy early access to experimental new features, which may change during development. We’ll be making these features accessible via a new beta panel in your settings, which is rolling out to all Plus users over the course of the next week.

[![Image 19](https://downloads.intercomcdn.com/i/o/740734818/c7d818c221f5f023ab1a0c27/BetaPanel.png?expires=1749403800&signature=d7af2e1db54f958be216e91b684a2ad3c86247f411c9525288cd855670959a1c&req=cyQnEcp6lYBXFb4f3HP0gPBVDqDeE5127qEhBW3N3eqmvc07%2FAtaj1jDoxhJ%0AZpkoURcH0Usupk96FQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/740734818/c7d818c221f5f023ab1a0c27/BetaPanel.png?expires=1749403800&signature=d7af2e1db54f958be216e91b684a2ad3c86247f411c9525288cd855670959a1c&req=cyQnEcp6lYBXFb4f3HP0gPBVDqDeE5127qEhBW3N3eqmvc07%2FAtaj1jDoxhJ%0AZpkoURcH0Usupk96FQ%3D%3D%0A)

Once the beta panel rolls out to you, you’ll be able to try two new features:

To use third-party plugins, follow these instructions:

To enable beta features:

For more information on our rollout process, please check out the article here.

In addition to the beta panel, users can now choose to continue generating a message beyond the maximum token limit. Each continuation counts towards the message allowance.

## May 3, 2023

## Updates to ChatGPT

We’ve made several updates to ChatGPT! Here's what's new:

## March 23, 2023

## Introducing plugins in ChatGPT

We are announcing experimental support for AI plugins in ChatGPT — tools designed specifically for language models. Plugins can help ChatGPT access up-to-date information, run computations, or use third-party services. You can learn more about plugins here.

Today, we will begin extending plugin access to users and developers from our waitlist. The plugins we are rolling out with are:

You can join the waitlist to try plugins here:

## March 14, 2023

## Announcing GPT-4 in ChatGPT

We’re excited to bring GPT-4, our latest model, to our ChatGPT Plus subscribers.

GPT-4 has enhanced capabilities in:

To give every Plus subscriber a chance to try the model, we'll dynamically adjust the cap for GPT-4 usage based on demand. You can learn more about GPT-4 here.

For this release, there are no updates to free accounts.

## Feb 13, 2023

## Updates to ChatGPT

We’ve made several updates to ChatGPT! Here's what's new:

## Feb 9 2023

## Introducing ChatGPT Plus

As we recently announced, our Plus plan comes with early access to new, experimental features. We are beginning to roll out a way for Plus users the ability to choose between different versions of ChatGPT:

Version selection is made easy with a dedicated dropdown menu at the top of the page. Depending on feedback, we may roll out this feature (or just Turbo) to all users soon.

## Jan 30, 2023

## Factuality and mathematical improvements

We’ve upgraded the ChatGPT model with improved factuality and mathematical capabilities.

## Jan 9, 2023

## Updates to ChatGPT

We're excited to announce several updates to ChatGPT! Here's what's new:

## Dec 15, 2022

## Performance updates to ChatGPT

We're excited to announce several updates to ChatGPT! Here's what's new:

To see if you’re using the updated version, look for “ChatGPT Dec 15 Version” at the bottom of the screen.

---

Related Articles

[What is the ChatGPT model selector?](https://help.openai.com/en/articles/7864572-what-is-the-chatgpt-model-selector)[Model Release Notes](https://help.openai.com/en/articles/9624314-model-release-notes)[ChatGPT MacOS app release notes](https://help.openai.com/en/articles/9703738-chatgpt-macos-app-release-notes)[ChatGPT Enterprise & Edu - Release Notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes)[ChatGPT Team - Release Notes](https://help.openai.com/en/articles/11391654-chatgpt-team-release-notes)
