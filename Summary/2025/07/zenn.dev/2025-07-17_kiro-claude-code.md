---
title: 'KiroとClaude Codeの組み合わせで開発の質と速度を両取りできた'
source: https://zenn.dev/ubie_dev/articles/kiro-claude-code
author:
  - zenn.dev
published: ''
fetched: '2025-07-17T02:23:27.387235+00:00'
tags:
  - codex
  - zenn
image: https://res.cloudinary.com/zenn/image/upload/s--xpAYwKRm--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Kiro%25E3%2581%25A8Claude%2520Code%25E3%2581%25AE%25E7%25B5%2584%25E3%2581%25BF%25E5%2590%2588%25E3%2582%258F%25E3%2581%259B%25E3%2581%25A7%25E9%2596%258B%25E7%2599%25BA%25E3%2581%25AE%25E8%25B3%25AA%25E3%2581%25A8%25E9%2580%259F%25E5%25BA%25A6%25E3%2582%2592%25E4%25B8%25A1%25E5%258F%2596%25E3%2582%258A%25E3%2581%25A7%25E3%2581%258D%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_34:%25E9%25B9%25BF%25E9%2587%258E%2520%25E5%25A3%25AE%2Cx_220%2Cy_108/bo_3px_solid_rgb:d6e3ed%2Cg_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3plbm4tdXNlci11cGxvYWQvYXZhdGFyL2VlOWMzMWRhODMuanBlZw==%2Cr_20%2Cw_90%2Cx_92%2Cy_102/co_rgb:6e7b85%2Cg_south_west%2Cl_text:notosansjp-medium.otf_30:Ubie%2520%25E3%2583%2586%25E3%2583%2583%25E3%2582%25AF%25E3%2583%2596%25E3%2583%25AD%25E3%2582%25B0%2Cx_220%2Cy_160/bo_4px_solid_white%2Cg_south_west%2Ch_50%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2hwRUMxbUtjVjZsX01lT2R6N1Nsejk1SXR4WUZoYjB2LTNOdzNjV3c9czI1MC1j%2Cr_max%2Cw_50%2Cx_139%2Cy_84/v1627283836/default/og-base-w1200-v2.png
---

## 要約

**Kiro**は要件定義から設計書、タスクリストを自動生成するAmazon製IDEで、対話形式で詳細な仕様を作れる一方、実装が遅い。**Claude Code**は爆速だが、曖昧な指示だと失敗しやすく長い会話では情報を忘れがち。そこでKiroの設計書を基にタスクをClaude Codeに渡すと、指示が明確になり高品質かつ迅速な開発が実現した。記事では太陽系シミュレータ作成を例に、タスクファイルのパス指定をドラッグ&ドロップで行うコツも紹介。既存の開発環境を保ちながら新しいワークフローを組み込めるのも利点で、今後はKiroの速度向上に期待しつつ当面この組み合わせを利用するという。これにより開発効率が大きく向上したと述べている。

## 本文

* Kiroは対話形式で詳細な要件書・設計書を作れるが、実装速度が遅い
* Claude Codeは爆速開発ができるが、正確な指示出しが難しい

2つの長所を組み合わせることで、質と速度の両取りができました。

Kiroで作った仕様書をClaude Codeに読み込ませたら、Claude Codeがタスクを理解して最後まで実装してくれました。

<https://x.com/tonkotsuboy_com/status/1945410412016816322>

Kiroとは
======

Kiroとは2025年7月15日にAmazonがリリースした統合開発環境で、要件定義・設計からコードの開発までを行ってくれます。対話形式で詳細なrequirements（機能要件）・design（設計）・tasks（タスクリスト）を作成できます。作られたタスクを実行することで、開発が完了します。

詳しくは次の記事がわかりやすいです。

<https://zenn.dev/sesere/articles/31d4b460c949e5>

<https://kiro.dev/blog/introducing-kiro/>

Kiroは設計は得意だが、実装速度が遅い
====================

Kiroは高機能な要件定義・設計機能は持っていますが、現時点では実装速度が遅いです。今開発の現場で標準的に使われているClaude Codeは、実装速度が高速です。一方で、曖昧な指示だと手戻りが発生しがちで、詳細な仕様がないと期待と異なる実装になる傾向があります。また、長い会話の中では初期の内容を忘れることもしばしばあります。

であれば、Kiroの要件定義・設計機能とClaude Codeの実装速度を組み合わせれば、詳細な設計書を元にした期待値どおりの高速な開発ができるのではないかと思いました。

