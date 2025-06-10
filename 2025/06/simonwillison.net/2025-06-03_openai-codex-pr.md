<!-- metadata -->

- **title**: PR #537: Fix Markdown in og descriptions
- **source**: https://simonwillison.net/2025/Jun/3/openai-codex-pr/
- **author**: Simon Willison
- **published**: 2025-06-03T23:58:00Z
- **fetched**: 2025-06-04T04:26:27Z
- **tags**: codex, ai-agents, openai, ai, llms, ai-assisted-programming, generative-ai, chatgpt, github, testing, postgresql
- **image**: https://static.simonwillison.net/static/2025/codex-fix.jpg

## 要約

**OpenAI Codex** を活用し自ブログの **OGP** 説明文のMarkdownを除去する **GitHub** PRを作成し、Codexのエージェント活用事例を紹介。

## 本文 / Article

**[PR #537: Fix Markdown in og descriptions](https://github.com/simonw/simonwillisonblog/pull/537)**. Since [OpenAI Codex](https://openai.com/index/introducing-codex/) is now available to us ChatGPT Plus subscribers I decided to try it out against my blog.

It's a very nice implementation of the GitHub-connected coding "agent" pattern, as also seen in Google's [Jules](https://jules.google/) and Microsoft's [Copilot Coding Agent](https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/).

First I had to configure an environment for it. My Django blog uses PostgreSQL which isn't part of the [default Codex container](https://github.com/openai/codex-universal), so I had Claude Sonnet 4 [help me](https://claude.ai/share/a5ce65c2-a9a4-4ae7-b645-71bd9fd6ea2c) come up with a startup recipe to get PostgreSQL working.

I attached my [simonw/simonwillisonblog](https://github.com/simonw/simonwillisonblog) GitHub repo and used the following as the "setup script" for the environment:

```
# Install PostgreSQL
apt-get update && apt-get install -y postgresql postgresql-contrib

# Start PostgreSQL service
service postgresql start

# Create a test database and user
sudo -u postgres createdb simonwillisonblog
sudo -u postgres psql -c "CREATE USER testuser WITH PASSWORD 'testpass';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE simonwillisonblog TO testuser;"
sudo -u postgres psql -c "ALTER USER testuser CREATEDB;"

pip install -r requirements.txt

```

I left "Agent internet access" off for reasons [described previously](https://simonwillison.net/2025/Jun/3/codex-agent-internet-access/).

Then I prompted Codex with the following (after one previous experimental task to check that it could run my tests):

> Notes and blogmarks can both use Markdown.
>
> They serve `meta property="og:description" content="` tags on the page, but those tags include that raw Markdown which looks bad on social media previews.
>
> Fix it so they instead use just the text with markdown stripped - so probably render it to HTML and then strip the HTML tags.
>
> Include passing tests.
>
> Try to run the tests, the postgresql details are:
>
> database = simonwillisonblog
> username = testuser
> password = testpass
>
> Put those in the DATABASE_URL environment variable.

I left it to churn away for a few minutes (4m12s, to be precise) and [it came back](https://chatgpt.com/s/cd_683f8b81657881919a8d1ce71978a2df) with a fix that edited two templates and added one more (passing) test. Here's [that change in full](https://github.com/simonw/simonwillisonblog/pull/537/files).

And sure enough, the social media cards for my posts now look like this - no visible Markdown any more:

![Screenshot of a web browser showing a blog post preview card on Bluesky. The URL in the address bar reads "https://simonwillison.net/2025/Jun/3/pr-537-fix-markdown-in-og-descriptions/". The preview card shows the title "PR #537: Fix Markdown in og descriptions" and begins with the text "Since OpenAI Codex is now available to us ChatGPT Plus subscribers I decided to try it out against my blog. It's a very nice implementation of the GitHub-connected coding". The domain "simonwillison.net" appears at the bottom of the card.](https://static.simonwillison.net/static/2025/codex-fix.jpg)
