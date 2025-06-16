---
title: GitHub - nishimoto265/Claude-Code-Communication
source: https://github.com/nishimoto265/Claude-Code-Communication
author:
- github.com
published: ''
fetched: '2025-06-10T08:48:20.489157+00:00'
tags:
- codex
- ai
image: https://opengraph.githubassets.com/03c0bdee4520a4ecd6f6d8ba348f9a42daaf719989b99eff4c61a6a2ea1bd5f9/nishimoto265/Claude-Code-Communication
---

## 要約

本リポジトリは **tmux** 上で複数エージェントが階層的にコミュニケーションするデモ環境を提供する。`setup.sh` でセッションを自動構築し、PRESIDENT セッションで認証後に multiagent 全ペインで `claude` を起動することで **PRESIDENT→boss1→workers** へ指示が伝達される。Workers は Hello World 実行と完了報告を行い、`agent-send.sh` により手動送信やログ確認も行える。セッション一覧表示や環境リセット手順も用意されており、簡単にデモを再現できる。

## 本文

# 🤖 Tmux Multi-Agent Communication Demo

Agent同士がやり取りするtmux環境のデモシステム

## 🎯 デモ概要

PRESIDENT → BOSS → Workers の階層型指示システムを体感できます

### 👥 エージェント構成

```
📊 PRESIDENT セッション (1ペイン)
└── PRESIDENT: プロジェクト統括責任者

📊 multiagent セッション (4ペイン)
├── boss1: チームリーダー
├── worker1: 実行担当者A
├── worker2: 実行担当者B
└── worker3: 実行担当者C
```

## 🚀 クイックスタート

### 0. リポジトリのクローン

```bash
git clone https://github.com/nishimoto265/Claude-Code-Communication.git
cd Claude-Code-Communication
```

### 1. tmux環境構築

⚠️ **注意**: 既存の `multiagent` と `president` セッションがある場合は自動的に削除されます。

```bash
./setup.sh
```

### 2. セッションアタッチ

```bash
# マルチエージェント確認
tmux attach-session -t multiagent

# プレジデント確認（別ターミナルで）
tmux attach-session -t president
```

### 3. Claude Code起動

**手順1: President認証**

```bash
# まずPRESIDENTで認証を実施
tmux send-keys -t president 'claude' C-m
```

認証プロンプトに従って許可を与えてください。

**手順2: Multiagent一括起動**

```bash
# 認証完了後、multiagentセッションを一括起動
for i in {0..3}; do tmux send-keys -t multiagent:0.$i 'claude' C-m; done
```

### 4. デモ実行

PRESIDENTセッションで直接入力：

```
あなたはpresidentです。指示書に従って
```

## 📜 指示書について

各エージェントの役割別指示書：

- **PRESIDENT**: `instructions/president.md`
- **boss1**: `instructions/boss.md`
- **worker1,2,3**: `instructions/worker.md`

**Claude Code参照**: `CLAUDE.md` でシステム構造を確認

**要点:**

- **PRESIDENT**: 「あなたはpresidentです。指示書に従って」→ boss1に指示送信
- **boss1**: PRESIDENT指示受信 → workers全員に指示 → 完了報告
- **workers**: Hello World実行 → 完了ファイル作成 → 最後の人が報告

## 🎬 期待される動作フロー

```
1. PRESIDENT → boss1: "あなたはboss1です。Hello World プロジェクト開始指示"
2. boss1 → workers: "あなたはworker[1-3]です。Hello World 作業開始"
3. workers → ./tmp/ファイル作成 → 最後のworker → boss1: "全員作業完了しました"
4. boss1 → PRESIDENT: "全員完了しました"
```

## 🔧 手動操作

### agent-send.shを使った送信

```bash
# 基本送信
./agent-send.sh [エージェント名] [メッセージ]

# 例
./agent-send.sh boss1 "緊急タスクです"
./agent-send.sh worker1 "作業完了しました"
./agent-send.sh president "最終報告です"

# エージェント一覧確認
./agent-send.sh --list
```

## 🧪 確認・デバッグ

### ログ確認

```bash
# 送信ログ確認
cat logs/send_log.txt

# 特定エージェントのログ
grep "boss1" logs/send_log.txt

# 完了ファイル確認
ls -la ./tmp/worker*_done.txt
```

### セッション状態確認

```bash
# セッション一覧
tmux list-sessions

# ペイン一覧
tmux list-panes -t multiagent
tmux list-panes -t president
```

## 🔄 環境リセット

```bash
# セッション削除
tmux kill-session -t multiagent
tmux kill-session -t president

# 完了ファイル削除
rm -f ./tmp/worker*_done.txt

# 再構築（自動クリア付き）
./setup.sh
```

---

🚀 **Agent Communication を体感してください！** 🤖✨
