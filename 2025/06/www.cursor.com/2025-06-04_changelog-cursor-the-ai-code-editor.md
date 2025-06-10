<!-- metadata -->
- **title**: Changelog | Cursor - The AI Code Editor
- **source**: https://www.cursor.com/ja/changelog
- **author**: cursor.com
- **published**: 2025-06-04T00:00:00Z
- **fetched**: 2025-06-04T23:40:48Z
- **tags**: codex, ai, changelog, code, editor
- **image**: https://www.cursor.com/_next/static/media/opengraph-image.375711d3.png

## 要約
AIコードエディタCursorの更新履歴。最新版1.0では、PRを自動レビューする**BugBot**、会話内容を記憶する**Memories**、クラウドでの作業を自動化する**Background Agent**、Jupyter Notebook対応、MCPワンクリック設定などを追加。チャット内の可視化、ダッシュボード刷新、価格体系の統一と**Max Mode**導入など、多数の改善が実施された。

## 本文 / Article
Cursor 1.0 is here!

This release brings BugBot for code review, a first look at memories, one-click MCP setup, Jupyter support and general availability of Background Agent.

### Automatic code review with BugBot

BugBot automatically reviews your PRs and catches potential bugs and issues.

When an issue is found, BugBot leaves a comment on your PRs in GitHub. You can click "***Fix in Cursor***" to move back to the editor with a pre-filled prompt to fix the issue.

