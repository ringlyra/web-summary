# ルール
AGENTS.md → README.md → md template.md の順番で参照すること。

# エージェント指示: 長い行の出力をスマートに処理する

## コンテキスト
あなたは shell 内でコマンドを実行しています。この環境では **1 行が 1 600 byte を超えるとセッションが強制終了** されます。上限は厳格で、1 601 byte でもアウトです。
※AGENTS.md はここ(ルート上)にあるものだけで、サブディレクトリにはないので探しにいく必要はありません。

## 目標
1. **ハードエラーを防ぐ** — 物理 1 行が 1 600 byte を超えないようにする  
2. **ユーザ情報を守る** — 分割や外部保存をしてもデータを欠損させない  
3. **透明性を保つ** — 省略や分割、ファイル転送をした場合は簡潔に通知する

## 必須動作
- **行長ガード**  
  - 出力前に各行の UTF-8 バイト長を測定する  
  - `len(line_bytes) > 1 600` の場合は、何も送る前に以下のフォールバックを適用
- **フォールバック戦略**  
  1. *ソフトラップ*: `space`, `,`, `;` など安全な箇所に `\n` を挿入して 1 行 1 600 byte 以下に分割  
  2. *フォールド出力*: `fold -w 1600` または言語ネイティブの相当機能で折り返す  
  3. *ファイルリダイレクト*: 完全出力を一時ファイル（例: `out.txt`）に書き、パスを短く通知

## エラーログの例
以下のようなエラーが出ないように事前に対策する必要があります。
```
Error: Output for session 'shell' contained a line exceeding the max of 1600 bytes (observed at least 3184 bytes).

The byte sequence which exceeded the limit started with: b'<meta name="csrf-tok'

The exec session has been deleted. Please start a new session.

Tip - rerun the command and extract only what you need, e.g.:
  * grep -nE 'PATTERN' FILE | cut -c1-200
  * grep -o 'PATTERN' FILE
  * jq -r '.json.path' FILE
  * grep -a PATTERN FILE
```
