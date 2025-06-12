const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const root = process.cwd();
const summariesRoot = path.join(root, "Summary");

// Collect year directories like 2025, 2023 inside Summary/
const yearDirs = fs
  .readdirSync(summariesRoot)
  .filter((name) => /^\d{4}$/.test(name))
  .filter((name) => fs.statSync(path.join(summariesRoot, name)).isDirectory())
  .map((name) => path.join("Summary", name));

if (yearDirs.length === 0) {
  console.error("No year directories found.");
  process.exit(1);
}

// Build globs for Prettier
const globs = yearDirs.map((dir) => `"${dir}/**/*"`).join(" ");

const cmd = `npx prettier --write ${globs}`;
console.log(cmd);
execSync(cmd, { stdio: "inherit", shell: true });
