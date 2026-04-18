import asyncio
from playwright.async_api import async_playwright
import os
import time
import argparse

async def capture_showcase(url, output_dir, interactions=None):
    """
    Generalized Playwright capture script.
    
    Args:
        url: The root URL of the application.
        output_dir: Where to save screenshots.
        interactions: List of dicts with {action, selector, value, filename}
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        os.makedirs(output_dir, exist_ok=True)
        print(f"🎬 Starting UI Capture for {url}...")
        
        try:
            await page.goto(url)
            await asyncio.sleep(5) # Base wait for hydration
            
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
            await browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:8501")
    parser.add_argument("--dir", default="showcase")
    args = parser.parse_args()
    
    asyncio.run(capture_showcase(args.url, args.dir))
