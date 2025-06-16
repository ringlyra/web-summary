---
title: Why Fireworks Scrapped Creating Their Own Agents Framework to Build with Mastra
source: https://mastra.ai/blog/fireworks-xml-prompting
author:
- mastra.ai
published: '2025-06-10'
fetched: '2025-06-11T07:00:58.236873+00:00'
tags:
- codex
- ai
- agents
image: https://mastra.ai/api/og/blog?title=Why%20Fireworks%20Scrapped%20Creating%20Their%20Own%20Agents%20Framework%20to%20Build%20with%20Mastra&date=Jun%2010,%202025
---

## 要約

Fireworks AIはUberやCursorなどを顧客にもつ推論プラットフォームで、元Metaのエンジニアが立ち上げた。エージェント基盤を自社で構築しようとしていたが、マストラを採用することでステートマシンの実装を省き、AIMLというXMLタグ付きプロンプトで多段階処理が書けるフレームワークを短期間で公開した。マストラはフィードバックを受けて値の受け渡し機能などを改善し、MetaやAirbnbの開発者も試用中である。これによりFireworksのチームは内部インフラよりUXに注力でき、リアルタイムトレースなど本番運用へ向けた機能開発を進めている。この流れは、言語モデル活用の敷居を下げ、より迅速に製品開発を進めるための好例といえる。

## 本文

Fireworks AI is an inference platform that runs open-source models and processes over 140 billion tokens daily for companies like Uber, DoorDash, and Cursor. Founded in October 2022 by former Meta engineers Lin Qiao and Dmytro Dzhulgakov who built and ran PyTorch, Fireworks recently closed a $52M Series B at a valuation over $500 million.

## Building infrastructure from scratch

In September 2024 Matt Apperson, a Staff Software Engineer at Fireworks, was tasked with "figuring out, documenting and executing on an agentic vision for Fireworks." The goal was to build a hosted agentic system similar to OpenAI's Assistant API, but with the control and programmability requested by Fireworks' customers.

"I'm a big fan of using state machines for agentic flows," Matt explains. "I think they make a lot of sense, but they're not quite perfect, they're a little verbose." The team was prototyping a three-layer architecture: a state machine foundation, an agentic runtime on top of that, then an API layer.

But finding the right foundation proved challenging. "There wasn't really a lot out there that was not Python based, that was robust, that wasn't just like, give me a prompt and we do something magical with it, but something that's controllable and somewhat programmatic," Matt recalls. Existing solutions like LangChain "were either too much or too little, and it wasn't something that sort of allowed other pieces of the TypeScript ecosystem."

So Fireworks started building their own. Matt had gotten 75% of the way through implementing a custom state machine system when he found Mastra.

## Matt discovers Mastra

Matt discovered Mastra while browsing GitHub to get a lay of the land. He found Mastra and was immediately impressed: "You guys were already using XState, which we were too."

The timing couldn't have been better. "Mastra basically handed us that first layer in a nice neat little bow," Matt explains. "I was like, all right, well then screw having to write. And I had it like 75% written. But I was like, this will replace that."

## Building AIML: Multi-step agents through prompting

Using Mastra workflows as their foundation, the Fireworks team built AIML, an open source framework that allows developers to build multi-step agentic systems using only prompts with special XML tags.

"Instead of sending just text as a system prompt to Fireworks API, you can send these AIML style prompts," Matt explains. "It has just special XML tags just like you use XML that are more functional."

![AIML workflow visualization showing state graph with Incoming Request, Think, Answer, and Stream Response nodes](https://mastra.ai/images/casestudy-fireworks-1.png)

The system works by parsing XML-tagged prompts, breaking them down into document order flows based on SCXML state graphs, then dynamically composing Mastra workflows to execute the logic. The result: complex agentic workflows that can be built and iterated on without writing code.

"The general idea here being that you no longer need to worry about whether your code is TypeScript or not, whether you have Java or PHP or Python, whether your product team is building in TypeScript but your AI experts know Python," Matt notes. "It's a whole lot easier to hand a prompt back and forth than it is, you know, here's a Python notebook and - convert that to TypeScript."

![AIML code examples showing Simple control flow, Real-time streaming, and State & Context features](https://mastra.ai/images/casestudy-fireworks-2.png)

The Mastra team worked closely with Matt during development. "The biggest pain point being the concept around being able to pass things from values from one step to the next," Matt said. The Fireworks team had wrapped Mastra workflows in a class to automatically pass values between steps, and shared this feedback with the Mastra team, who "implemented it quickly, but not just like, slapping it together, but really kind of thoughtfully applying the feedback from a first principles perspective."

## Early traction and focus shift

AIML is in use at some big companies. "At the moment we have a few developers from within Meta and within Airbnb and a few other bigger companies that have already started prototyping with AIML" Matt reports.

More importantly, using Mastra allowed the team to shift focus from infrastructure to user experience. "It allowed us to definitely take a step back and stop worrying about the internals," Matt reflects. "It allowed us to focus much more on the experience." The team is currently working on real-time tracing capabilities and preparing for broader production use.
