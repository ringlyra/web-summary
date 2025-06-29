---
title: 'Install Tailscale on Windows with WSL 2 · Tailscale Docs'
source: https://tailscale.com/kb/1295/install-windows-wsl2
author:
  - tailscale.com
published: ''
fetched: '2025-06-29T01:47:13.897911+00:00'
tags:
  - codex
  - tailscale
image: https://tailscale.com/files/images/og-image.png
---

## 要約

Windows上のWSL2にTailscaleを導入する手順を案内するドキュメント。まず`wsl -l -v`でWSL2を確認し、Linux環境からcurlでインストールスクリプトを実行する。完了後に`sudo tailscale up`でブラウザを開きSSO認証するとtailnetに参加できる。WSL2のノード名はWindowsと重複しやすく、管理画面で変更可能。新しいノードはMachinesページに表示され、不要になれば`sudo apt-get remove tailscale`で削除できる。WindowsとWSL2で同時実行するとパケットが二重化し通信に失敗するため推奨されず、WSL2ではMTUを1340へ上げて動作する。

## 本文

Install Tailscale on Windows with WSL 2
=======================================

The current version of the Tailscale client available for [download](https://tailscale.com/download/windows) requires Windows 10 or later.

Installing Tailscale on WSL 2 is an advanced concept. You can find learn more about WSL from [Microsoft's documentation](https://learn.microsoft.com/en-us/windows/wsl).

There is a specific issue with packet size and Tailscale. You can follow this [GitHub issue](https://github.com/tailscale/tailscale/issues/4833) for details. Report any performance issues on this thread if it is related.

This topic shows how to install Tailscale within the Windows Subsystem for Linux (WSL 2) package. If you want to use the Tailscale
`.exe` installer, see [Install Tailscale on Windows](https://tailscale.com/kb/1022/install-windows). If you want to use the
Tailscale `.msi` installer, see [Install Tailscale on Windows with MSI](https://tailscale.com/kb/1189/install-windows-msi).

1. Verify that you are on WSL 2. From Powershell, run the following command: `wsl -l -v`. In the `VERSION` column you should see a `2`. This means you are using WSL 2.
2. Start your WSL 2 instance from Powershell by running `wsl.exe` or opening up a Linux terminal tab (if you have it already configured).
3. Run the automatic installation script:

```
curl -fsSL https://tailscale.com/install.sh | sh

```

You can find more detailed instructions in [Install Tailscale on Linux](https://tailscale.com/kb/1031/install-linux) page, including a manual installation process.

1. After the installation completes, Tailscale will not yet be running, so you will need to follow the text prompt after the installation and run `sudo tailscale up`. This will post a Tailscale URL that you can select or copy and paste into your browser.
2. When your browser window launches you will need to authenticate
   using [your SSO identity provider](https://tailscale.com/kb/1013/sso-providers).
3. Follow the prompts to add this node to your tailnet and you should see your new WSL 2 node in the [**Machines**](https://login.tailscale.com/admin/machines) shortly.

Users can uninstall Tailscale by running the following command: `sudo apt-get remove tailscale`.

* Your new WSL 2 node will most likely have the same name as your Windows node and it might show up in the Tailscale admin page as a duplicate name or with an appended number. You can rename your node in the Tailscale [**Machines**](https://login.tailscale.com/admin/machines) page to reflect that it is your WSL 2 node.
* If you run Tailscale on both the Windows host and inside WSL 2 at the same time, Tailscale encrypted traffic that flows from WSL 2 over Tailscale on the Windows host will not work due to Tailscale packets not being able to fit in Tailscale packets. For this reason it is recommended that users run Tailscale on the Windows host only, and not inside WSL 2.
* If you run Tailscale inside WSL 2, the current versions of WSL 2 have a default `MTU` of `1280` on their default interface, which is not large enough for Tailscale to function. There is a workaround inside `tailscaled` that will raise the `MTU` of the default interface to `1340` if it detects that you're on WSL and it is using what appears to be this default `MTU`.
