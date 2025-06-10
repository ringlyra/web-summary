const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const root = process.cwd();

// Collect year directories like 2025, 2023
const yearDirs = fs
  .readdirSync(root)
  .filter((name) => /^\d{4}$/.test(name))
  .filter((name) => fs.statSync(path.join(root, name)).isDirectory());

if (yearDirs.length === 0) {
  console.error("No year directories found.");
  process.exit(1);
}

// Build globs for Prettier
const globs = yearDirs.map((dir) => `"${dir}/**/*"`).join(" ");

const cmd = `npx prettier --write ${globs}`;
console.log(cmd);
execSync(cmd, { stdio: "inherit", shell: true });
