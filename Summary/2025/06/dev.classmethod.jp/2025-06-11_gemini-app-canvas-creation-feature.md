---
title: Gemini アプリ Canvas の作成機能でスライド作成が捗りそう！ | DevelopersIO
source: https://dev.classmethod.jp/articles/gemini-app-canvas-creation-feature/
author:
- エノカワ
published: '2025-06-11T00:00:00+09:00'
fetched: '2025-06-11T08:32:14.646145+00:00'
tags:
- codex
- ai
- gemini
image: https://images.ctfassets.net/ct0aopd36mqt/wp-thumbnail-6a331d7c70f1897ca2ef1ad4cbe7c6bf/78c556633ae5115aa065636cc4a1160a/eyecatch_gemini
---

## 要約

Gemini アプリのCanvas機能に新設された「作成」メニューでは、テキストを入力するだけでウェブページやインフォグラフィック、テスト、音声概要を自動生成でき、生成されたコンテンツはコード編集も可能だ。Canvasではテキストや画像を自由に配置して情報の関連性を視覚化でき、チャット形式と切り替えられる。DeepResearchと連携すれば最新情報の収集から視覚化までをシームレスに行え、プレゼン資料の下地作りが大幅に効率化する。ウェブページはスライド構成の骨格となり、インフォグラフィックは視覚素材を即座に生成、テストは聴衆の理解度を高め、音声概要は発表練習にも役立つ。著者はCloudNative Daysの経験を引き合いに、この機能を活用することでより訴求力のある資料が作成できると強調している。

## 本文

