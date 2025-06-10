<!-- metadata -->

- **title**: Hack the model: Build AI security skills with the GitHub Secure Code Game - The GitHub Blog
- **source**: https://github.blog/security/hack-the-model-build-ai-security-skills-with-the-github-secure-code-game/
- **author**: Joseph Katsioloudes, Jaroslav Lobacevski, Greg Ose, Man Yue Mo
- **published**: 2025-06-03T16:37:03+00:00
- **fetched**: 2025-06-04T13:21:57Z
- **tags**: codex, ai, security, game, github
- **image**: https://github.blog/wp-content/uploads/2025/04/wallpaper_github_generic_1.png

## 要約

GitHubはソフトウェア開発者向けの無料学習コース「Secure Code Game」のシーズン3を公開した。今回はAIがもたらすセキュリティ課題に焦点を当て、悪意あるプロンプトを作ってLLMの脆弱性を突く攻撃者視点から始め、最終的には防御策を実装していく。各レベルではシステムプロンプト設計、出力検証、入力フィルタリング、自己検証などの手法を段階的に学べる。またオープンソースの貢献者が作ったHackMerlinをベースにより実践的なシナリオを備える。リポジトリを公開しており、誰でもチャレンジや改善に参加可能。

## 本文 / Article

We just launched season three of the GitHub Secure Code Game, and this time we’re putting you face to face with the security risks introduced by artificial intelligence. Get ready to learn by doing and have fun doing it! First, you’ll step into the shoes of an adversary crafting malicious prompts. Then, you’ll secure your application against those attacks.

