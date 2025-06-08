import asyncio
from playwright.async_api import async_playwright

async def main():
    url = "https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction?hl=ja"
    output_file = "fetched_page.html"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto(url, wait_until="networkidle")
            content = await page.content()
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully fetched and saved HTML to {output_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
