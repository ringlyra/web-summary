---
title: 'GitHub - coderabbitai/ast-grep-essentials: Community-led collection of essential ast-grep rules.'
source: https://github.com/coderabbitai/ast-grep-essentials
author:
  - github.com
published: ''
fetched: '2025-06-25T20:49:48.848602+00:00'
tags:
  - codex
  - github
image: https://opengraph.githubassets.com/92d1feace4a543b27ae543195139fb655b9775723fa079667e20c30332b98d7e/coderabbitai/ast-grep-essentials
---

## 要約

ast-grep-essentialsは、セキュリティ脆弱性の軽減や開発者のベストプラクティス遵守を支援するため、コミュニティ主導で作成されたast-grepルール集です。ルールはプログラミング言語やカテゴリ別に整理され、YAML形式でIDや言語、メッセージ、詳細説明、重大度、具体的なruleを記述します。testsディレクトリでは各言語向けのテストケースを提供し、正しい運用を保証します。ルールファイルはnoteやseverityなど公式ドキュメントに沿った項目を備え、utilsディレクトリには管理を補助する設定やスクリプトが含まれます。貢献する際は低誤検知率のルールを追加しプルリクエストを送り、議論はDiscord上で行われます。

## 本文

# AST-GREP Essentials

[![CodeRabbit Reviews](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.coderabbit.ai%2Fstats%2Fgithub%2Fcoderabbitai%2Fast-grep-essentials&query=%24.reviews&suffix=%20Reviews&style=for-the-badge&label=CodeRabbit&labelColor=%23FF570A&color=%2325BAB1)](https://app.coderabbit.ai/login)

## Overview

`ast-grep-essentials` is a community-led collection of
[`ast-grep`](https://ast-grep.github.io) rules to help developers mitigate
security vulnerabilities and enforce best practices in their codebases.

> [!TIP]
>
> Please read the CodeRabbit
> [documentation](https://docs.coderabbit.ai/guides/review-instructions) to
> understand how to use `ast-grep` in [CodeRabbit](https://coderabbit.ai)
> reviews.

## Structure

```plaintext
ast-grep-essentials
│
├── rules
│   ├── javascript
│   │   ├── jwt
│   │   │   ├── rule1.yml
│   │   │   ├── rule2.yml
│   │   │   └── ...
│   │   ├── ...
│   │   └── ...
│   └── go
│       ├── jwt-go
│       │   ├── rule1.yml
│
├── utils
│   ├── script1.yml
│   ├── script2.yml
│   └── ...
│
└── tests
    ├── javascript
    │   ├── rule1-test.yml
    │   ├── rule2-test.yml
    │   └── ...
    ├── ...
    └── ...
```

The package is organized into three main directories:

- `rules`: Contains `ast-grep` rules categorized by language and security
  category.
- `utils`: Houses utility configs to support rule management.
- `tests`: Includes test cases for validating the effectiveness of the rules
  across different languages.

### Rules Structure

Within the `rules` directory, you'll find the following structure:

- `language`: Each language supported by `ast-grep` (e.g., Python, JavaScript).
- `category`: Rules categorized based on security concerns (e.g., Input
  Validation, Authentication).

#### Rule file structure

> [!TIP]
>
> Read the `ast-grep` > documentation to understand the
> [rule configuration](https://ast-grep.github.io/reference/yaml.html) and the
> [rule object properties](https://ast-grep.github.io/reference/rule.html).

Each rule file should have the following structure:

```yaml
# Unique across the package, not just the language
id: rule-id
# The language property that the rule is going to get matched against
language: "language" # e.g., javaScript, go
# A short description of the rule
message: "Rule message"
# A more detailed explanation of the rule
note: "Rule note"
# Severity level of the rule (e.g., hint, warning)
severity: "severity"
# ast-grep rule property, check documentation for more information
rule: ...
```

### Tests Structure

Inside the `tests` directory, tests are organized by language:

- `language`: Test cases specific to the corresponding language's rules.
- `rule-file`: each test rule file should have by convention the
  `rule-file-name-test.yml` format.

> [!NOTE]
>
> Tests should follow the `ast-grep` testing rules format. Please refer to the
> `ast-grep`
> [documentation](https://ast-grep.github.io/guide/test-rule.html#test-case-configuration)

## Contributing

This project relies on the community to contribute rules. Please open a pull
request with your rules and tests. Please ensure that the rules are truly
essential and have a low false positive rate.

## Community

Join the discussion on our [Discord server](https://discord.gg/C3rGCxHn).
