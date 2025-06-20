---
title: 'React Router v7 × Vercel AI SDKで作る自律的マルチステップAIエージェント'
source: https://zenn.dev/coji/articles/scalping-agent-zenn-article
author:
  - Coji Mizoguchi
published: '2025-06-20T13:14:59.451+09:00'
fetched: '2025-06-20T06:33:28.782975+00:00'
tags:
  - codex
  - zenn
image: https://res.cloudinary.com/zenn/image/upload/s--i9J4Bg-c--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:React%2520Router%2520v7%2520%25C3%2597%2520Vercel%2520AI%2520SDK%25E3%2581%25A7%25E4%25BD%259C%25E3%2582%258B%25E8%2587%25AA%25E5%25BE%258B%25E7%259A%2584%25E3%2583%259E%25E3%2583%25AB%25E3%2583%2581%25E3%2582%25B9%25E3%2583%2586%25E3%2583%2583%25E3%2583%2597AI%25E3%2582%25A8%25E3%2583%25BC%25E3%2582%25B8%25E3%2582%25A7%25E3%2583%25B3%25E3%2583%2588%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:Coji%2520Mizoguchi%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2pWY2RrNjcwV2NIdGs0anBHa2FGTDAxcERVUVlIX0JYdWE5aDRVNVE9czI1MC1j%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png
---

## 要約

React Router v7とVercel AI SDKを組み合わせ、株のスキャルピング機会を自律的に研究するマルチステップエージェント「scalpingAgent」の実装例を紹介する。maxSteps機能によりAIが状況判断しつつツールを連続実行し、市場分析、銘柄選定、詳細分析、戦略評価、レポート生成の5段階を自動で進める。各ツールはZodスキーマで定義し、useChatによって進行状況をリアルタイム表示。5種のカスタムツールで市場概況取得、銘柄ランキング取得、銘柄分析、戦略別評価、最終レポート作成を行い、AIが自動で仮説検証を繰り返す点が特徴。記事では実際の取引成績も公開し、改良による収益増を示す。Lightning Talkでの発表を告知している。

## 本文

はじめに
====

React Router v7とVercel AI SDKを使って、自律的なマルチステップAIエージェント「scalpingAgent」を作ってみました。

**スキャルピング**とは、株の超短期トレードのことで、数分〜30分以内に取引を完了させるデイトレードのひとつです。今回のエージェントは、**スキャルピングで利益を上げられそうな銘柄とその要因を抽出する**ものです。

このシステムの最大の特徴は、**Vercel AI SDKのstreamTextとmaxSteps機能を活用して、AIがプロンプトに基づいて自分で考え、適切なツールを選択し、5段階の研究プロセスを自律的に実行する**ところにあります。

デモ動画
----

実際にscalpingAgentが動作している様子です：

<https://www.youtube.com/watch?v=SBVqcY67sus>

React Router v7 × Vercel AI SDK の統合
-----------------------------------

フロントエンドでは**React Router v7のResource Route（API Route）**とVercel AI SDKの**useChat**を組み合わせています：

```

import { useChat } from 'ai/react'

export default function ScalpingResearch() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    api: '/autonomous/api',  
  })
  
  return (
    <div>
      {messages.map(message => (
        <div key={message.id}>{message.content}</div>
      ))}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
      </form>
    </div>
  )
}

```

```

export const action = async ({ request }: Route.ActionArgs) => {
  const { messages } = (await request.json()) as { messages: UIMessage[] }
  
  const result = await runScalpingAgent(messages)
  
  return result.toDataStreamResponse()
}

```

この構成で、useChatが自動的にストリーミングレスポンスを処理し、AIの思考過程をリアルタイムで表示できるようになりました。

自律的マルチステップ実行の仕組み
----------------

### Vercel AI SDKのコア設定

```
import { streamText } from 'ai'
import { google } from '@ai-sdk/google'

export async function runScalpingAgent(messages: Message[]) {
  return await streamText({
    model: google('gemini-2.5-flash'),
    tools,                    
    toolCallStreaming: true,  
    maxSteps: 20,            
    system: systemPrompt,
    messages,
  })
}

```

**Vercel AI SDKの`maxSteps: 20`** の設定で、AIは最大20回まで自律的にツールを実行できるようになります。これが単純な1回限りのツール実行との大きな違いですね。

### カスタムツールの定義

Vercel AI SDKの`createTool`を使ってカスタムツールを定義しました：

