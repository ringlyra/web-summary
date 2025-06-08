<!-- metadata -->
- **title**: claude code でローカルなMCPサーバーを叩けるようにする
- **source**: https://zenn.dev/mizchi/articles/claude-local-mcp-server
- **author**: mizchi
- **published**: 2025-06-08T18:32:52.581+09:00
- **fetched**: 2025-06-08T16:17:46Z
- **tags**: codex, ai, typescript, mcp
- **image**: https://res.cloudinary.com/zenn/image/upload/s--miyzM-f0--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:claude%2520code%2520%25E3%2581%25A7%25E3%2583%25AD%25E3%2583%25BC%25E3%2582%25AB%25E3%2583%25AB%25E3%2581%25AAMCP%25E3%2582%25B5%25E3%2583%25BC%25E3%2583%2590%25E3%2583%25BC%25E3%2582%2592%25E5%258F%25A9%25E3%2581%2591%25E3%2582%258B%25E3%2582%2588%25E3%2581%2586%25E3%2581%25AB%25E3%2581%2599%25E3%2582%258B%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:mizchi%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2liclRHT052Z3d3ay1fNGxlcVk4TGNGSlNuX0FoWnpEWVlKaXJNcWc9czI1MC1j%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png

## 要約
claude code をローカルの MCP サーバーへ接続する方法を解説。Node 製サーバーで URL から本文を抽出して返すツール `read_url_content` を実装し、 `.claude/mcp.json` に設定。`claude --mcp-config` で CLI から利用でき、Deno 版や zshrc 用ラッパー `claudex` も紹介している。

## 本文
claude code 安くて便利。

自前 MCP を大量に持ってると、手元に用意しておいた MCP サーバーに繋ぎたくなります。

以下のドキュメントによると、 `claude --mcp-config=...` でローカルな MCP サーバーを叩けるみたいです。

<https://docs.anthropic.com/ja/docs/claude-code/settings>

以下、claude code に手元の MCP サーバーを登録する例です。

ローカル MCP につなぐ
-------------

MCP サーバー実装を書きます。

これは指定した URL を本文抽出して markdown で取得する実装です。

```
// .claude/mcp-server.ts
// npm add -D @modelcontextprotocol/sdk zod @mizchi/readability
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { extract, toMarkdown } from "@mizchi/readability";

const server = new McpServer({
  name: "deno",
  version: "1.0.0",
});

server.tool(
  "read_url_content",
  "与えられたURLの本文抽出で取得し、Markdown形式で返します。",
  { url: z.string().describe("URL") },
  async ({ url }) => {
    const html = await fetch(url).then((res) => res.text());
    const extracted = extract(html, { charThreshold: 100 });
    if (extracted.root) {
      const parsed = toMarkdown(extracted.root);
      return { content: [{ type: "text", text: parsed }] };
    } else {
      return {
        content: [
          {
            type: "text",
            text: `No content found at the provided URL. Return full html.\n${html}`,
          },
        ],
      };
    }
  }
);

try {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Local MCP Server running on stdio");
} catch (error) {
  console.error("Error starting MCP server:", error);
  process.exit(1);
}

```

特に変なことはしていません。

実行
--

これを標準入出力で読み込む設定の例

.claude/mcp.json

```
{
  "mcpServers": {
    "local": {
      "command": "node",
      "args": [".claude/mcp-server.ts"]
    }
  }
}

```

これは次のように読み込みます。

```
$ claude --mcp-config=.claude/mcp.json

```

実行例

```
> https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling を markdown で要約して

# 出力の抜粋

Tool use                                                │
│                                                         │
│   local:read_url_content(url: "https://ai-sdk.dev/doc   │
│   s/ai-sdk-core/tools-and-tool-calling") (MCP)          │
│   与えられたURLの本文抽出で取得し、Markdown形式で返し   │
│   ます。                                                │
│                                                         │
│ Do you want to proceed?                                 │
│ ❯ 1. Yes                                                │
│  2. Yes, and don't ask again for local:read_url_content │
│   commands in /home/mizchi/sandbox/claude-mcp           │
│                                                         │
│   3. No, and tell Claude what to do differently

  使用例

  import { generateText, tool } from 'ai';
  import { z } from 'zod';

  const result = await generateText({
    model: yourModel,
    tools: {
      weather: tool({
        description: '場所の天気を取得',
        parameters: z.object({
          location:
  z.string().describe('天気を取得する場所'),
        }),
        execute: async ({ location }) => ({
          location,
          temperature: 72 + Math.floor(Math.random() *
   21) - 10,
        }),
      }),
    },
    maxSteps: 5,
    toolChoice: 'required',
    prompt: 'サンフランシスコの天気は？',
  });

```

おまけ: deno 用
-----------

MCP サーバーはパーミッションを絞って起動したいので、自分は deno で書いてることが多いです。

サーバー実装は実装は node 互換モードでだいたい一緒なので略。

コマンド部分に `deno run -A --deny-env` 相当を渡します。

.claude/mcp.json

```
{
  "mcpServers": {
    "deno-local": {
      "command": "deno",
      "args": ["run", "-A", "--deny-env", ".claude/deno-server.ts"]
    }
  }
}

```

node 環境でも `.vscode/settings.json`の`deno.enablePaths` で `.claude/deno-server.ts` だけ Deno LSP を有効にします。

.vscode/settings.json

```
{
  "deno.enablePaths": [".claude/deno-server.ts"]
}

```

おまけ: zshrc 用の claudex コマンド
--------------------------

`.claude/mcp.json` がある場合、これを読み込むコマンドを作りました。

```
function claudex() {
    git_root=$(git rev-parse --show-toplevel 2>/dev/null)
    if [ -f "$git_root/.claude/mcp.json" ]; then
        claude --mcp-config="$git_root/.claude/mcp.json" "$@"
    else
        claude "$@"
    fi
}

```
