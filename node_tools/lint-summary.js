#!/usr/bin/env node
// lint-summary.js
//
// Summary/**/*.md を対象に
//   1. Prettier で整形 (--write)
//   2. textlint でエラーのみ検出 (--quiet)
// 終了コード: textlint でエラーがあれば非ゼロ

const { execSync } = require("child_process");

const summariesGlob = 'Summary/**/*.md';

// --- 1) Prettier -------------------------------------------------
const prettierCmd = `npx prettier --write "${summariesGlob}"`;
console.log(`\n> ${prettierCmd}`);
execSync(prettierCmd, { stdio: "inherit", shell: true });

// --- 2) textlint (errors only) -----------------------------------
const textlintCmd = `npx textlint --quiet "${summariesGlob}"`;
console.log(`\n> ${textlintCmd}`);

try {
  execSync(textlintCmd, { stdio: "inherit", shell: true });
} catch (err) {
  // textlint がエラーを検出するとここに来る
  console.error("\ntextlint found errors above.");
  // CI などで失敗を検知できるよう終了コードを引き継ぐ
  process.exitCode = err.status ?? 1;
}