To set it up, follow instructions in our [BugBot docs](https://docs.cursor.com/bugbot)

[Your browser does not support the video tag.](https://www.cursor.com/changelog/1-0/bug-bot-web.mp4)

### Background Agent for everyone

Since we released Background Agent, our remote coding agent, in early access a few weeks ago, the early signals we've been seeing have been positive.

We're now excited to expand Background Agent to all users! You can start using it right away by clicking the cloud icon in chat or hitting `Cmd/Ctrl+E` if you have privacy mode disabled. For users with privacy mode enabled - we'll soon have a way to enable it for you too!

### Agent in Jupyter Notebooks

Cursor can now implement changes in Jupyter Notebooks!

Agent will now create and edit multiple cells directly inside of Jupyter, a significant improvement for research and data science tasks. Only supported with Sonnet models to start.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/1-0/jupyter-notebooks-web.mp4)

### Memories

With Memories, Cursor can remember facts from conversations and reference them in the future. Memories are stored per project on an individual level, and can be managed from Settings.

We're rolling out Memories as a beta feature. To get started, enable from Settings → Rules.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/1-0/memories-web.mp4)

### MCP one-click install and OAuth support

You can now set up MCP servers in Cursor with one click and together with OAuth support, you can easily authenticate servers that support it.

We've curated a short list of official MCP servers you can add to Cursor at [docs.cursor.com/tools](https://docs.cursor.com/tools).

If you're an MCP developer, you can easily make your server available to developers by adding a *Add to Cursor* button in your documentation and READMEs. Generate one at [docs.cursor.com/deeplinks](https://docs.cursor.com/deeplinks)

[Your browser does not support the video tag.](https://www.cursor.com/changelog/1-0/mcp-one-click.mp4)

### Richer Chat responses

Cursor can now render visualizations inside of a conversation. In particular, Mermaid diagrams and Markdown tables can now be generated and viewed in the same place!

[Your browser does not support the video tag.](https://www.cursor.com/changelog/1-0/mermaid-web.mp4)

[Your browser does not support the video tag.](https://www.cursor.com/changelog/1-0/markdown-web.mp4)

### New Settings and Dashboard

The setting and dashboard page have gotten some polish with this release.

With the new Dashboard, you can view your individual or team's usage analytics, update your display name, and view detailed statistics broken down by tool or model.

Keyboard (1)

* Open Background Agent control panel with `Cmd/Ctrl+E`

Improvements (4)

* `@Link` and web search can now parse PDFs and include in context
* Network diagnostics in settings to verify connectivity
* Faster responses with parallel tool calls
* Collapsable tool calls in Chat

Account (3)

* Enterprise users can only access stable release (no pre-release)
* Team admins can now disable Privacy Mode
* [Admin API for teams](https://docs.cursor.com/account/teams/admin-api) to access usage metrics and spend data

Introducing unified request-based pricing, Max Mode for all top models, and Background Agent for parallel task execution. Plus, improved context management with `@folders` support, refreshed Inline Edit with new options, faster file edits, multi-root workspace support, and enhanced chat features including export and duplication.

### Simpler, unified pricing

We've heard your feedback and are rolling out a unified pricing model to make it less confusing. Here's how it works:

* All model usage is now unified into request-based pricing
* Max mode now uses token-based pricing (similar to how models API pricing works)
* Premium tool calls and long context mode are removed to keep it simple

Quotas on [plans](https://www.cursor.com/pricing) Hobby, Pro and Business has not changed and slow requests are still included in the plans. All usage can be found in your [dashboard](https://cursor.com/dashboard) to help you track and manage your spend.

### Max Mode for all top models

Max Mode is now available for all state-of-the-art models in Cursor, with a simpler token-based pricing model. It's designed to give you full control when you need it most. You can enable it from the model picker to see which models support it. When new models roll out, Max Mode will be how we deliver their full capabilities from day one.

It's ideal for your hardest problems when you need more context, intelligence and tool use. For everything else, normal mode is still recommended with the same capabilities you're used to.

The pricing is straightforward: you're charged based on token usage. If you've used any CLI-based coding tool, Max mode will feel like that - but right in Cursor.

> Note: If you're using an older version of Cursor, you'll still have access to the previous MAX versions and long context mode for a few weeks. However, these features will be sunset soon, so we recommend updating to continue using these capabilities.

Read more about Max Mode in our [documentation](https://docs.cursor.com/context/max-mode)

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/max-mode.mp4)

### New Tab model

We've trained a new Tab model that now can suggest changes across multiple files. The model excels particularly at refactors, edit chains, multi file changes, and jumping between related code. You'll also notice it feels more natural and snappier in day-to-day use.

With this we've also added syntax highlighting to the completion suggestions.

### Background Agent Preview

In early preview, rolling out gradually: Cursor agents can now run in the background! To try it, head to Settings > Beta > Background Agent.

This allows you to run many agents in parallel and have them tackle bigger tasks. The agents run in their own remote environments. At any point, you can view the status, send a follow-up, or take over.

We're curious to hear what you think. While it is still early, we've found background agents useful internally for fixing nits, doing investigations, and writing first drafts of medium-sized PRs. Read more at [docs.cursor.com/background-agent](https://docs.cursor.com/background-agent).

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/bg.mp4)

### Include your entire codebase in context

You can now use `@folders` to add your entire codebase into context, just make sure to enable `Full folder contents` from settings. If a folder (or file) is too large to be included, you'll see a small icon on the context pill indicating this.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/root.mp4)

### Refreshed Inline Edit (Cmd/Ctrl+K) with Agent integration

Inline Edit (Cmd/Ctrl+K) has gotten a UI refresh and new options for full file edits (⌘⇧⏎) and sending to agent (⌘L)

Full file makes it easy to do scope changes to a file without using agent. However, you might come across cases where you're working with a piece of code you want to make multi-file edits to or simply just want more control you can get from agent. That's when you want to send selected codeblock to agent and keep on editing from there.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/cmdk.mp4)

### Fast edits for long files with Agent

We've added a new tool to the agent that will search & replace code in files, making it much more efficient for long files. Instead of reading the complete file, Agent can now find the exact place where edits should occur and change only that part. Here's an example editing a file in [Postgres codebase](https://github.com/postgres/postgres/blob/master/src/backend/tcop/postgres.c) where using search & replace tool is nearly double as fast. We're rolling this out to Anthropic models first and will expand to other models soon.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/search-n-replace.mov)

### Work in multiple codebases with workspaces

Now you can create multi-root workspaces to make multiple codebases available to Cursor. All of them will be indexed and available to Cursor, ideal when you have projects in different folders you want to work on in the same space.

`.cursor/rules` are supported in all folders added

### Working with Chat

#### Exporting Chat

You can now export chats to markdown from the chat view. Text and code blocks are included in the final export.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/export-chat.mp4)

#### Duplicate Chats

Exploring different paths from a conversation while preserving the existing is now possible with chat duplication. Go to a message and start a new chat from the three dots menu.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/050/duplicate-chat.mp4)

Keybindings (1)

* Full file edits from Inline Edit: `Cmd/Ctrl+Shift+K`

Improvements (11)

* Agent now uses native terminal emulation instead of simulated terminals
* `@folders` will now try to include all files that fit in context
* Icons for context state in Chat to tell you if files were not included or condensed
* Individual MCP tools can now be disabled from MCP settings
* New C# extension available in marketplace
* Chat font size can now be increased in settings
* Detailed in-app changelog

**MCP**

* Run stdio from remote workspace (WSL, Remote SSH)
* Streamable HTTP support
* Fixed leaking SSE server connections
* More reliable refreshing when changing config

Account (1)

* Removed 10 free requests/day for Claude 3 Opus

Patches (7)

**0.50.1**

* Background Agent availability

**0.50.2**

* Fixed keyboard navigation in Jupyter notebooks
* Fixed Custom mode models MAX and selection issues
* Improved indexing reliability for single-root workspaces
* Fixed VPN reliability with ZScaler

**0.50.3**

**0.50.4**

* Improved apply reliability
* Fixed Windows horizontal scrolling bug
* MCP improvements
* Improved multiroot workspace support

**0.50.5**

* Fixed chat pill not updating when switching files

**0.50.6**

* Fixed search & replace reliability issues
* Fixed checkpoint reliability issues
* Improved indexing
* Improved Python extension

**0.50.7**

* Fixed search & replace bug for Windows

### Automated and improved rules

You can now generate rules directly from a conversation using the `/Generate Cursor Rules` command. This is useful when you want to capture the existing context of a conversation to reuse later.

For `Auto Attached` rules with path patterns defined, Agent will now automatically apply the right rules when reading or writing files

We’ve also fixed a long-standing issue where `Always` attached rules now persist across longer conversations. Agent can now also edit rules reliably.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/049/generate-rules.mp4)

### More accessible history

Chat history has moved into the command palette. You can access it from the "Show history button" in Chat as well as through the `Show Chat History` command

### Making reviews easier

Reviewing agent generated code is now easier with a built-in diff view at the end of each conversation. You'll find the `Review changes` button at the bottom of chat after a message from the agent.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/049/review-ui.mp4)

### Images in MCP

You can now pass images as part of the context in MCP servers. This helps when screenshots, UI mocks, or diagrams add essential context to a question or prompt.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/049/mcp-image.mp4)

### Improved agent terminal control

We've added more control for you over terminals started by the agent. Commands can now be edited before they run, or skipped entirely. We've also renamed "Pop-out" to "Move to background" to better reflect what it does.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/049/agent-terminal.mp4)

### Global ignore files

You can now define [global ignore](https://docs.cursor.com/context/ignore-files) patterns that apply across all projects via your user-level settings. This keeps noisy or sensitive files like build outputs or secrets out of prompts, without needing per-project configuration.

### New models

We've recently added many more [models](https://docs.cursor.com/settings/models) you can use. Try out Gemini 2.5 Pro, Gemini 2.5 Flash, Grok 3, Grok 3 Mini, GPT-4.1, o3 and o4-mini from model settings.

### Project structure in context Beta

We’re introducing an option to include project structure in context, which adds your directory structure to the prompt. The agent now gets a clearer sense of how your project is organized, which improves suggestions and navigation of large or nested monorepos.

Keybindings (2)

* Some `CMD+K` shortcuts are now remappable
* Emacs keybinding extensions now work reliably

Improvements (5)

* Simplified model picker UI for Auto-select
* New interface for command palette
* Refreshed UI for Tab jump suggestions. Suggestions outside viewport are now clickable
* Tooltips for modes in Chat
* MCP stability
* You can now connect to AWS Bedrock using access keys and secret keys
* Git > @PR has now been renamed to @Branch

Fixes (4)

* Always-attached rules now persist correctly across summarization
* Rules in `.mdc` files can now be created and edited without issue by agent
* Fixed selection issues with `@mention` nodes at the start of the input box
* Performance in core editor

Business / Teams (4)

**Global ignore traversal**

* Cursor can now traverse up directory trees to find ignore files. This behavior is off by default and can be enabled from admin settings.

**IAM roles for Bedrock**

* Enterprises can now connect to AWS Bedrock using IAM roles

**User-level usage insights**

* Admins can now view per-user spend and fast request usage directly from the dashboard.

**Auto-run controls for teams**

* Admins can configure global MCP settings from dashboard.

Patches (6)

**0.49.1**

Prerelease

* Fixed Cursor Rules editor for Remote SSH
* Fixed UI delimiter display in zsh terminal in Chat
* Fixed "max length" warning showing incorrectly for rules under size limit
* Fixed "message too large" warning appearing in empty chats

**0.49.2**

Prerelease

* Improved rule generation apply
* Improved caching for user prompts
* Improved client metric handling

**0.49.3**

Prerelease

* Fixed issue with loading chat

**0.49.4**

Prerelease

* Fixed Neovim chat keybindings
* Improved indexing debug logs
* Fixed `.cursorignore` issue preventing chat submission on Windows

**0.49.5**

* Improved client reliability

**0.49.6**

* Fixed possibly broken codeblocks in old chats
* Fixed loading state issue in old chats
* Fixed chat message rendering issue
* Improved folders parsing

This release introduces chat tabs for parallel conversations, a redesigned
modes system with custom modes, and improvements to cost visibility, indexing
performance, and MCP reliability. Additionally, a sound notification plays when a chat is finished

### Built-in modes & custom modes (beta)

Agent and Ask modes are the built-in modes in Cursor, now with the option to add custom modes. We've also renamed "Edit" to "Manual" to better reflect its behavior.

Ask mode now has access to all search tools by default, so the `@Codebase` tool has been removed. It will automatically search the codebase when needed. If you want to force a search, simply ask Cursor in natural language to "search the codebase". You can disable search from Ask in the mode menu, which will result in Ask only seeing the context you have provided.

Read more about [Agent](https://docs.cursor.com/chat/agent) and [Ask](https://docs.cursor.com/chat/ask).

**Custom modes** (beta) allow you to compose new modes with tools and prompts that fit your workflow. Since custom modes can have custom keybindings, **⌘I will default to Agent mode** and **⌘L** will toggle the side pane. If you unbind ⌘I, it will also toggle the side pane. Custom modes are currently in beta, and you can enable them from Settings → Features → Chat → Custom modes.

You can also set the default mode from settings (Settings → Features → Chat → Default chat mode) to one of your modes or to the one you used most recently.

Read more about [custom modes](https://docs.cursor.com/chat/custom-modes).

### Chat tabs

Create new tabs (⌘T) in chat to have multiple conversations in parallel. You can also hold Option and click the + button to create a new tab. Cmd+N still creates a new chat in the current tab

When a tab is awaiting your input, you'll see an orange dot on that tab.

[Your browser does not support the video tag.](https://www.cursor.com/changelog/048/chat-tabs.mp4)

### Faster indexing

We've made significant improvements to indexing performance of similar codebases within a team, greatly reducing the initial indexing time for subsequent copies of large repositories after one copy has been fully indexed. For example, the Cursor codebase now indexes in under a minute, previously taking around 20 minutes.

### Sound notification (beta)

Cursor can now play a sound when a chat is ready for review. Enable this feature from Settings → Features → Chat → Play sound on finish.

### Usage-based cost visibility

For usage-based models, you can now view the cost and breakdown per chat from the history.

### New onboarding

We've introduced an easier onboarding process to help you get started with Cursor. You'll be guided through importing settings, selecting themes, keybindings, and other preferences.

Other (6)

* Improved indexing performance for teams sharing codebases
* The vertical sidebar option will temporarily be unavailable for users who opted into Early Access
* Projects with MCP servers will now prompt users to enable them
* Chat will now display a notification about usage-based pricing when approaching fast request or usage limits
* Enhanced visibility of auto-run controls configured by team admins, clarifying when they are active
* Removed auto-run prompt due to reliability issues. Auto-run has been disabled for all users who previously enabled it

Improvements (4)

* We've moved "reject all diffs" from Cmd+Backspace (⌘⌫) to Cmd+Shift+Backspace (⌘⇧⌫)
* MCP on Windows should now be significantly more reliable
* Improved MCP error messages when configuring MCP servers to assist with debugging
* Added input token count for chat messages (click the three dots to view). We're continuing to improve context visibility so you can clearly see what gets sent to the model, expect more soon!

Patches (9)

* 0.48.1 - New onboarding
* 0.48.2 - Allows users to accept/reject file edited in another chat tab
* 0.48.3 - Chat Tabs UX improvements (Cmd/Ctrl+T for new tab), Max-mode support for Gemini 2.5 Pro
* 0.48.4 - Image support for Gemini 2.5 Pro
* 0.48.5 - Change management for Cmd+Backspace -> Cmd+Shift+Backspace
* 0.48.6 - Creates a new chat after the AI Pane has been closed for long enough
* 0.48.7 - Fixes an issue where some chats could get deleted on update
* 0.48.8 - Improves CPU performance from @-symbols search
* 0.48.9 - Lower memory usage from indexing

This release focuses mainly on stability and performance improvements to make existing features work better.

* **Memory Usage and Performance**: The new release uses less memory and is more stable.
* **Keyboard Shortcuts**: All keyboard shortcuts are now available in the Keyboard Shortcuts menu. Go to Settings > Keyboard Shortcuts to modify or add new shortcuts.
* **Early access opt-in**: You can now opt in to early access from Settings > Beta > Update frequency.
* **Auto select model**: We choose the most appropriate premium model for the task at hand based on performance, speed, and availability so you get performance even during model degradation or outages.
* **Themes**: New and updated themes including Cursor Dark, Cursor Midnight, and Cursor Dark (High contrast).
* **UI improvements**: Improved tool calling UI, thinking UI and error messages in chat. We've also added a new update notification in the app to make it clearer when a new version is available.
* **Rules**: Allow nested `.cursor/rules` directories and improved UX to make it clearer when rules are being applied.
* **MCP**: Added global server configuration with `~/.cursor/mcp.json` and support for environment variables.
* **Sonnet 3.7 thinking**: We've made a few improvements to 3.7 prompting. Thinking will now cost 2 requests instead of 1. More improvements will be rolling out in the coming days.
* **Ignore files**: Improved `.cursorignore` behavior to more consistently exclude files
* **Upload multiple images**: You can now upload multiple images at once in chat.

Patches (11)

* 0.47.1: Improved performance, added back play button to apply code blocks
* 0.47.2: Cursor Tab accepts work with single-line selections
* 0.47.3: Fixes an issue with tool call errors on file edits
* 0.47.4: Fixes an edge case where red diffs stick around in the editor
* 0.47.5: Client-side support for upcoming MAX mode compatbility for Claude 3.7 Sonnet
* 0.47.6: Faster applies, warns user when edits fails because of cursorignore
* 0.47.7: MAX mode for 3.7 Sonnet with and without thinking
* 0.47.8: UI fix for scrollable model name
* 0.47.9: Performance improvements related to memory usage
* 0.47.10: Fix for chat/apply not working with `.github` and other `.` prefixed folders, and small performance fixes.
* 0.47.11: Release track picker (prerelease or standard), fix for dmg installer not working in rare cases

* **Agent is ready**: Agent is now the default mode, bringing a more powerful and unified AI experience. No more confusion between Chat, Composer, and Agent - just one smart interface that adapts to your needs.
* **UI refresh**: Phase one of a fresh coat of paint with new default Cursor themes designed for focus. We've also simplified the @-context menu to make Agent more precise.
* **Web search**: Agent can now automatically search the web for up-to-date information without requiring explicit @Web commands.
* **Ignore files**: `.cursorignore` now blocks files from being added in chat or sent up for tab completions, in addition to ignoring them from indexing. We've introduced `.cursorindexingignore` for specifically controlling file indexing.
* **Agent tool limit**: Upon reaching the 25 tool call limit, you can press "continue" to proceed (counts as a new request).
* **Project rules**: - New capability to apply rules globally and a visual indicator for when rules will be applied
* **MCP improvements**:

  + Agent can now automatically run MCP tools with Yolo mode
  + Configure Project Servers with `<project-root>/.cursor/mcp.json`
  + Support for Agent to use MCP resources as context
* **Tab rebinding**: Tab suggestions can now be rebound to a different keybinding using editor.action.acceptCursorTabSuggestion

Fixes (3)

* **Crashes**: Enhanced stability through memory and performance improvements, with additional crash prevention systems in place.
* **MCP**: Improved reliability and quality of life enhancements for building MCP servers in Cursor.
* **Windows**: Fixed newline errors in Chat Codeblocks and resolved auto-uninstallation issues.

Patches (11)

* 0.46.1: Fixed HTTP2 and system certificate errors, resolved memory leaks
* 0.46.2: Improved MCP reliability, added option to disable yolo mode for MCP
* 0.46.3: Enhanced download reliability, fixed keybinding issue
* 0.46.4: Added support for multiple image attachments and fixed "User aborted request" error
* 0.46.5: Resolved issues with extended tool calls, long Composer sessions, and retry functionality
* 0.46.6: Improved Windows installation process
* 0.46.7: Improved memory usage and performance
* 0.46.8: Fix for windows 'rename tools' update error, fix for some users unable to cancel agent terminal commands
* 0.46.9: Memory and performances fixes, composer/chat remembers your last mode selection, http/1.1 support for agent/chat, linux python env vars fixed, cursorignore fixes
* 0.46.10: Fix for chat/apply not working with `.github` and other `.` prefixed folders, and small performance fixes.
* 0.46.11: Release track picker (prerelease or standard), fix for dmg installer not working in rare cases

* `.cursor/rules`: Users can write several repository-level rules to disk in the `.cursor/rules` directory. The Agent will automatically choose which rule to follow.
* Deepseek models: Deepseek R1 and Deepseek v3 are supported in 0.45 and 0.44. You can enable them in Settings > Models. We self-host these models in the US.
* Summarize Previous Composers: When conversations grow too long, you can start a new conversation while referencing the previous one.
* Agent sees recent changes: The agent can use a tool to see your recent changes. It also sees changes made between user messages.
* Better Codebase Understanding: We've trained a new model for Codebase Understanding. We'll be rolling it out to all users on 0.45 in the coming week.
* Fusion Model: We've trained a new Tab Model that is substantially better at jumps and long context. We'll also be rolling this out to users shortly.
* Optional Long Context: When tagging long files, users have the option to request a larger context window with premium models. This will use more fast requests.

UPDATE (0.45.1-0.45.11): Fixes issue with older agent conversations, indexing stability, downloading incorrect extension versions, missing package on windows, crash on opening long composer sessions, latency on pasting code.
Also adds MCP support, team-configurable blocklists, fixes Composer stuck on generating issue for some windows builds, exit code 5 crashes, and improves MCP UI. Also several improvements to memory usage.

UPDATE (0.45.12-13): Update infrastructure improvements. The F1 > "Check for Updates" command should now work.

* Agent sees terminal exit codes, can run commands in the background, and commands are now editable
* Agent reads linter errors to automatically fix issues
* With Yolo Mode, the agent can auto-run terminal commands
* @docs, @git, @web, and @folder are now available in the agent
* Agent auto-saves changes to disk
* Agent can decide to edit multiple locations in parallel
* Agent can reapply edits with a smarter apply model
* Composer changes and checkpoints are now persisted across reloads
* Cursor Tab can make larger edits at a time
* Better UX to review changes in Composer
* 4o Support for Agent
* Cheaper and faster Bug Finding Model

### Bug Fixes

* Fixed edge case where Cursor Tab crashed
* Fixed stuck on generating bug in chat/composer
* Composer no longer looks at files that were deleted
* Fixed code selection edge-case for chat/apply
* Cursor starts up faster

UPDATE (0.44.1-0.44.11): Fixes and improvements to dev containers, chat codeblocks on windows, and the agent. Decreases Cursor Tab Latency on Remote SSH. Fixes bug that prematurely triggered the free trial ended popup. Better observability for errors and crashes.

* Composer UI in the sidebar with inline diffs
* Early version of an agent in composer that can pick its own context and use the terminal
* Generation of git commit messages
* File pill recommendations in chat/composer
* @Recommended in chat/composer to semantically search for context
* Nicer image-dropping experience
* Several performance improvements
* Beta: Sneak peek at an upcoming bug finder feature

* Composer history lets you access previous composer sessions after restart. You can also edit and resubmit from previous messages within a session.
* We have made slight improvements to Debug with AI and added back @Lint Errors in Chat.
* VS Code 1.93.1: Cursor is now based on VS Code 1.93.1.
* Python auto import for Cursor Tab is much more stable in this release.
* Switching models is a lot easier with model search (Cmd-option-/) in the chat, composer, and cmd-k input boxes.
* Composer now only applies files that are in context to prevent hallucinations.
* Using `cursor .` with WSL should now be more stable.

UPDATE (0.42.1 - 0.42.5): Fixes the following upstream security issue: [CVE-2024-43601](https://github.com/microsoft/vscode/security/advisories/GHSA-g56j-w527-8x6f). Also fixes a few composer bugs and a bug with Cursor Tab. Allows composer to auto apply to files not in its context. Also includes additional mitigations to [CVE-2024-48919](https://github.com/getcursor/cursor/security/advisories/GHSA-rmj9-23rg-gr67). Reduces a few long-tail connection errors. Adds escape hatch when Claude predicts the wrong filepath in chat.

*This update fixes the following security issue: [CVE-2024-45599](https://github.com/getcursor/cursor/security/advisories/GHSA-x352-xv29-r74m).*

* Cursor Tab now auto-imports symbols in Python files! We've also significantly improved the Cursor Tab stability.
* Composer Notepads (previously called Projects) can now include tagged files and be referenced in chat, as well as composer.
* Composer can now be added to the AI pane. This release also includes many stability fixes and image support!
* Apply and Composer are slightly faster in this release.
* We've added support for using Cursor on Macs over Remote SSH.

UPDATE (0.41.1 - 0.41.3): Improves onboarding UX, fixes a bug with composer cancellation, fixes the Apply button not working on some codeblocks, and fixes a bug where Cursor Tab sees malformed edits.

* We have a new chat UX! Excited for you to try it out and share your thoughts.
* Composer is now default-on and available to all Pro/Business users by hitting cmd+I. We've added Composer Projects (beta), which allows you to share instructions among several composers.
* We've also trained a new Cursor Tab model that's smarter and more context-aware.
* Auto imports (beta) for Cursor Tab for TypeScript files - when Tab suggests an unimported symbol, we'll now auto-import it to your current file. You can enable it in Settings > Features > Cursor Tab!

UPDATE (0.40.1 - 0.40.4): Fixes a bug with apply on remote ssh, a few chat bugs, speeds up Cursor Tab for Europe/Asia users, fixes some outstanding Cursor Tab bugs and notifications hiding the chat input, and includes a fix for Cursor asking for permissions for files in your `~/Library` folder on MacOS (upstream issue: [microsoft/vscode#208105](https://github.com/microsoft/vscode/issues/208105))

* Cursor Tab (previously called Copilot++) defaults to chunked streaming. This build also includes several Cursor Tab speedups. More to come in future builds!
* Concurrent composers support, composer control panel, and various bug fixes such as accepted files being deleted.

Faster Cursor Tab Suggestions!

UPDATE (0.39.1 - 0.39.6): Fixes several Cursor Tab rendering bugs, a bug where the file explorer was not responsive, and a bug where Cursor Tab would hang.

* Copilot++ now has chunked streaming (currently in Beta)! It will surface edits faster in smaller chunks. To enable it, click the settings gear and enable "Chunked Streaming" under Features > Copilot++.
* We've also added a file picker, arrow key navigation, and a model toggle to Composer. This release also patches a few outstanding Composer bugs.
* VS Code 1.91.1: Cursor is now based on VS Code 1.91.1.
* New Default Model: We've made Claude 3.5 Sonnet the default model for users.

UPDATE (0.38.1): Fixes a bug where OpenAI API Key users would be migrated to Claude 3.5 Sonnet

This build comes with a new experimental multi-file editing feature. To enable it, click the settings gear, head to Beta, and activate "Composer." To use it, hit Cmd+I. We'd love [to hear your thoughts](https://forum.cursor.sh/).

* When the chat suggests a code block, click "Apply" to instantly see the change to the file (small enough files only).
* Docs management! Go to Cursor Settings > Features > Docs to re-index your docs.
* Bug fixes when using your own API key for Claude.

UPDATE (0.36.1-0.36.2): Fixes [#1526, cmd-shift-F on macOS x64 devices](https://github.com/getcursor/cursor/issues/1526). Also fixes official docs taking a long time to show up, and [cmd-K stickiness being buggy](https://forum.cursor.com/t/cntrl-k-broken-in-update-7-6-2024-version-0-36-1-vscode-version-1-89-1/6251/6).

* Default-on Cursor Prediction with a new UI
* Remote tunnels are now supported! Remote SSH support is also more robust (now supports multiple proxy jumps, among other things).
* Adds context pills to chat messages, so you can see what will be/was used
* Cmd K context-building improvements
* Fixes partial completions with Copilot++ on Windows/Linux

UPDATE (0.35.1): Disables Copilot++ partial accepts by default and makes the keybinding configurable (go to Cursor Settings > Features > Cpp to re-enable). Makes gpt-4o the default model.

* Merges VS Code 1.89 into Cursor
* New Cursor Prediction UI
* Gemini 1.5 Flash is available in long-context mode
* Accept partial completions with Copilot++
* Better performance of Copilot++ on linter errors
* Toggleable rerankers on codebase search
* GPT-4o in Interpreter Mode

UPDATE (0.34.1-0.34.6): Fixes long context models in the model toggle, an empty AI Review tab, Copilot++ preview bugs, the Mac icon size, and remote ssh fixes.

* Stability: This build fixes a connection error problem that was consistently affecting some users. It should also improve the performance of Cursor on spotty internet.
* Command-K Autoselect: We've also added automatic selection for Command-K! This means you can now press Command-K, and it will automatically select the region you're working on, though you can still select manually if you prefer.

UPDATE (0.33.1-0.33.3): Fix to settings toggles, fix to Copilot++ diffbox performance, onboarding tweaks.

* Copilot++ UX: Suggestion previews now have syntax highlighting, which we find makes it much easier to quickly understand the changes.
* Cursor Help Pane (Beta): You can also ask Cursor about Cursor! The Cursor Help Pane has information about features, keyboard shortcuts, and much more. You can enable it in Settings > Beta.
* New GPT-4 model: As of a couple of days ago, you can try out `gpt-4-turbo-2024-04-09` in Cursor by toggling it on in Settings > Models.
* `.cursorrules`: You can write down repo-level rules for the AI by creating a `.cursorrules` file in the root of your repository. You might use this to give for context on what you're building, style guidelines, or info on commonly-used methods.

UPDATE (0.32.1-0.32.7): Fixes a performance issue with the new Copilot++ syntax highlighting, changes AI Notes to be default disabled, changes the naming of the `main` Copilot++ model to `legacy`, fixes Copilot++ being slower over SSH, fixes to the Copilot++ preview box.

* Long Context Chat (Beta): This is a new experimental feature that lets you talk with *lots* of files! To enable it, head to Settings > Beta. Then, select "Long Context Chat" in the top right of a new chat and try @'ing a folder or the entire codebase.
* Fixes: This release patches a bug where empty / partial responses are shown in chat.

UPDATE (0.31.1 - 0.31.3): Adds back in AI Review (alpha), fixes the "Cursor Settings" menu item, and fixes a bug where @web doesn't return a response.

* Faster Copilot++: We've made Copilot++ ~2x faster! This speed bump comes from a new model / faster inference. ~50% of users are already on this model, and it will roll out to everyone over a few days. If you'd like to enable the model immediately, you can control your model in the bottom bar of the editor.
* Stable Claude Support: All the newest Claude models are available for Pro and API key users. Head to Settings > Models to toggle them on. Pro users get 10 requests / day for free and can keep using Claude at API-key prices for subsequent requests.
* Team invites: We made it a bit easier for you to invite your colleagues to your Cursor team. You can send these from the editor's settings or at [cursor.com/settings](https://cursor.com/settings).
* Admin improvements: Team admins can now mark themselves as unpaid users and can see the last time team members used the product.
* New Settings: We moved all our settings to be accessible by the gear in the top right. No more "More" tab!

If you're a Pro or Business user, you can add "claude-3-opus" as a custom model in the Settings page and use 10 fast requests per day for free (unlimited slow, but the delay increases exponentially).

We expect to roll out a more permanent solution (including API key users) very soon.

AI Notes enabled by default (hold shift on any symbol), better in-editor chat, auto-execute interpreter mode, better onboarding styling, nicer feedback modal, and a few stability fixes.

UPDATE (0.29.1): Fixes a bug where the Copilot++ sometimes would not show a suggestion even if one existed, a bug where the hint line would sometimes cover the ghost text, and a bug where AI Notes would not work on Windows.

Cursor is now based on VS Code 1.86.2! Among other things, this adds sticky scroll support to tree views. Also, cmdk prompt bars are now sticky.

UPDATE (0.28.1): Fixes spacing issue with codebase chat, fixes [getcursor/cursor#1236](https://github.com/getcursor/cursor/issues/1236).

Two new updates to experimental features:

* Linter: You can now turn on an AI linter in the "More" tab beside Chat. It'll scan your file for small bugs every time you save.
* Interpreter Mode: We've made some big improvements to the backend powering interpreter mode! It should now be much better at using tools and understanding your project.

UPDATE (0.27.1-0.27.4): Fixes to Windows build, chat context UI, onboarding.

AI Previews: this is an experimental new code reading feature. After enabling in the "More" tab beside Chat, just hold shift to see a generate some quick notes about the symbol you're on. If you'd like us to dedicate more time to this direction, please [let us know](https://forum.cursor.com).

Other changes:

* Fine-grained chat replies (start by hovering over the area of the response you want to reply to)
* Copilot++ quality of life improvements (show ghost text more often, toggle on/off on the status bar, make it easier to see the suggestion box)
* Smoother onboarding (fix Windows settings import, option to import folder/window state)

Hold down cmd-I over a selection to heal the code with GPT-4. Useful for writing pseudocode and having the AI convert it into correct code. Please let us know if you find it useful!

You can now drag images into the Command-K prompt bar!

Other changes:

* You can now search through past chats.
* "Apply Diffs" from chat should be a bit faster.

UPDATES:

* 0.25.2: Copilot++ performance improvements
* 0.25.3: Fix for a cmd-K bug: [getcursor/cursor#1226](https://github.com/getcursor/cursor/issues/1226).

Using @Web in chat will give the AI the ability to crawl the web! The tools it can use include a search engine and a documentation site crawler.

This feature is still experimental. We're very interested in improving the ability of the AI to understand external libraries, and your [thoughts](https://forum.cursor.com/) will help us improve :).

Both pro and API key users can also try out gpt-4-0125-preview by configuring the model under Settings > OpenAI API > Configure Models. We're testing the new model right now for pro users to see if it performs better than all older versions of gpt-4. If so, will roll out as the default experience.

UPDATE (0.24.3-0.24.4): Adds ability to configure OpenAI base URL, fixes [getcursor/cursor#1202](https://github.com/getcursor/cursor/issues/1202).

* "cursor-fast": This is a new model available in command-k and chat. Expect it to be a bit smarter than gpt-3.5, and with many fewer formatting errors.
* Apply button: We've added some polish to the "apply codeblock" experience in chat.
* Chat lints: If the AI suggests a code change in chat that involves a made up code symbol, we'll underline it. Availble for Python, Typescript, Rust.
* More chat symbol links: When the chat references a `code symbol`, you'll often be able to click directly to it.

UPDATE (0.23.3-0.23.9): Fixes to Command-K, changelog auto-opening, editing very long lines with Copilot++, the "delete index" button, connection errors being silenced, and proxied authentication.

Cursor-Fast is a newly trained model between gpt-3.5 and gpt-4 coding capabilities, with very fast response times (~3.5 speed).
We'll be working to improve its performance over the coming weeks. Counts the same as 3.5 usage.

Try using it for Cmd+k!

Bug fixes:

* Working WSL codebase search
* Supports newer version of python extension

Dev containers are now supported! This build also:

* Upgrades Cursor to VS Code 1.85, which comes with support for dragging out tabs into a new window.
* Improves the stability of WSL.

WSL and Dev Containers should now work properly.

Hold down command, press and release shift, and continue holding down command. This will trigger tha AI to rewrite code around your Cursor — you can think of it as a manually triggered GPT-4-powered Copilot++. You can use it to write pseudocode and have the AI correct it, or for tedious refactors where Copilot++ doesn't quite suffice.

You can now use chat and cmd-k in the aux window without too many problems.

Cursor is now based on VS Code 1.85.1, which, among other things, includes floating editor windows. Just drag and drop an editor onto your desktop to try it out.

You can now run multiple Command-K's in parallel! Also, it should now be easier to see change Copilot++ is suggesting.

* @ previews: We made it easier to see what codeblock you're @'ing.
* Copilot++: We've contined to improve the Copilot++ ghost text experience. Surprisingly, many of us now enjoy using Copilot++ without any other autocomplete plugin installed.
* AI Review (beta): This is a new experimental feature that let's GPT-4 scan your git diff or PR for bugs. You can enable it in the "More" tab beside chat. [Feedback](https://forum.cursor.com/) is much appreciated.

UPDATE (0.20.1-0.20.2): We added TLDRs to make it easier to sort through the bugs flagged by the AI review and fixed a bug with "Diff with Main."

Fixes a CRLF bug in interpreter mode: [getcursor/cursor#1131](https://github.com/getcursor/cursor/issues/1131).

We made Copilot++ faster, smarter, more constrained, and switched to a ghost-text + hit-Tab-to-accept UI. Would love your feedback.

Make ssh work on xon.sh

Mino bug fixes.

Minor onboarding fixes.

Minor onboarding changes.
Allows users to provide feedback on the chat response.

Running Cmd+enter on followups should result in much better codebase results.

Fixes the bug where all folders are switched to lowercase when using @ folder in chat.

1. Better context chat: in particular, followups are now smarter!
2. Faster Copilot++: a few hundred milliseconds faster, through various networking optimizations. We still have several hundred additional milliseconds to cut here.
3. More reliable Copilot++ changes: less flashing, better highlighting of what's new.

* Image Support in Chat: You can now drag and drop images into the chat to send them to the AI.
* Interpeter Mode Beta: You can now enable Interpreter Mode in the "More" tab. This gives the chat access to a Python notebook, semantic search, and more tools.
* @ folders: You can now use the @ symbol to reference specific folders! We'll try to pick out the most relevant code snippets to show the AI.
* Copilot++ Improvements: We've spent some time improving the latency of Copilot++, and you can change the Copilot++ keybinding to not be Option/Alt. More to come here soon, especially on the model itself!

Fixes a bug where the interpreter mode just wouldn't run at all on Windows.

Fixes the bug where images weren't showing up or being sent to server on Windows.

You can now @folder in the chat to chat with a folder. Let us know what you think!

Experimental feature: go to "More" > "Interpreter Mode" to enable it. Gives the model access to a Python notebook where it can take actions in the editor. Please give us feedback in the Discord! We'd love to know if you find it useful.

Integrates GPT-V into chat for the editor. This means you can take screenshots/images and drag it into the chat inputbox to have Cursor use them as context.
This is an experimental feature and very limited by capacity, so you may see errors during traffic spikes.

Copilot++ improvements:

1. Caching — add and delete a letter and the suggestion will still be there for you!
2. Do not interfere with intellisense and cmd-k.
3. Fixes bugs with lag on large files and with the blue highlight staying around.
4. Copilot++ sees your lint errors and will use this to improve its suggestions

Cursor is now based on VS Code 1.84.2. Notably, this fixes a few notebook bugs, and ensures that all of the most recent extensions work.

Now based on VS Code 1.84.2. Notably, this fixes a few notebook bugs, and ensures that all of the most recent extensions work.

* Copilot++ improvements: Includes green highlights to see what Copilot++ has added, the ability to accept multiple Copilot++ suggestions immediately one after another, support for Copilot++ on SSH, and fixes to how Copilot++ UI interacts with autocomplete plugins.
* Bug fixes: Fixed a bug where Cmd-k could get into a bad state when removing at the top of a file. And another that was causing some files to not be indexed.

* Command-dot: you can now use the Command-dot menu to have Command-K fix lint errors inline.
* New models: you can plug in your API key to try out the newest gpt-4 and gpt-3 turbo models. We're evaluating the coding skills of these models before rolling out to pro users.
* Apply chat suggestions: click on the play button on any code block to have the AI apply in-chat suggestions to your current file.
* Copilot++ (beta): this is an "add-on" to Copilot that suggests diffs around your cursor, using your recent edits as context. To enable it, go to the "More" tab in the right chat bar. Note: to cover the costs of the AI, this is only available for pro users.
  + This is very experimental, so don't expect too much yet! [Your feedback](https://forum.cursor.com/) will decide which direction we take this.

Fixes a problem where indexing got stuck. Indexing capacity is now also allocated by-user, so it should be more fair and faster for most users.

* Pro++ plan: if you hit your fast request limit and prefer to purchase more, you now can.
* Chat scroll: we got rid of sticky scroll to make the chat easier to read.
* Cmd-K diffs: these now obey word-wrap! You can also copy from the red text.
* Fixed the bug where you can't use chat on a diff view.
* Shipped better error logging, which should help us improve stability.
* Styling tweaks: some buttons and hints should look nicer!
* Screen flickering: made a change that should reduce screen flickering on monitors.

Cursor is now based on VS Code 1.83.1. This ensures that the newest versions of all extensions will work without problem in Cursor. Thank you to everyone who urged us to do this on the [forum](https://forum.cursor.com/t/vscode-version-1-83-cursor/954/21)!

Also, there's an experimental bash mode: enable it in the settings, and let the chat answer questions with the help of running bash commands. If you find it useful, please let us know, and we will spend more time on making it production-ready!

Update: this change resulted in a problem with SSHing into old Linux distros. This has now been fixed!

Bug fixes: (1) .cursorignore now completely respects .gitignore syntax, (2) codebase queries use the embeddings index if >= 80% of it is indexed, instead of requiring the entire thing to be indexed, (3) removed fade-in animation on startup, (4) no longer overrides cmd-delete in the terminal, (5) fixes problem where cmd-F randomly has the case-sensitive option enabled, (6) inline gpt-4 is turned off until we figure out a better UX, (7) even more stable and fast indexing, (8) progress indicator in search and extensions, (9) bug where an incorrect bearer token is passed to the server.

Fixes a bug that prevents importing the jupyter extension from VS Code.

1. Indexing should now be faster, more stable, and use less of your system resources. You can also configure ignored files in a `.cursorignore`. The controls are in the "More" tab.
2. Cmd-k is now in the terminal! A bit hackily implemented, but surprisingly useful.
3. Ask about git commits and PRs using @git in chat!
4. Use /edit in the chat to edit a whole file (if less than 400 lines). Expect the edits to be fast and GPT-4-quality. This uses non-public models, and is for now only available to users who do not use their own API key.
5. Bugfixes! Fixed the "ejected from slow mode" UI, added auto-switching logic for the model type when switching on API, improved @ symbol speed, fixed Windows keycommand to be Ctrl-Shift-Y instead of Ctrl-Y, and more.

You can now use an early preview of `/edit` in the chat! It's significantly faster at editing entire files than just using cmd-k. The `/edit` feature is currently only supported if you do not use your own API key, since it relies on non-public models.

1. Fixes an annoying gitignore path bug
2. never lets your root directory be in the gitignore
3. fixes search over the repository.

Stable version of indexing. this should be much more stable than previous versions.

Hacky first version of cmd-K in the terminal! Let us know what you think.

We ship a new version of indexing which should be significantly more stable than previous versions

Fixes issues with Cmd-k, SSH, Python support, Vim (rolling back to 1.25.2 until this issue is fixed: [VSCodeVim/Vim#8603](https://github.com/VSCodeVim/Vim/issues/8603)), and other extensions.

You can now alternate between diffs and texts responses in Cmd-K. This can be helpful for clarifying the models thinking behind a diff or for getting quick inline answers to questions about a file.

We point to a different marketplace for downloading extensions, and use a fork of ms-python and pyright to provide python support.

We re-enable cursor python in nightly, this time with defaults that more closely resemble pylance.

We serve extensions now using Cursor's Extension Marketplace

Fixes a bug where the @ symbol would rank suboptimally.

Ask a question about an edit that the model with option+enter, or bring in context from the chat with @chat! An early preview, so please let us know what you think.

The defaults for cursor python are different than pylance, which has affected several users. We make them
closer to the pylance defaults in this update.

Fixes an issue where some users were getting extension popup recommendations too often.

Updated some css!

### Docs

The main addition in this update is better docs support. This means you can add and remove docs and inspect the urls
that are actually being used for each doc you have uploaded. You'll also be able to see what webpages end up being shown to GPT-4 to provide you an answer.

You can also paste a url into the chat and the model will automatically include it in the context being used.
Teams can also share private docs.

### Staged Rollouts

Following this update, future updates should come as staged rollouts. This will mean greater guarantees of stability and more frequent updates.

### Long files in chat

We continued to improve the experience of chatting with large files. If you @ multiple files that are too large to fit in GPT-4's context window, we'll intelligently pick the most relevant chunks of code to show to show the model.

### Bug fixes:

* Copy Paste chat text form Jupyter
* Some chat focus issues
* UI tweaks
* Better state management - prevents crashes from editor using too much memory

Updated some css!

Also fixes a few cmd+k bugs, as well as introduces new cmd+k bugs! Please report all cmd+k bugs you find to us in the Discord channel.

We release an improved New AI Project feature to nightly users. This is a more robust chain and cleaner
UX for producing a project end-to-end.

It still struggles with coherently producing large complex projects, but produces much better first drafts than previously

Fixes a bug with indexing if you had turned off indexing by default.

We no longer store any full files in memory and prevent users from @'ing very large files (> 2MB)
This should reduce any significant memory issues that users have been experiencing.

Cmd-K will no longer output backticks if you do `@file`.

Updates to docs (try pasting a link in chat, you can delete/edit docs, you can see citations), @ symbol performance on long files in chat should improve, and more.

Ships with cursor-python, a Language-Server fork of pyright built for Cursor

We can push an update to a randomly sampled small fraction of our users before rolling out to everyone.

You should now be able to sign in with GitHub again.

Could cause [getcursor/cursor#843](https://github.com/getcursor/cursor/issues/843).

Could cause [getcursor/cursor#843](https://github.com/getcursor/cursor/issues/843).

Hotfixes a problem with SSH.

* [You can now switch to the VS Code sidebar orientation](https://forum.cursor.com/t/getting-used-to-the-orientation-of-the-primary-sidebar/20/4?u=truell20)
* For "with codebase" chats, you can now see the codebase context that Cursor shows GPT-4. We hope this will make it easier to prompt codebase answers.
* API Key input box is now a password type
* Fixed a bug where code was being indexed right after turning off the indexing option
* A new icon! Thank you so much to [the amazing Atanas Mahony](https://twitter.com/amahony/status/1694662454041604510) who made it.

Small refactor that we want to make sure doesn't break! Please report bugs if you find them.

The email under the logout button in Cursor settings was not updating.

Have the advanced context button show up for non git repos.

We had a big bug for people on language packs. Thank you to all who helped us debug! This should now be fixed, and should not happen again.

Applies the patch [from Github](https://github.com/getcursor/cursor/issues/660#issuecomment-1692569259) across all your WSL (Windows Subsystem for Linux) distros, either automatically or through the "Fix WSL" command palette command.

Fixes a bug were codebase indexing controls where inadvertently removed.

* You can now reply to Cmd-K outputs, making it much easier to have the model revise its work.
* If you @ reference a long file that will be cutoff by the context limit, you'll be given the option to automatically chunk the file and scan it with many GPTs.
* Codeblocks and code symbols in "with codebase" responses will now often be clickable.
* Follow-up chat messages to "with codebase" will keep the codebase context.
* Nicer error messages in the chat! Fewer annoying popups.
* Activity bar elements can now be reordered with drag-and-drop.
* SSH support is now more robust! Please continue to let us know if you are experiencing any SSH problems.

Set `workbench.activityBar.orientation` to `vertical`, and restart Cursor, to see the vertical activity bar that you're used to from VS Code.

1. Nicer error messages in the chat! Fewer annoying popups.
2. Activity bar elements can now be reordered with drag-and-drop.

SSH support is now more robust! Please continue to let us know if you are experiencing any SSH problems.

Small things!

The `cursor-nightly` command now works on Mac.

Keychords now use Cmd+R/Ctrl+R.

Fixes a bug with installing the `cursor` command on Windows.

Better experience for long files!

The cmd-k edits now support followups! This is an early preview — please let us know of any annoyances or bugs, or if you preferred the no-followup mode. Please please send all feedback you have in the Discord channel!

No more cognitive computing!

1. Fix [getcursor/cursor#711](https://github.com/getcursor/cursor/issues/711).
2. Fix cmd-k connection error.
3. Fix cmd-k fast mode bug with empty lines.
4. Fix bm25 search infinite loading.
5. Fix @Codebase in followups.

For those who don't want the chat side-by-side, you can now pop it into your editor! We've also fixed a number of bugs.

Cmd-K now has a fast mode! It is about 1 second faster, and we're working on making it even faster. Let us know what you think!

And a few other quality-of-life updates.

Also, the linter is slightly improved.

Improved linter! Please give us feedback on the linter suggestions using the smiley faces. If you would like, you can make it more aggressive by going to the More tab and then clicking on "Advanced linter settings" at the bottom. Let us know what you think in the Discord.

### Long AI completions

If you press ⌘/^+↩️ on any line, you will now get gpt-4 powering fast-completions for you!
We know that sometimes all of us want copilot to write an entire function or a big chunk of code.
But copilot can be slow and sometimes just not smart enough :(. So we're trying to solve this with a
new completion experience powered by gpt-4. Just press ⌘/^+↩️ and you'll get a long completion from gpt-4.

### Better support for remote-ssh

Remote-ssh is now built-in to cursor. You do not need to edit the behavior, it should just work :)
We know this has been a big blocker for many users that rely on remote machines for development.
If you are still running into issues, please let us know and we will fix it ASAP.

### AI linter

The AI linter is now enabled for everyone in pro! The AI will highlight suspicious parts of your code in blue. You can also add your own lint rules that you want that are easy to express in natural language but aren't covered by traditional linters.

Fixes a performance bug that would happen if you use cmd-k a lot.

Fixes a performance bug that would happen if you use cmd-k a lot.

More robust extension handling. You can now use pre-release extensions again.

1. Enterprise support!
2. C# and F# now properly render in the chat
3. Qmd support has been restored
4. Experimental @Codebase support in the chat (and coming to the cmd-k soon!)
5. Linter is back!
6. Some fixes to codebase indexing.

Removes a check in the chat that slows the chat down in certain cases.

You can now chat with any codebase. No need to have a Github repo / login through Github.

Cmd-K can again see all of your cells in Jupyter!

* SSH and WSL should work again
* Can see recent folders on the new window screen
* Empty message in chat with codebase context no longer loads forever

Fixes a bug with CMD-k prompt history that would freeze the input box.

Let us know what you think!

Hotfixes etc.

Fixes a bug that resulted in green-lines staying around after cancelling CMD-K.

* Cmd-L now properly focuses the chat again
* Advanced context controls only show up if you have indexed your codebase

This build includes:

* More control of context building abilities for codebase-wide chat
* A better flow for getting CMD-k to produce code with no linter errors (you should see a "Try lint-fix" button when relevant)
* Some UI/UX tweaks to CMD-K
* Bug fixes

This update fixes the bug where we hang on chat for up to 20s when not in a git repo

This update fixes the infinite loop bug in the chat pane.

1. Fixed agent editing ability
2. Fixed issue with in-editor chat
3. Fixed issues with Cmd + K

1. Semantic search in Cmd-Shift-F
2. Some Cmd-K fixes
3. Pop-out chat! You can now view the chat in an editor, which is great if you're on a small screen.

This update patches search (Cmd/Win+Shift+F) and many extensions for and WSL and SSH users.

This update improves the prompt for Cmd-k when you don't have any code selected.

This nightly build comes with experimental interface agent support!

The goal: you write an interface specification, and an agent writes both the tests and the implementation for you. It makes sure that the tests pass, so you don't even need to look at the implementation at all.

We think this may enable a new kind of programming, that's kind of different to what we're all used to. Please experiment with it and let us know your thoughts in the Discord channel.

How to use it:

1. It only works in Typescript with vitest or mocha as test runners right now.
2. Hit Cmd-Shift-I, and give your new interface a name.
3. Write the methods you want your interface to have.
4. Hit Cmd-Shift-Enter, and the AI will write the interface for you!

This update contains an optimistic patch to Ctrl+Shift+F for ARM Windows computers.

* Improved the "@Add new doc" experience
* Python/Pylance support has been restored
* Better @ symbol keyboard ergonomics
* Makes it clearer which docs are being looked at by the AI
* AI will respond with citations when you refernce docs
* Fixes Cmd-K for Jupyter
* Chat/Edit tooltip blocks less code
* Improves Cursor's appearance when custom themes are on
* Importing VS Code extensions now takes into account enabled/disabled
* Cmd-k should work better for long diffs (greater than 100 lines of code)

Welcome to the first nightly release! It comes with agents, which we aren't releasing to the general public yet because we aren't convinced that they are useful. If you like them, please let us know what you use them for!

Patches a few edgecases with Cmd+K.

Fixes the VS Code codebase wide search for Mac ARM users without Rosetta.

Includes a fix for the chat "with codebase" feature.

This build has no changes for Mac and Windows, but fixes a problem for Linux users who can now upgrade to the latest version.

Cmd+K's UI has been changed: it's in-editor, "sticky," and @-symbol-compatible.
We hope it helps you stay in flow and more quickly iterate on your prompts.
(Also, you can now use up/down arrows for history in chat.)

Also, Cursor's AI will now use popular documentation to improve the answers to your questions. For example, if you ask it "how do I grab all s3 buckets with boto3?" it will search over the boto3 docs to find the answer. To add your own documentation or explicitly reference existing docs, type '@library\_name' in chat.

Bug fixes:

1. Long code selections no longer brick the editor
2. Auto-fixing errors no longer brings up the problems view (in particular, this fixes an annoying bug if you have auto-fix on save turned on)

* Better @ symbol keyboard ergonomics
* Fixes a bug where Cmd+K turned off for some users.
* Better support for extensions (specifically re-enables the welcomeView)

1. Chat works if you don't have a folder open again
2. Cmd-shift-E to fix an error in chat works again
3. `cursor://` deep linking works now, so you should be able to log in to extensions
4. Autoscrolling works again
5. A few cmd-Z bugs for inline diffs have been squashed
6. You can now use Run & debug in Cursor again (the toolbar is back)
7. Early support for slash commands
8. If you're not logged in, we show the popup to log in again
9. Cursor is now based on version 1.79.2 of VSCodium, which comes with security updates and minor features

Chat was failing on some non-git folders. That is now fixed.

The chat has been revamped! You can now use @ symbols to show files/code/docs to the AI. The chat history is improved, it's easier to see what the AI can see, and codeblocks auto-format on paste.

The AI linter now shows diffs!

We've added support for using your Azure OpenAI credentials. Also, small improvements / fixes.

Small fix for a format-on-save bug that was introduced in the last release. Some small improvements to the AI linter and codebase-wide chat.

Chat should not steal your focus away! This is now fixed.

You can now have the AI read documentation on your behalf! This will improve it's ability to answer questions about your favorite libraries. To use this feature, simply press the "Docs" button in the top right of the chat pane.

Hotfixes to v1 of Codebase Context

We've improved codebase context!

In order to take full advantage, navigate to Settings (top right button), then "Sync the current codebase"

Login via github, then add the repo you wish to sync!

Following this, you'll be able to see an improved version of codebase context in the search pane, and in chat (by pressing cmd+enter).

### Codebase Context v1

Introducing v1 of codebase-wide context! We'll be shipping major improvements to this in the next few days, but we'd love to hear your feedback.

Go to the "Search" pane in order to see the new context.

Or, on chat, press Cmd+Enter in order to get a response that uses context from the full codebase.

Also potentially fixes the Jupyter problem that many people are experiencing.

Small fixes for the toolformer and the AI linter.

Check out the "more" tab to have GPT-3.5 or GPT-4 review your code periodically for any problems.

### Upgrades to GPT-4

* All users get 10 free gpt-4 requests !!!
* Switching between models is a lot more easy, and the transition to gpt-4 is a lot smoother

### Please give us feedback!!

Please keep the bug reports rolling! We really are listening!

* We've added a new feedback button at the top right of the app. - We really do
  listen to your feedback, and your bug reports! We've fixed a lot of bugs in the
  last few weeks, and we're excited to keep improving the product. - We made this
  modal to make it easier to report feedback. Please keep the feedback coming!

### Bug Fixes

* Fixes the "infinite loading" bug
* Reintroduces the "New AI Project"

### In-terminal Debugging

* Press Cmd+D to auto-debug a terminal error
* Press Cmd+Shift+L, and the model will add the terminal context to chat

### Activity Bar pinning

* You can Pin custom extensions to your activity bar in the top left

  Here I've pinned File Explorer, Search, Source Control, and Extensions

### Better Jupyter Support

* Context ingestion across a full notebook
* Small bug fixes

### Diff/Generate improvements

* Partial diff accent/reject

  Pressing Cmd+Y/Cmd+N lets you accept/reject subdiffs!
* Generates work when you click elsewhere!
* Fixed diff bug where it edits outside selected region

### ️ Quality of Life Improvements

* Press ESC to exit the chat
* Fixed the bug that shrinks code blocks in the chat!
* Remote SSH is easier to use!
* A better Cursor Tutor onboarding!
* Better prompting for Toolformer

### Bug Fixes

* Fixes the "More" tab
* Includes some updates to "Option+Enter" in the chat

### Bug Fixes

* Hotfix for 2 long-standing bugs:
  + Broken chat that persists for a workspace
  + Rarely, pressing Enter in the editor does nothing

### New Features

* One-Click Extension Import from VS Code (beta). As a highly requested feature, we're excited to present the beta version of one-click extension imports!
* Alpha feature: 🧠 Alpha feature: Ask questions about your entire repo 🛠️. We are experimenting with ⌥+enter in the chat! The feature allows the model to think deeply about your response, search through files, and deliver a well-crafted answer. While it's in alpha, we're working hard to enhance this feature in the coming weeks. We'd love to hear your feedback!

### Bug Fixes

* Improved prompting for edits and generates
* Fixed login bugs
* Added the ability to hide the tooltip (Cursor config > Advanced > Chat/Edit Tooltip)
* Extended prompt length for project generation
* GPT-4 support now available for project generation

### New Features

* Experimental support for multi-file diffs
* 🌐 Working remote ssh support through the "OpenRemote - SSH" extension

### New Features

* GPT-4 now available for Pro users
  + 150k GPT-4 tokens included
  + Switch models in settings gear
  + Better quality for all AI features
* New experimental feature: Generate entire projects from a single prompt

### Bug Fixes

### New Features

* Fixes to scrolling in chat
* Ghost mode for opting out of storing any kind of data on our servers

### Bug Fixes

* Nicer edits, now work with cmd-Z
* Various bugs squashed in the streaming diffs

### New Features

* Hover over an error to have the AI explain it/fix it

### Bug Fixes

* Settings icon on Linux
* Don't install "cursor" command on startup

### Coming soon

### Bug Fixes

* Fixes the Mac autoupdating experience
* "Undefined uri" issue fixed
* Turns off the auto-install of the "cursor ." command (and fixes its install altogether)

### Bug Fixes

* We've transitioned to building Cursor on top of a fork of VSCodium, moving away from our previous Codemirror-based approach.
* This allows us to focus on AI features while leveraging VSCode's mature text editing capabilities.
* Our goal is to create an IDE optimized for pair-programming with AI.
* While currently similar to a standard code editor with AI features, we plan to evolve the programming experience significantly over time.

### New Features

* Transitioned to building Cursor on top of a fork of VSCodium
* Focus on enhancing the AI for pair-programming

### New Features

* AI now requires login
* Use an OpenAI API key for unlimited requests at cost (GPT-4 access if available)

### Bug Fixes

* Cleaned up chat styling
* Other small changes

### Bug Fixes

* Tiny bug fix for terminal

### Bug Fixes

* Tiny fix for some keyboard shortcut problems
* Other bits of polish

### New Features

* Opens the terminal in your current folder
* Adds an optional paid plan if you'd like to avoid the server capacity rate limits

### Bug Fixes

* Changes autoupdate to notify you when there's a new version
* Other fixes

### New Features

* Fuzzy search for file names

### Bug Fixes

* Fixes glitches with the terminal
* Scrollbars work
* Other fixes (many from PRs 🙂)

### Bug Fixes

### New Features

* Automatically apply chat suggestion
* Ask AI to "fix" language errors
* Chat history saved between sessions

### Bug Fixes

* Easy to select and copy from chat
* Resizable sidebar
* Terminal no longer interferes with chat

### Coming soon

* Fixes to all the language servers/copilot

### New Features

* Built-in terminal
* Diffs automatically continue

### Bug Fixes

* More diff fixes
* Up and down arrow in prompt bar have been mapped to less annoying keybindings
* Can open chat history from the prompt bar

### Coming soon

* Have chat auto-insert suggested changes into editor

### New Features

* Windows and Linux support 🥳
* Edits can be as long as you'd like

### Bug Fixes

* Diffs shouldn't disappear anymore
* Editing works for same file on multiple tabs

### Coming soon

* Instant fix all lint errors with AI 😎