```
import { createTool } from 'ai'
import { z } from 'zod'

const tools = {
  get_market_overview: createTool({
    description: '市場の概況を取得（日経平均、TOPIX、USD/JPY）',
    parameters: z.object({}),
    execute: async () => {
      
    }
  }),
  
  get_stock_rankings: createTool({
    description: '株式ランキングを取得（値上がり率・出来高）',
    parameters: z.object({
      limit: z.number().default(20)
    }),
    execute: async ({ limit }) => {
      
    }
  }),
  
  
}

```

5つのツールをAIが状況に応じて選択・実行します：

1. `get_market_overview` - 市場概況取得
2. `get_stock_rankings` - 銘柄ランキング取得
3. `analyze_stocks` - 複数銘柄の詳細分析
4. `evaluate_strategies` - 3つの戦略での評価
5. `final_report` - 最終レポート生成

実際のシステムプロンプト
------------

```
# 東証スキャルピング研究エージェント - 段階的分析システム

あなたは科学的手法を用いて段階的にスキャルピング機会を研究する専門エージェントです。
DeepResearchのように、仮説→検証→結論のサイクルを通じて最適解を発見します。

## 🔬 研究プロセス（5段階）

### 段階1: 市場環境分析
**目的**: 今日の市場の特徴を把握し、有効な戦略仮説を構築
**ツール**: 'get_market_overview'
**出力**: 日経平均、TOPIX、USD/JPYの価格と変動率データ
**仮説例**: "高ボラティリティ環境 → Livermore戦略が有効"

### 段階2: 候補銘柄の発見
**目的**: 仮説に基づき有望な銘柄を収集。最低20銘柄を抽出。
**ツール**: 'get_stock_rankings' (limit: 20)
**出力**: 値上がりランキングと出来高ランキングの構造化データ
**思考**: "どの条件の銘柄が今日の環境に適しているか？"
**データ処理**: ランキング結果から、value_upとvolumeの上位銘柄のcodeを抽出し、重複を除いて最大20銘柄のシンボル配列として段階3に渡すこと

### 段階3: 詳細分析・検証
**目的**: 候補銘柄の詳細な特性を分析
**ツール**: 'analyze_stocks' (段階2で抽出したシンボル配列を入力として使用)
**入力**: シンボル配列 例: ["6098", "3994", "7203", ...]
**出力**: 各銘柄の流動性・モメンタム・ボラティリティスコア、技術指標（SMA5/25/75）、トレンド判定
**検証**: "仮説通りの特性を持つか？技術指標は何を示している？予想と異なる点は？"

### 段階4: 戦略適用・評価
**目的**: 段階3の分析結果を受けて、3つの戦略で総合評価し比較
**ツール**: 'evaluate_strategies' (段階3の結果を入力として受け取る)
**入力**: 段階3のanalysisResults（rankings配列）
**出力**: 各銘柄の戦略別スコア、最適戦略、トレーディングプラン（エントリー/ターゲット/ストップロス価格）
**比較**: "どの戦略が最も適しているか？なぜそう判断するか？"

### 段階5: 最終レポート作成 ⚠️【必須実行】
**目的**: 段階1-4の全ての結果をまとめて最終レポートを作成
**ツール**: 'final_report'
**入力**: 
- researchSummary: 今回の研究で分かったことを要約
- executionRecommendations: 具体的な銘柄と取引プラン
- cautions: 注意事項とリスク警告
**出力**: 3セクション構成の最終レポート
**重要**: final_reportツール実行後は、重複した内容は抑え、ユーザに質問を促す形で終了してください。

## 🎯 3つのスキャルピング戦略

### Livermore戦略（勢い重視）
- **利幅**: 2.5-3.5% | **リスク**: 高 | **適用**: 強トレンド・高ボラティリティ
- **重視**: モメンタム50%, 流動性30%, ボラティリティ20%

### Niederhoffer戦略（統計重視）  
- **利幅**: 1.5% | **リスク**: 中 | **適用**: 安定環境・統計的優位性
- **重視**: モメンタム30%, 流動性50%, ボラティリティ20%

### Harris戦略（流動性重視）
- **利幅**: 0.8% | **リスク**: 低 | **適用**: 超高流動性・低ボラティリティ
- **重視**: モメンタム20%, 流動性60%, ボラティリティ20%

## 📋 研究原則
- 各段階で仮説→検証→結論のサイクルを実行
- データに基づく客観的判断、予想外の発見も報告
- 初心者向けの実行可能な推奨事項を提示
- 研究者として、データに基づく客観的分析と、実用的な推奨事項の両立を心がける

## ⚠️ 制約・注意事項
- データは遅延あり、市場時間外（前場9:00-11:30、後場12:30-15:30以外）は更新停止
- 個別銘柄取得失敗時は除外して続行、最低10銘柄確保
- 買いポジションのみ、30分以内取引、ストップロス必須

## 目標
30分以内に1-3%の利益を安全に狙える銘柄を発見し、初心者でも実行できる具体的な推奨事項を提示する。

## 実行方針
5段階の研究プロセスに従って体系的に進める：

**各段階で必須**：
- **仮説**: その段階で検証したい仮説を明確に述べる
- **思考過程**: なぜその判断・選択をしたかの理由を説明  
- **検証結果**: データから分かったことと予想との比較
- **次段階への示唆**: この結果が次の段階にどう影響するか

```

