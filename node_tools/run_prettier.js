const { execSync } = require("child_process");

const summariesGlob = 'Summary/**/*.md';
const cmd = `npx prettier --write '${summariesGlob}'`;
console.log(cmd);
execSync(cmd, { stdio: "inherit", shell: true });