The [Secure Code Game](https://gh.io/securecodegame) is a free software security course suitable for all developer levels, where players fix intentionally vulnerable code to build code security skills. By placing gameplay directly in the code editor—a developer’s natural habitat—it helps them practice spotting vulnerabilities where they normally work. Its straightforward setup allows players to start in under two minutes using Codespaces.

We launched the [first season](https://github.blog/developer-skills/github/build-a-secure-code-mindset-with-the-github-secure-code-game/) of the Secure Code Game in March 2023 to fill a gap in developer training, where security often takes a backseat to functionality. To grab attention, we presented seemingly flawless code snippets riddled with critical vulnerabilities, like the [OWASP Top 10](https://owasp.org/www-project-top-ten/). We then gamified the learning by challenging players to efficiently fix these issues without introducing new ones or missing edge cases. Supported by a strong community that contributed challenges, [season two](https://github.blog/developer-skills/application-development/build-code-security-skills-with-the-github-secure-code-game/) premiered a year later. Since then, over 10,000 developers across enterprise, open source, and education communities have played to sharpen their skills.

> This training was a one-of-a-kind experience. Initially, when I looked at the entire code file, I just thought it was completely normal. I didn’t see any flaws. The unit tests were completely normal, and the code seemed perfect. But the vulnerability was right in front of my eyes. It made me realize how much of a gap there is in identifying even the most basic flaws. It made me more cautious.
>
> Sanyam Mehta, Back-end developer

> This is a pretty fun way to learn! I would definitely recommend this game, as it helped me be more aware of the vulnerabilities out there.
>
> Tyler Anton, Computer science student

## Now’s the perfect time to elevate your skills!

Today, we’re excited to launch the [third season](https://github.com/skills/secure-code-game/tree/main/Season-3), which immerses players into the fascinating world of artificial intelligence through six realistic challenges. As the world moves decisively into a new era—McKinsey & Company reports that the use of generative AI increased from 33% in 2023 to 71% in 2024 and GitHub Copilot is now being used by more than 77,000 organizations—there’s no better time to enhance your skills.

## What you’ll learn

Each of the six security challenges focuses on a different defensive technique. The levels get progressively harder as they build on the defensive techniques of the previous ones. Some of the topics you’ll learn about include:

- **Crafting robust system prompts:** Securely design the initial instructions that guide the model’s behavior, ensuring desired, safe, and relevant outputs by setting its role, constraints, format, and context.
- **Output validation:** Prevent leaks by verifying that the output conforms to certain predefined rules, formats, or expectations.

- **Input filtering:** Examine, modify, or block user-provided text before it’s fed into the model to prevent harmful or irrelevant content from influencing the model as it generates output.

- **LLM self-verification:** Use this technique to have the Large Language Model (LLM) check its own output for accuracy, consistency, and compliance with defined rules or constraints. This may involve checking for errors, validating reasoning, or confirming adherence to policies. Self-verification can be prompted directly or built into the model’s response generation.

Progressing through season three requires players to hack LLMs. Each challenge begins with a set of guiding instructions for the LLM provided in the form of a code and a system message. These elements might include gaps or edge cases that could be exploited using a malicious prompt. Your task is to identify the vulnerabilities and craft prompts to manipulate the model into exposing a hidden secret.

[![video](https://github.blog/wp-content/uploads/2025/06/Screenshot-2025-06-02-at-11.52.51%E2%80%AFAM.png)](https://github.blog/wp-content/uploads/2025/06/s3-demo.mp4)

After exploiting the vulnerability, your next task is to refine the code and system message to prevent future leaks from those malicious prompts. You must do this while maintaining the functionality of the code.

> I learned to spot vulnerabilities, where and how they occur, and to correct them effectively before pushing them out to the world. I would absolutely recommend this training to anyone, not only in cybersecurity but software development too.
>
> Rajeev Mandalam, Application security at Boeing

> One of the major takeaways was that it’s good to focus on details because they could often lead to vulnerabilities that you wouldn’t have imagined. In terms of the format, I liked the fact that it didn’t focus on one particular programming language, and the whole emphasis is on the code concepts. I also liked how easy it was to navigate between game levels. The game provided me with a great new skillset to add to my professional journey.
>
> Reshmi Mehta, Security analyst at Alcon

## How to get started

If you’re eager to start learning, we’ve got a [Secure Code Game repository](https://github.com/skills/secure-code-game) all set up and ready to go. It includes instructions for all the seasons, so you can experience everything it has to offer. Just browse through the _README_ and get started.

## How season three came together

> Don’t wait to be an expert. Build, share, and the right people will find you. Open source changed my life, and it can do the same for you.
>
> Bartosz Gałek ([@bgalek](https://github.com/bgalek)), contributor of Secure Code Game season three

It all started in [FOSDEM 2025](https://fosdem.org/2025/) in Belgium, where I presented the Secure Code Game to a group of open source maintainers. [Bartosz](https://www.linkedin.com/in/bartosz-galek/) was in the audience and here’s what happened in his own words:

_The Secure Code Game immediately clicked, as security and game development is my thing! After the talk, I thanked Joseph on LinkedIn and shared [HackMerlin](https://hackmerlin.io/) with him—a game I created that challenges players to test their prompting skills. To my surprise, he liked it!_

_One thing led to another, and HackMerlin became the base of our collaboration for season three. The whole journey started as a silly idea, but it turned into something much bigger._

![Screenshot of an interactive game interface at Level 6. The game instructs the player to outsmart Merlin by asking clever questions to reveal a password. A cartoon wizard, Merlin, appears at the top, saying 'Hello traveler! Ask me anything...'. Below is a text box where the user can type questions, an 'Ask' button, and a field labeled 'Enter the secret password' followed by a 'Submit' button to check the validity of the answer.](https://github.blog/wp-content/uploads/2025/06/hackmerlin.png?resize=932%2C1240)

A key challenge in moving from HackMerlin’s UI-centric approach to the Secure Code Game’s code-first season three was ensuring user friendliness. HackMerlin’s backend provided an LLM gateway through the UI, abstracting much of the integration complexity—an area where GitHub products truly excel! Codespaces let us preconfigure the development environment and automate access to [GitHub Models](https://github.com/marketplace/models), a catalog and playground of AI models that provided us with built-in LLM integration.

Moreover, HackMerlin used an OpenAI model hosted on Azure, allowing for the game’s creator to adjust or disable the model’s provider default safeguards. In contrast, season three prioritized realism by adhering to the default safeguards of GitHub Models. Finally, GitHub Models made it easy for our players to switch between models and explore their differences.

What do you think? Do you have ideas for new challenges? Be our next contributor and help shape the next season of the game! See our [contribution guidelines](https://github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md) for details.

**Time to play!** Get ready to unleash your creativity on the challenges of season three! [Start playing now >](https://github.com/skills/secure-code-game/tree/main/Season-3)