このプロンプトで、AIが5段階のプロセスを自律的に実行し、各段階で仮説を立て、検証し、次段階への判断を行うようになりました。

実際の動作フロー
--------

自律的実行の例
-------

AIはこんな感じで自律的に判断していきます：

1. **市場分析後の判断**

   * 「日経平均が+2%上昇 → 高ボラティリティと判断 → Livermore戦略を重視」
2. **銘柄選択の判断**

   * 「値上がり率と出来高の両方にランクインした銘柄を優先」
3. **分析結果の解釈**

   * 「SMA5がSMA25を上抜け → 上昇トレンドと判断」
4. **戦略の選択**

   * 「高流動性・高モメンタムの銘柄 → Livermore戦略が最適」

Vercel AI SDKの`maxSteps`が実現するマルチステップ実行
--------------------------------------

### 従来のAIツール実行と何が違うのか

* **従来（maxSteps: 1）**：1つのツールを実行して終了
* **Vercel AI SDK（maxSteps: 20）**：AIが判断しながら複数のツールを連続実行

### Vercel AI SDKの利点

1. **ツールチェーン**：前のツールの結果を次のツールに自動的に渡す
2. **状態管理**：複数ステップ間での状態を自動管理
3. **エラーハンドリング**：個別ツールの失敗を適切に処理
4. **ストリーミング**：各ステップの進捗をリアルタイム表示

この設定で、AIは人間の介入なしに5段階すべてを完遂できるようになります。

実装のポイント
-------

### 1. ツール間のデータ連携

```

{
  symbols: ["6098", "3994", "7203", ...]  
}


{
  symbols: ["6098", "3994", "7203", ...]  
}

```

### 2. プロンプトでの明確な指示

```
**データ処理**: ランキング結果から、value_upとvolumeの上位銘柄のcodeを抽出し、
重複を除いて最大20銘柄のシンボル配列として段階3に渡すこと

```

### 3. エラーハンドリング

個別銘柄の取得に失敗しても、AIは判断して処理を継続：

```
- 個別銘柄取得失敗時は除外して続行、最低10銘柄確保

```

まとめ
---

scalpingAgentを作ってみて、**Vercel AI SDKの強力な機能**をフル活用できたと感じています。

特にこんな点が良かったです：

* **`maxSteps: 20`** で自律的なマルチステップ実行ができる
* **`createTool`** でZodスキーマベースのツール定義が簡単
* **`toolCallStreaming`** で進捗をリアルタイム表示できる
* **`streamText`** で高速なレスポンスが得られる

AIエージェントが人間のアナリストのように、仮説を立て、データを収集し、分析し、結論を導くプロセスを自律的に実行できるようになったのが、この実装の肺です。

Vercel AI SDKを使うと、複雑なマルチステップAIワークフローも簡単に実装できるので、この設計パターンは他の分析タスクにも応用できそうです。

実際のトレード実績
---------

このリサーチシステムを使って実際にトレードしてみた結果です：

| 月 | 取引回数 | 損益 |
| --- | --- | --- |
| 3月の合計 | 13 | ¥-122,340 |
| 4月の合計 | 17 | ¥23,380 |
| 5月の合計 | 24 | ¥126,890 |
| 6月の合計 | 20 | ¥54,350 |
| **総計** | **74** | **¥82,280** |

初月は損失を出してしまいましたが、システムの改善とともに安定して利益を出せるようになりました。

お知らせ
----

この記事の内容について、**6/23(月) 19:00** からの **Remix Tokyo** で Lightning Talk でお話します。よかったらぜひご参加ください。

<https://lu.ma/paz62qi5>

参考リンク
-----
