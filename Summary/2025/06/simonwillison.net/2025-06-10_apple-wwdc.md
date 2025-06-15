---
title: 'WWDC: Apple supercharges its tools and technologies for developers'
source: https://simonwillison.net/2025/Jun/9/apple-wwdc/
author: Simon Willison
published: '2025-06-09T19:42:00Z'
fetched: '2025-06-10T09:33:08.998412+00:00'
tags:
- codex
- ai
image: ''
---

## 要約

WWDCの発表から特に注目すべきはプライバシーを守りつつオフライン推論を実現する**Foundation Models Framework**とAppleシリコンで安全にコンテナを実行できる**Containerization Framework**であり前者は3Bモデルを2bit量子化しSwiftから数行で利用可能で後者は各コンテナを軽量VMで隔離しOCI互換を保ちながら理想的なサンドボックスを提供すると評価している

## 本文

**[WWDC: Apple supercharges its tools and technologies for developers](https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/)**. Here's the Apple press release for today's WWDC announcements. Two things that stood out to me:

> **Foundation Models Framework**
>
> With the Foundation Models framework, developers will be able to build on Apple Intelligence to bring users new experiences that are intelligent, available when they’re offline, and that protect their privacy, using AI inference that is free of cost.
> The framework has native support for Swift, so developers can easily access the Apple Intelligence model with as few as three lines of code.

Here's new documentation on [Generating content and performing tasks with Foundation Models](https://developer.apple.com/documentation/FoundationModels/generating-content-and-performing-tasks-with-foundation-models) - the Swift code looks like this:

```
let session = LanguageModelSession(
    instructions: "Reply with step by step instructions"
)
let prompt = "Rum old fashioned cocktail"
let response = try await session.respond(
    to: prompt,
    options: GenerationOptions(temperature: 2.0)
)
```

There's also a [23 minute Meet the Foundation Models framework](https://developer.apple.com/videos/play/wwdc2025/286/) video from the conference, which clarifies that this is a 3 billion parameter model with 2 bit quantization. The model is trained for both tool-calling and structured output, which they call "guided generation" and describe as taking advantage of constrained decoding.

I'm also _very_ excited about this:

> **Containerization Framework**
>
> The Containerization framework enables developers to create, download, or run Linux container images directly on Mac. It’s built on an open-source framework optimized for Apple silicon and provides secure isolation between container images.

I continue to seek the ideal sandboxing solution for running untrusted code - both from other humans and written for me by LLMs - on my own machines. This looks like it could be a really great option for that going forward.

It looks like [apple/container](https://github.com/apple/container) on GitHub is part of this new feature. From the [technical overview](https://github.com/apple/container/blob/main/docs/technical-overview.md):

> On macOS, the typical way to run Linux containers is to launch a Linux virtual machine (VM) that hosts all of your containers.
>
> `container` runs containers differently. Using the open source [Containerization](https://github.com/apple/containerization) package, it runs a lightweight VM for each container that you create. [...]
>
> Since `container` consumes and produces standard OCI images, you can easily build with and run images produced by other container applications, and the images that you build will run everywhere.
