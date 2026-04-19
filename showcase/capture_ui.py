import asyncio
from playwright.async_api import async_playwright
import os

async def capture_showcase(url, output_dir):
    """
    Enhanced automated browser capture with simple verification for project-showcase-skill.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # New: Video recording context enabled!
        context = await browser.new_context(
            viewport={'width': 1440, 'height': 900},
            record_video_dir=os.path.join(output_dir, "videos/")
        )
        page = await context.new_page()
        
        os.makedirs(output_dir, exist_ok=True)
        print(f"🎬 Starting UI Capture for {url}...")
        
        try:
            # 1. Landing
            response = await page.goto(url, timeout=60000)
            await page.wait_for_load_state("networkidle", timeout=60000)
            
            # --- Verification Step ---
            status = response.status
            title = await page.title()
            
            if status >= 400 or "404" in title or "Not Found" in title:
                print(f"❌ Error detected! Status: {status}, Title: {title}. Attempting auto-fix (retry with wait)...")
                await asyncio.sleep(5)
                await page.reload()
                await page.wait_for_load_state("networkidle")
            # -------------------------

            await page.screenshot(path=os.path.join(output_dir, "landing.png"))
            
            # 2. Interact (Simulate some scrolling or hover)
            await page.mouse.wheel(0, 500)
            await asyncio.sleep(2)
            await page.screenshot(path=os.path.join(output_dir, "scrolled.png"))
            
            print(f"✅ Capture complete. Files and videos in {output_dir}")
            
        except Exception as e:
            print(f"❌ Error during capture: {e}")
        finally:
            await context.close()
            await browser.close()

if __name__ == "__main__":
    # Pointing to the correct repository for this project!
    asyncio.run(capture_showcase("https://github.com/ayushxx7/project-showcase-skill", "showcase"))