また、Kiro自体は魅力なのですが、Claude Codeで築き上げた開発環境（速度・コードの品質・MCPをはじめとする周辺ツール・hooksやカスタムスラッシュコマンドなどの豊富な機能）を手放したくなく、Claude Codeは使い続けたいと考えていたことも、今回の組み合わせに至った理由でもあります。

実際にプロジェクトで試してみた
===============

実際に、簡単な太陽系シミュレータを作りながら、KiroとClaude Codeの組み合わせの検証を行いました。

1. 要件書（requirements.md）の作成
--------------------------

Kiroに次のように呼びかけます。  
「太陽系の惑星の公転をシミュレーションできるツールを作りたい。3D表現で。各惑星をクリックすると、その惑星の情報が表示される形にして。」

Kiroが要件書をrequirements.mdとして作成します。

![](https://res.cloudinary.com/zenn/image/fetch/s--XsSRva5k--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/c98c7e3d48b7e83887f2245c.png%3Fsha%3D65808e801ea9a7b9baee55cf912f97374207e3f8)

実際に作られた要件書は次のとおりです。気に入らないところがあれば、対話しながら修正できます。

実際に作成された要件書（クリックで展開）

```
# 要件文書

## 概要

太陽系の惑星の公転を3Dで視覚化し、インタラクティブに探索できるシミュレーションツールです。ユーザーは惑星をクリックして詳細情報を表示でき、リアルタイムで公転運動を観察できます。

## 要件

### 要件 1

**ユーザーストーリー:** 教育者として、太陽系の惑星の公転運動を3Dで視覚化したいので、学生に天体の動きを直感的に理解してもらえる

#### 受入基準

1. WHEN アプリケーションが起動される THEN システムは太陽系の3D表現を表示する SHALL
2. WHEN 3D表示が読み込まれる THEN システムは太陽、水星、金星、地球、火星、木星、土星、天王星、海王星を正確な相対位置に配置する SHALL
3. WHEN シミュレーションが開始される THEN システムは各惑星を実際の公転周期に基づいた相対速度で公転させる SHALL

### 要件 2

**ユーザーストーリー:** ユーザーとして、惑星をクリックして詳細情報を見たいので、各天体について学習できる

#### 受入基準

1. WHEN ユーザーが惑星をクリックする THEN システムは選択された惑星の詳細情報パネルを表示する SHALL
2. WHEN 詳細情報パネルが表示される THEN システムは惑星名、直径、質量、公転周期、自転周期、太陽からの距離を表示する SHALL
3. WHEN ユーザーが情報パネル外をクリックする THEN システムは詳細情報パネルを閉じる SHALL

### 要件 3

**ユーザーストーリー:** ユーザーとして、3D空間を自由に操作したいので、異なる角度から太陽系を観察できる

#### 受入基準

1. WHEN ユーザーがマウスをドラッグする THEN システムはカメラの視点を回転させる SHALL
2. WHEN ユーザーがマウスホイールを操作する THEN システムはズームイン・ズームアウトを実行する SHALL
3. WHEN ユーザーが右クリックドラッグする THEN システムはカメラの位置をパンする SHALL

### 要件 4

**ユーザーストーリー:** ユーザーとして、シミュレーションの速度を制御したいので、観察に適したペースで惑星の動きを見られる

#### 受入基準

1. WHEN ユーザーが再生/一時停止ボタンをクリックする THEN システムはシミュレーションを開始または停止する SHALL
2. WHEN ユーザーが速度スライダーを調整する THEN システムは公転速度を0.1倍から10倍の範囲で変更する SHALL
3. WHEN ユーザーがリセットボタンをクリックする THEN システムは全ての惑星を初期位置に戻す SHALL

### 要件 5

**ユーザーストーリー:** ユーザーとして、視覚的に美しい表現を見たいので、学習体験を向上させられる

#### 受入基準

1. WHEN 3Dシーンが描画される THEN システムは各惑星に実際の色と質感に近いテクスチャを適用する SHALL
2. WHEN 太陽が表示される THEN システムは発光効果を適用して光源として表現する SHALL
3. WHEN 惑星が公転する THEN システムは軌道の軌跡を薄い線で表示する SHALL
4. WHEN シーンが描画される THEN システムは星空の背景を表示する SHALL

### 要件 6

**ユーザーストーリー:** ユーザーとして、レスポンシブなWebアプリケーションを使いたいので、様々なデバイスで利用できる

#### 受入基準

1. WHEN アプリケーションがデスクトップブラウザで開かれる THEN システムは全機能を提供する SHALL
2. WHEN アプリケーションがタブレットで開かれる THEN システムはタッチ操作に対応した3D操作を提供する SHALL
3. WHEN ウィンドウサイズが変更される THEN システムは3Dビューポートを適切にリサイズする SHALL

```

実装詳細
----

### アニメーションループ

requestAnimationFrame を使用してスムーズなアニメーションを実現

### 座標変換

* 論理座標系（天文単位）から画面座標系への変換
* ズーム・パン機能に対応した座標計算

### パフォーマンス最適化

* 画面外の惑星は描画をスキップ
* アニメーション速度に応じた描画頻度調整

2. 設計書（design.md）の作成
--------------------

次に、設計書が作成されます。設計書も対話形式で調整可能です。

![](https://res.cloudinary.com/zenn/image/fetch/s--EtZSEb0_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/fd7193b68f6b5011eb53e937.png%3Fsha%3D945d719cb2d27d59bf7eb20e4f2c7ea16afe8ba5)

実際に作成された設計書（クリックで展開）

```
# 設計文書

## 概要

Next.jsベースの太陽系シミュレーションWebアプリケーションです。Three.jsを使用した3D描画、React Contextによる状態管理、Vitestによるテスト環境を構築します。レスポンシブデザインでデスクトップとタブレットの両方に対応します。

## アーキテクチャ

### 技術スタック
- **フレームワーク**: Next.js 14 (App Router)
- **3Dライブラリ**: Three.js + React Three Fiber
- **状態管理**: React Context + useReducer
- **スタイリング**: Tailwind CSS
- **テスト**: Vitest + React Testing Library
- **型安全性**: TypeScript

### アプリケーション構造

src/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # ルートレイアウト
│   └── page.tsx           # メインページ
├── components/            # Reactコンポーネント
│   ├── ui/               # UI基本コンポーネント
│   ├── solar-system/     # 太陽系関連コンポーネント
│   └── controls/         # 制御UI
├── hooks/                # カスタムフック
├── lib/                  # ユーティリティ
├── types/                # TypeScript型定義
└── data/                 # 惑星データ


## コンポーネントとインターフェース

### 主要コンポーネント

#### 1. SolarSystemSimulator
- メインコンテナコンポーネント
- 3Dシーンとコントロールパネルを統合
- シミュレーション状態を管理

#### 2. Scene3D
- Three.js/React Three Fiberによる3D描画
- カメラ制御、ライティング、レンダリング
- 惑星とその軌道の描画

#### 3. Planet
- 個別の惑星コンポーネント
- クリックイベント処理
- テクスチャとマテリアル適用

#### 4. ControlPanel
- 再生/一時停止、速度調整、リセット
- シミュレーション制御UI

#### 5. PlanetInfoPanel
- 選択された惑星の詳細情報表示
- モーダル形式での情報表示

### インターフェース定義

typescript
interface Planet {
  id: string;
  name: string;
  nameJa: string;
  radius: number;
  distance: number;
  orbitalPeriod: number;
  rotationPeriod: number;
  mass: number;
  color: string;
  textureUrl: string;
  description: string;
}

interface SimulationState {
  isPlaying: boolean;
  speed: number;
  time: number;
  selectedPlanet: Planet | null;
}

interface CameraControls {
  position: [number, number, number];
  target: [number, number, number];
  zoom: number;
}


## データモデル

### 惑星データ

実際の天体データに基づいた惑星情報：

- 軌道半径（天文単位）
- 公転周期（地球日）
- 自転周期（時間）
- 質量（地球質量比）
- 物理的特性（半径、色、テクスチャ）

### 状態管理

React ContextとuseReducerを使用：

- SimulationContext: シミュレーション状態
- CameraContext: 3Dカメラ制御
- UIContext: UI状態（パネル表示など）

## エラーハンドリング

### 3D描画エラー

- WebGL非対応ブラウザの検出
- フォールバック表示の提供
- エラーバウンダリによる例外処理

### リソース読み込みエラー

- テクスチャ読み込み失敗時のデフォルト表示
- 段階的な機能低下（Progressive Enhancement）

### パフォーマンス最適化

- LOD（Level of Detail）による描画最適化
- フレームレート監視とパフォーマンス調整
- メモリ使用量の監視

## テスト戦略

### 単体テスト（Vitest）

- ユーティリティ関数のテスト
- 惑星データ計算ロジックのテスト
- 状態管理ロジックのテスト

### コンポーネントテスト（React Testing Library）

- UI コンポーネントの描画テスト
- ユーザーインタラクションのテスト
- 状態変更の検証

### 統合テスト

- シミュレーション全体の動作テスト
- 3D描画とUI連携のテスト

### E2Eテスト考慮事項

- 3D描画の検証は困難なため、主要なユーザーフローに焦点
- 惑星クリック → 情報表示の流れ
- コントロールパネルの操作

## 実装詳細

### 3D描画最適化

- インスタンス化による描画パフォーマンス向上
- シェーダーによるカスタム効果
- アニメーションループの最適化

### レスポンシブ対応

- Tailwind CSSによるレスポンシブレイアウト
- タッチデバイス向けのジェスチャー対応
- 画面サイズに応じたUI調整

### アクセシビリティ

- キーボードナビゲーション対応
- スクリーンリーダー対応
- 色覚異常への配慮

## パフォーマンス考慮事項

### 描画最適化

- フレームレート60fps維持
- GPU使用率の監視
- バッテリー消費の最小化

### メモリ管理

- テクスチャの適切な解放
- 不要なオブジェクトのクリーンアップ
- メモリリークの防止

### 読み込み最適化

- 段階的なリソース読み込み
- プリローディング戦略
- 圧縮テクスチャの使用


```

3. 実装計画（task.md）の作成
-------------------

最後に実装計画が作られます。こちらも対話形式で調整可能です。

![](https://res.cloudinary.com/zenn/image/fetch/s--XlyhH1h7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/9919a24253d4964046389d93.png%3Fsha%3De170b59176bf5e93c4e77cdb53872dca5e3e2527)

実際に作成された実装計画（クリックで展開）

```
# 実装計画

- [ ] 1. プロジェクト基盤とセットアップ
  - Next.js 14プロジェクトを作成し、必要な依存関係をインストール
  - TypeScript、Tailwind CSS、Vitestの設定を完了
  - 基本的なディレクトリ構造を作成
  - _要件: 6.1, 6.3_

- [ ] 2. 型定義とデータモデルの実装
  - Planet、SimulationState、CameraControlsインターフェースを定義
  - 惑星データの型安全な定義を作成
  - _要件: 1.2, 2.2_

- [ ] 3. 惑星データの作成と検証
  - 太陽系9天体の正確なデータを含むデータファイルを作成
  - 惑星データの妥当性検証関数を実装
  - データ取得用のユーティリティ関数を作成
  - _要件: 1.2, 2.2_

- [ ] 4. 基本的な3Dシーンのセットアップ
  - React Three Fiberを使用した基本的な3Dシーンコンポーネントを作成
  - カメラ、ライティング、レンダラーの初期設定を実装
  - 太陽を中心とした基本的なシーンを構築
  - _要件: 1.1, 5.2_

- [ ] 5. 惑星コンポーネントの実装
  - 個別の惑星を描画するPlanetコンポーネントを作成
  - 惑星の基本的な球体ジオメトリとマテリアルを実装
  - 惑星の相対サイズと位置の計算ロジックを実装
  - _要件: 1.2, 5.1_

- [ ] 6. 公転アニメーションの実装
  - 時間ベースの公転計算ロジックを実装
  - 各惑星の公転周期に基づいた相対速度計算を作成
  - アニメーションループとフレーム更新を実装
  - _要件: 1.3_

- [ ] 7. カメラ制御の実装
  - マウスドラッグによるカメラ回転機能を実装
  - マウスホイールによるズーム機能を実装
  - 右クリックドラッグによるパン機能を実装
  - _要件: 3.1, 3.2, 3.3_

- [ ] 8. 惑星クリック検出と情報表示
  - 3D空間での惑星クリック検出を実装
  - 選択された惑星の状態管理を実装
  - 惑星詳細情報パネルコンポーネントを作成
  - 情報パネルの表示/非表示制御を実装
  - _要件: 2.1, 2.2, 2.3_

- [ ] 9. シミュレーション制御UIの実装
  - 再生/一時停止ボタンコンポーネントを作成
  - 速度調整スライダーコンポーネントを実装
  - リセットボタン機能を実装
  - コントロールパネルのレイアウトを作成
  - _要件: 4.1, 4.2, 4.3_

- [ ] 10. 状態管理システムの実装
  - SimulationContextとプロバイダーを作成
  - useReducerを使用したシミュレーション状態管理を実装
  - 状態変更アクションとリデューサーを定義
  - _要件: 4.1, 4.2, 4.3_

- [ ] 11. 視覚効果の実装
  - 惑星テクスチャの読み込みと適用を実装
  - 太陽の発光効果を実装
  - 軌道軌跡の描画機能を実装
  - 星空背景の実装
  - _要件: 5.1, 5.2, 5.3, 5.4_

- [ ] 12. レスポンシブ対応の実装
  - タッチデバイス向けのジェスチャー制御を実装
  - 画面サイズに応じたレイアウト調整を実装
  - ビューポートリサイズ処理を実装
  - _要件: 6.2, 6.3_

- [ ] 13. エラーハンドリングの実装
  - WebGL非対応ブラウザの検出とフォールバック表示を実装
  - テクスチャ読み込み失敗時の処理を実装
  - エラーバウンダリコンポーネントを作成
  - _要件: 6.1_

- [ ] 14. パフォーマンス最適化
  - フレームレート監視機能を実装
  - LOD（Level of Detail）による描画最適化を実装
  - メモリ使用量の監視と最適化を実装
  - _要件: 1.3, 5.1_

- [ ] 15. テストの実装
  - 惑星データ計算ロジックの単体テストを作成
  - 状態管理ロジックの単体テストを作成
  - UIコンポーネントのテストを作成
  - シミュレーション統合テストを作成
  - _要件: 全要件の検証_

- [ ] 16. 最終統合とポリッシュ
  - 全コンポーネントの統合とテスト
  - UI/UXの最終調整
  - パフォーマンスの最終最適化
  - アクセシビリティ対応の確認
  - _要件: 全要件の最終検証_


```

作成した設計書をClaude Codeに渡して実装を命令する
==============================

今回のポイントです。Kiroで作成した設計書をClaude Codeに渡します。具体的には次のように渡しました。

「（tasks.mdへのパス）にしたがって実装して。必要であればdesign.mdやrequirement.mdも参照して。」（tasks.mdへのパス）のところは、「/Users/takeshi.kano/git/github.com/tonkotsuboy/solar-system-simulator/.kiro/specs/solar-system-simulator/tasks.md」といったパスになります。

![](https://res.cloudinary.com/zenn/image/fetch/s--V4mpbMAs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/4c7a4bbbff62452a37c8c6d1.png%3Fsha%3D2324a701365f8f527d472db63f24fb6a06092ee6)

パスの指定方法について、Claude Codeには `@` を使ってファイルパスを参照する機能があるのですが、Kiroの設計書が格納されている`.kiro`フォルダのような `.`始まりのパスは対応していないようです。そこで、私はtasks.mdをターミナルにドラッグ&ドロップして、パスをコピーして渡すようにしています。

![](https://res.cloudinary.com/zenn/image/fetch/s--C4OJJCrl--/https://storage.googleapis.com/zenn-user-upload/deployed-images/9ff7b286a7545bcf9a55b554.webp%3Fsha%3Df8bfedfec32320469aa0ad51de07591a17a3d5ef)

Kiroで作った実装計画（tasks.md）をClaude Codeに渡すと、Claude Codeはその実装計画にしたがって実装を開始します。

![](https://res.cloudinary.com/zenn/image/fetch/s--0lMeQbDt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/078ad92f16ebf9d2aa073600.png%3Fsha%3D79c2c03cdd5cdda9b683eef8882b145af2f17c70)

最後に
===

KiroとClaude Codeの役割を改めて整理すると次のとおりです。

| フェーズ | Kiro | Claude Code |
| --- | --- | --- |
| 要件定義 | ◎ 対話形式で詳細化 | △ 曖昧な要件は苦手 |
| 設計 | ◎ 高品質な設計書作成 | ○ 設計書があれば実装方針決定可 |
| 実装 | △ 時間がかかる | ◎ 爆速 |

Kiroのおかげで、AIに命令する際の要件を明確にできるようになり、かつClaude Codeのおかげでその要件に沿った高速開発が可能になりました。しばらくはこの組み合わせを使っていくことになりそうです。余談ですが、筆者はKiroのIDEを使うのは要件定義・設計のところまでで、その後の工程はターミナル（Warp）を使ったり、Cursorを使ったりしています。また、Kiroが遅いのはあくまで現時点の話です。今後のアップデートによって、速度は改善されていくことでしょう。

参考記事
====

<https://kiro.dev/blog/introducing-kiro/>

<https://zenn.dev/sesere/articles/31d4b460c949e5>