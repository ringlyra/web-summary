---
title: Claude Code のすすめ
source: https://speakerdeck.com/schroneko/getting-started-with-claude-code
author:
- schroneko
published: '2025-06-03T00:00:00Z'
fetched: '2025-06-04T02:37:24Z'
tags:
- codex
- ai
image: https://files.speakerdeck.com/presentations/d25a0c8d12644628866d1c285a97c985/slide_0.jpg?35330030
---

## 要約

ハイブリッドリーズニングモデル**Claude Code**の特徴と、トークン数を調整して利用する方法を解説するスライド。

## 本文

o のつくモデルのようになんでもかんでも考えるモデルとは打って変わって、Claude はどれだけ考えてくれ るかを調整できるハイブリッドリーズニングモデルです。明示的に指定して初めて思考過程を見せてくれ るモデルです。設計時や難しめのデバッグ、実装計画、分析などによし。 注: リーズニングが有効なタスクとそうでないタスクがあるので濫用は禁物 発動条件と思考に割り当てるトークン数 まず、環境変数 MAX_THINKING_TOKENS が指定されていればキーワードに関係なくその値が優先されま す。MAX_THINKING_TOKENS が指定されておらず、特定のワードが含まれている時に三段階で思考に割 り当てられるトークン数が決定します。現状 8 つの言語に対応。 BASIC（4,000） 「考えて」 「think」 MIDDLE（10,000） 「よく考えて」 「もっと考えて」 「たくさん考えて」 「think hard」 「megathink」 HIGHEST（31,999） 「熟考」 「深く考えて」 「しっかり考えて」 「ultrathink」 「think harder」 1 / 28
