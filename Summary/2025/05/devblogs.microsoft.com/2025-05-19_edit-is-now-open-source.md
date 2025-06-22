---
title: 'Edit is now open source'
source: https://devblogs.microsoft.com/commandline/edit-is-now-open-source/
author:
  - Christopher Nguyen
published: '2025-05-19T16:04:35+00:00'
fetched: '2025-06-22T17:42:26.642231+00:00'
tags:
  - codex
  - microsoft
image: https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2025/05/Edit_24x.png
---

## 要約

MicrosoftはRust製の新しいコマンドラインエディター「Edit」をオープンソースで公開し、Windows 11の標準エディターとして組み込む計画だ。軽量でバイナリサイズは250kB以下、モデルレス設計でマウス操作も可能。複数ファイル切り替え、検索・置換、ワードラップなど基本機能を備え、GitHubからビルドまたはインストールできる。Windows Insider Programでプレビュー後に正式リリース予定。従来の「MS-DOS Editor」不在を補い、vimのような学習コストを避けて誰でも使えることを目指している。現在は早期版として公開され、公式リポジトリでフィードバックを受け付けている。

## 本文

What is Edit?
=============

Edit is a new command-line text editor in Windows. Edit is open source, so you can [build](https://github.com/microsoft/edit?tab=readme-ov-file#build-instructions) the code or [install](https://github.com/microsoft/edit?tab=readme-ov-file#installation) the latest version from [GitHub](https://github.com/microsoft/edit)!

This CLI text editor will be available to preview in the [Windows Insider Program](https://www.microsoft.com/windowsinsider/) in the coming months. After that, it will ship as part of Windows 11!

How to use Edit
===============

Open Edit by running `edit` in the command line or running `edit <your-file-name>`. With this, you will be able to edit files directly in the command line without context switching.

![Edit image](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2025/05/Edit.gif)

What are Edit’s features?
=========================

Edit is still in an early stage, but it has several features out of the box. Here are some highlights!

Lightweight
-----------

Edit is a small, lightweight text editor. It is less than 250kB, which allows it to keep a small footprint in the Windows 11 image.

Mouse Mode Support
------------------

As a modeless editor with a Text User Interface (TUI), all the menu options in Edit have keybindings (which you can see next to the menu options).

![Mouse Mode Support image](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2025/05/MouseModeSupport.gif)

Open Multiple Files
-------------------

You can open multiple files in Edit and switch between them with `Ctrl+P` (or by clicking the file list on the lower-right).

![Multi File Support image](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2025/05/MultiFileSupport.gif)

Find & Replace
--------------

You can find and replace text with `Ctrl+R` or select Edit > Replace in the TUI menu. There is also Match Case and Regular Expression support as well.

![Replace image](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2025/05/Replace.png)

Word Wrap
---------

Edit supports word wrapping. To use Word Wrap, you can use `Alt+Z` or select View > Word Wrap on the TUI menu.

![Word Wrap Mode image](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2025/05/WordWrapMode.gif)

Why build another CLI editor?
=============================

What motivated us to build Edit was the need for a default CLI text editor in 64-bit versions of Windows. 32-bit versions of Windows ship with the MS-DOS editor, but 64-bit versions do not have a CLI editor installed inbox. From there, we narrowed down our options…

Many of you are probably familiar with the “How do I exit vim?” meme. While it is relatively simple to learn the magic exit incantation, it’s certainly not a coincidence that this often turns up as a stumbling block for new and old programmers.

Because we wanted to avoid this for a built-in default editor, we decided that we wanted a modeless editor for Windows (versus a modal editor where new users would have to remember different modes of operation and how to switch between them).

This unfortunately limited our choices to a list of editors that either had no first-party support for Windows or were too big to bundle them with every version of the OS. As a result, Edit was born.

Happy Editing!
==============

Edit will be rolling out to the [Windows Insider Program](https://www.microsoft.com/windowsinsider/) in the coming months. Edit is now open source, so you can [build the code](https://github.com/microsoft/edit?tab=readme-ov-file#build-instructions) or [install it](https://github.com/microsoft/edit?tab=readme-ov-file#installation) from our GitHub repository.

If you have any feedback or questions, please reach out to the team on the official [Edit repository](https://github.com/microsoft/edit)!