![Gemini アプリ Canvas の作成機能でスライド作成が捗りそう！](https://images.ctfassets.net/ct0aopd36mqt/wp-thumbnail-6a331d7c70f1897ca2ef1ad4cbe7c6bf/78c556633ae5115aa065636cc4a1160a/eyecatch_gemini)

# Gemini アプリ Canvas の作成機能でスライド作成が捗りそう！

[#Gemini](/tags/gemini/)

[#Google Cloud (GCP)](/tags/google-cloud/)

[#生成AI](/tags/generative-ai/)

[#AI](/tags/ai/)

[![エノカワ](https://devio2023-media.developers.io/wp-content/uploads/devio_thumbnail/2024-06/enokawa-hayato.jpeg)

エノカワ](/author/enokawa-hayato/)

こんにちは！エノカワです。

Google が提供するAIアシスタント **Gemini** アプリに、新たに **Canvas で作成** 機能が追加されました。

- [Gemini アプリの機能アップデート > 2025.05.20](https://gemini.google.com/updates?hl=ja#:~:text=%E3%81%8C%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82-,Canvas%20%E3%81%A7%E4%BD%9C%E6%88%90,-%E6%9B%B4%E6%96%B0%E5%86%85%E5%AE%B9%3A)

> Canvas で作成
>
> 更新内容: Canvas の新しい利用方法をご紹介します。このたび、新しい [作成] メニューでテキストを変換し、さまざまな動的コンテンツ、カスタマイズされたウェブページ、視覚的にすぐれたインフォグラフィック、やる気を引き出すテスト、臨場感あふれる音声概要を作成できるようになりました。作成したいものを説明するだけで Gemini がコードを生成し、実用的なプロトタイプを構築する様子も確認できます。プロトタイプができたら、Gemini と相談しながら自分のニーズに合わせてカスタマイズすることができます。

## Gemini の Canvas 機能とは？

Canvas 機能は、Geminiの通常のチャットインターフェースを超えて、より自由な形式でのアイデアの整理や視覚化を可能にする機能です。  
テキスト、画像、リンクなどの要素を自由に配置し、それらの関係性を視覚的に表現できます。

Canvas の主な特徴は以下の通りです。

- **自由な配置と整理**: テキストや画像を自由に配置し、関連性を視覚的に表現
- **Gemini による支援**: Gemini が内容の提案や整理をサポート
- **複数のビュー**: チャット形式とCanvas形式を切り替え可能
- **コラボレーション**: 共有リンクを通じて他のユーザーとの共同作業が可能
- **作成機能**: ウェブページ、インフォグラフィック、テスト、音声概要など様々なコンテンツを作成可能

今回は特に **「作成機能」** に注目し、**スライド作成** における活用方法に焦点を当ててご紹介します。

## Canvas の作成

作成機能を活用するには、まず新しい Canvas を作成します。

### DeepResearch 連携

今回は DeepResearch で作成したレポートを Canvas に取り込んで作成します。  
DeepResearch で収集した情報を Canvas に直接取り込むことができるため、リサーチからアイデア整理、視覚化までの一連の作業をシームレスに行うことができます。

DeepResearch を有効化するには、画面に表示されるトグルスイッチをオンにするだけです。  
これにより、Gemini はウェブ上の最新情報にアクセスし、質問に対してより正確で包括的な回答を提供できるようになります。

![gemini-app-canvas-creation-feature_01.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/lN8lEcSZbt4f.png)

先日、沖縄で開催された **CloudNative Days Summer 2025** でキーノートスピーカーを務めた際も、スライド作成のためにこの DeepResearch 機能を活用しました。

<https://dev.classmethod.jp/articles/cloudnative-days-summer-2025-okinawa-dx-cnds2025/>

「クラウドデータ基盤で切り拓く沖縄DXの可能性」というテーマで発表するにあたり、沖縄の産業状況やDXの課題、クラウドデータ基盤の活用事例など、多岐にわたる情報収集が必要でした。

今回も同様に「沖縄DXとクラウドデータ基盤」をキーワードにリサーチを行います。  
画面上の **[リサーチを開始]** をクリックすると、Gemini が関連情報の収集を始めます。

![gemini-app-canvas-creation-feature_02.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/9aCUNX3Y0jrZ.png)

## 作成機能

DeepResearch で情報を収集した後、Canvas の作成機能を活用してこれらの情報を視覚的に整理し、スライド資料として形にしていきます。

Canvas の作成機能には目的に応じた様々なコンテンツが用意されており、それぞれがスライド作成の異なるフェーズをサポートします。

![gemini-app-canvas-creation-feature_03.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/Q50HXc9IE3nl.png)

レポート画面の右上に表示される **[作成]** ボタンをクリックすると、利用可能なコンテンツ一覧が表示されます。

![gemini-app-canvas-creation-feature_04.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/RbnP7hdEbUKx.png)

現在、以下の4種類のコンテンツが提供されています。

- ウェブページ
- インフォグラフィック
- テスト
- 音声概要

それぞれのコンテンツが持つ特徴と、スライド作成への活用方法を見ていきましょう。

### ウェブページ

**ウェブページ** は、収集した情報を体系的に整理し、インタラクティブなレポートとして表示します。

ウェブページを選択すると、DeepResearch で収集した情報を基に、Gemini が自動的にインタラクティブなレポートを作成します。  
見出し、本文、リスト、リンクなどが適切に配置され、内容に応じた構造化されたドキュメントが生成されます。

![gemini-app-canvas-creation-feature_05.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/0217Iwybqbpa.png)

このような構造化されたレポートは、スライドの各セクションの内容を詳細に記述したものとなり、スライド作成の元となる素材として活用できます。  
特に、スライドの骨格を構築するのに最適で、章立てや論理構造を明確にしたい場合に威力を発揮します。

せっかくなので、生成されたドキュメントの各セクションを見ていきましょう。

#### セクション：現状と課題

テキストは簡潔にまとめられており、箇条書きや見出しによって読みやすく構造化されています。

![gemini-app-canvas-creation-feature_06.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/kzwMkLHk5Oyv.png)

#### セクション：解決策

![gemini-app-canvas-creation-feature_07.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/E0wRJOH4XBA4.png)

#### セクション：ユースケース

![gemini-app-canvas-creation-feature_08.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/ZpswLKHPKHI1.png)

#### セクション：ロードマップ

ウェブページはインタラクティブな要素も持っています。

![gemini-app-canvas-creation-feature_09.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/1m2aUsb2yFLv.png)

例えば「DX初心者の中小企業様」をクリックすると、その対象に特化した情報が表示されるようになっています。

![gemini-app-canvas-creation-feature_10.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/w9UqBnn6RtF8.png)

#### セクション：成功への提言

![gemini-app-canvas-creation-feature_11.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/m2NBwLY9kXXQ.png)

こちらも同様にインタラクティブな要素を持っており、「行政機関への提言」をクリックすると、その対象に特化した提言内容が表示されます。

![gemini-app-canvas-creation-feature_12.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/m1Da8BUcYpZ7.png)

#### コード

ウェブページは、生成されたコンテンツのHTMLコードを直接確認・編集できます。

![gemini-app-canvas-creation-feature_13.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/mcdSLrOVNYbf.png)

これにより、レイアウトやスタイルを細かく調整したり、独自の要素を追加したりすることが可能です。  
また、このコードをエクスポートして他のウェブプラットフォームで活用することもできます。

### インフォグラフィック

**インフォグラフィック** は、複雑な情報や概念を視覚的に表現することができます。

インフォグラフィックを選択すると、DeepResearch で収集した情報を基に、Gemini が自動的にビジュアル要素を生成します。  
テキスト、アイコン、図形、矢印などが適切に配置され、情報の関連性や流れが視覚的に表現されます。

![gemini-app-canvas-creation-feature_14.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/FSyDIoUPu1ya.png)

この例では「沖縄DXとクラウドデータ基盤」のテーマに関するインフォグラフィックが生成されており、中心概念から派生する要素や関連性が視覚的に整理されています。

![gemini-app-canvas-creation-feature_15.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/UH5pGgI6mzrE.png)

スライド作成において最も直接的に活用できるコンテンツであり、核となる視覚素材を簡単に生成できます。

#### コード

インフォグラフィックもHTMLコードとして確認・編集が可能です。

![gemini-app-canvas-creation-feature_16.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/tCNB9qFsQn0f.png)

これにより、色やレイアウト、フォントなどを細かく調整して、スライドのデザインテーマに合わせたカスタマイズが可能です。

### テスト

**テスト** は、理解度確認のためのクイズやインタラクティブな要素をスライドに取り入れるための機能です。

テストを選択すると、DeepResearch で収集した情報を基に、Gemini が自動的に関連する質問と回答選択肢を生成します。  
この例では「沖縄のDX推進における最大の課題は何か？」という問いに対して、複数の選択肢が提示されています。

![gemini-app-canvas-creation-feature_17.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/ElV8TWURCJCo.png)

各問題には「ヒントを表示」機能も用意されており、聴衆が考えるためのガイドを提供することができます。

![gemini-app-canvas-creation-feature_18.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/vkVOPSbNaiQf.png)

正解時には解説が表示されます。

![gemini-app-canvas-creation-feature_19.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/3abLBAXy93UQ.png)

不正解の場合も同様に、解説が提供されます。

![gemini-app-canvas-creation-feature_20.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/o7DRzm3KOTWZ.png)

クイズ形式の質問は、スライドの中間部分や各セクションの終わりに挿入することで、聴衆の注意を引き戻し、重要ポイントの理解を深める効果が期待できます。

### 音声概要

**音声概要** は、テキスト情報を音声形式に変換し、要点を簡潔にまとめる機能です。

音声概要を選択すると、DeepResearch で収集した情報の要点が Gemini によって抽出され、ポッドキャスト風に紹介する音声データが作成されます。

![gemini-app-canvas-creation-feature_21.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/asFdrcG80TV9.png)

NotebookLM でもおなじみのこの機能は、スライドの発表練習やスクリプト作成に活用できます。  
Gemini が生成した音声を参考に、自分の発表スタイルを確立したり、重要なポイントを効果的に伝える方法を検討したりするのに役立ちます。

## ファイル一覧

Canvas 機能で作成したすべてのコンテンツは、クラウド上に保存され、いつでも簡単にアクセスすることができます。

画面右上のフォルダアイコンをクリックすると、これまでに作成したファイルの一覧が表示されます。  
ここでは、ウェブページ、インフォグラフィック、テスト、音声概要など、すべての作成物を管理することができます。

![gemini-app-canvas-creation-feature_22.png](https://devio2024-2-media.developers.io/upload/590ubZMRi2K0tjf06ObdL1/2025-06-11/egcximnWKgwx.png)

この一覧から過去の作成物を選択すると、編集を再開したり、新しいバージョンを作成したりすることが可能です。

スライド作成においては、異なるテーマやターゲット向けに複数のバージョンを準備しておき、必要に応じて適切なものを選択して利用することができそうですね。

## まとめ

今回は Gemini アプリの Canvas の作成機能に焦点を当てて、特にスライド作成における活用方法をご紹介しました。

**いかがだったでしょうか？**

ウェブページ、インフォグラフィック、テスト、音声概要という4つのコンテンツは、それぞれがスライド作成の異なるフェーズや目的をサポートする強力なツールであることがお分かりいただけたかと思います。

DeepResearch と組み合わせることで、情報収集から視覚的なスライド素材作成までをシームレスに行うことができます。

CloudNative Days Summer 2025 での登壇経験を振り返ると、「あの時この作成機能があれば！」と強く感じます。  
特にインフォグラフィック機能は、「クラウドデータ基盤で切り拓く沖縄DXの可能性」のような抽象的なテーマを視覚化するのに非常に役立ったのではないでしょうか。

今後の登壇や提案資料作成には、ぜひこの Canvas 機能を積極的に活用していきたいと思います。

みなさんも Gemini の Canvas 機能を試してみて、スライド作成の効率化にお役立てください！

## 参考リンク

- [Gemini公式サイト](https://gemini.google.com/)
- [Gemini アプリの機能アップデート](https://gemini.google.com/updates?hl=ja)
- [Canvas でドキュメントやアプリなどを作成する - パソコン - Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/16047321?hl=ja)
