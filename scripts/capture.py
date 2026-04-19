import asyncio
from playwright.async_api import async_playwright
import os
import time
import argparse

async def capture_showcase(url, output_dir, interactions=None, record_video=False):
    """
    Generalized Playwright capture script.
    
    Args:
        url: The root URL of the application.
        output_dir: Where to save screenshots.
        interactions: List of dicts with {action, selector, value, filename}
        record_video: Whether to record a video of the capture.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        context_args = {'viewport': {'width': 1440, 'height': 900}}
        if record_video:
            context_args['record_video_dir'] = os.path.join(output_dir, "videos/")
            
        context = await browser.new_context(**context_args)
        page = await context.new_page()
        
        os.makedirs(output_dir, exist_ok=True)
        print(f"🎬 Starting UI Capture for {url}...")
        
        try:
            await page.goto(url)
            await asyncio.sleep(5) # Base wait for hydration
            
            # Simple Verification: Check for 404 or page errors
            title = await page.title()
            if "404" in title or "Not Found" in title:
                print(f"⚠️ Warning: Possible 404 detected ('{title}').")
                # Suggesting a retry or different path to the agent
            
            if interactions:
                for idx, interaction in enumerate(interactions):
                    action = interaction.get('action')
                    selector = interaction.get('selector')
                    value = interaction.get('value')
                    filename = interaction.get('filename', f"capture_{idx}.png")
                    wait_time = interaction.get('wait', 2)
                    
                    print(f"📸 Action: {action} on {selector}...")
                    
                    if action == 'fill':
                        await page.fill(selector, value)
                        await page.keyboard.press("Enter")
                    elif action == 'click':
                        await page.click(selector)
                    
                    await asyncio.sleep(wait_time)
                    await page.screenshot(path=os.path.join(output_dir, filename))
            else:
                # Simple landing page capture
                await page.screenshot(path=os.path.join(output_dir, "landing.png"))
                
            print(f"✅ Capture complete. Files in {output_dir}")
            
        except Exception as e:
            print(f"❌ Error during capture: {e}")
        finally:
            await context.close()
            await browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:8501")
    parser.add_argument("--dir", default="showcase")
    parser.add_argument("--record-video", action="store_true", help="Record video of the capture")
    args = parser.parse_args()
    
    asyncio.run(capture_showcase(args.url, args.dir, record_video=args.record_video))
