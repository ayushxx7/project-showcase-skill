import asyncio
from playwright.async_api import async_playwright
import os
import time
import argparse
import json

# Standard viewports for responsive testing
VIEWPORTS = {
    "desktop": {"width": 1440, "height": 900},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 812}
}

async def capture_showcase(url, output_dir, interactions=None, record_video=False, 
                            responsive=False, full_page=False, theme="light",
                            mask_selectors=None):
    """
    Enhanced Playwright capture script for professional showcases.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Determine viewports to capture
        targets = VIEWPORTS.items() if responsive else [("desktop", VIEWPORTS["desktop"])]
        
        os.makedirs(output_dir, exist_ok=True)
        if record_video:
            os.makedirs(os.path.join(output_dir, "videos"), exist_ok=True)

        for vp_name, vp_size in targets:
            print(f"🎬 Starting UI Capture for {url} ({vp_name})...")
            
            context_args = {
                'viewport': vp_size,
                'color_scheme': theme
            }
            
            if record_video and vp_name == "desktop":
                context_args['record_video_dir'] = os.path.join(output_dir, "videos/")
            
            context = await browser.new_context(**context_args)
            page = await context.new_page()
            
            try:
                # Use networkidle for more reliable captures
                await page.goto(url, wait_until="networkidle", timeout=60000)
                await asyncio.sleep(2) # Extra buffer for animations/late hydration
                
                # Simple Verification: Check for 404 or page errors
                title = await page.title()
                if "404" in title or "Not Found" in title:
                    print(f"⚠️ Warning: Possible 404 detected ('{title}').")

                # Apply masking if selectors provided
                if mask_selectors:
                    for selector in mask_selectors:
                        try:
                            elements = await page.query_selector_all(selector)
                            for el in elements:
                                await el.evaluate("el => el.style.filter = 'blur(8px)'")
                        except Exception as e:
                            print(f"⚠️ Could not mask {selector}: {e}")

                if interactions:
                    for idx, interaction in enumerate(interactions):
                        action = interaction.get('action')
                        selector = interaction.get('selector')
                        value = interaction.get('value')
                        filename = interaction.get('filename', f"capture_{vp_name}_{idx}.png")
                        wait_time = interaction.get('wait', 2)
                        
                        print(f"📸 Action: {action} on {selector}...")
                        
                        try:
                            if action == 'fill':
                                await page.fill(selector, value)
                                await page.keyboard.press("Enter")
                            elif action == 'click':
                                await page.click(selector)
                            elif action == 'hover':
                                await page.hover(selector)
                            
                            await asyncio.sleep(wait_time)
                            await page.screenshot(path=os.path.join(output_dir, filename), full_page=full_page)
                        except Exception as e:
                            print(f"❌ Interaction failed: {e}")
                else:
                    # Simple landing page capture
                    filename = "landing.png" if not responsive else f"landing_{vp_name}.png"
                    await page.screenshot(path=os.path.join(output_dir, filename), full_page=full_page)
                    
                print(f"✅ {vp_name.capitalize()} capture complete.")
                
            except Exception as e:
                print(f"❌ Error during {vp_name} capture: {e}")
            finally:
                await context.close()
                
        await browser.close()
        print(f"🎉 All captures complete. Files in {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:8501")
    parser.add_argument("--dir", default="showcase")
    parser.add_argument("--record-video", action="store_true", help="Record video of the capture")
    parser.add_argument("--responsive", action="store_true", help="Capture Desktop, Tablet, and Mobile")
    parser.add_argument("--full-page", action="store_true", help="Take full page screenshots")
    parser.add_argument("--theme", choices=["light", "dark"], default="light", help="Color scheme (light/dark)")
    parser.add_argument("--mask", help="Comma-separated selectors to mask (e.g. '.api-key,.user-email')")
    parser.add_argument("--interactions", help="JSON string of interactions")
    
    args = parser.parse_args()
    
    mask_list = args.mask.split(",") if args.mask else None
    interactions_list = json.loads(args.interactions) if args.interactions else None
    
    asyncio.run(capture_showcase(
        args.url, 
        args.dir, 
        interactions=interactions_list,
        record_video=args.record_video,
        responsive=args.responsive,
        full_page=args.full_page,
        theme=args.theme,
        mask_selectors=mask_list
    ))
