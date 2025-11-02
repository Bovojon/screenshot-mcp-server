from playwright.async_api import async_playwright

async def capture(url: str, output_path: str = "screenshot.png") -> str | None:
    try:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            await page.screenshot(path=output_path)
            await browser.close()
        return output_path
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None
