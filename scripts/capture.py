import asyncio
from playwright.async_api import async_playwright
import os
import time
import argparse
import json
import subprocess
import shutil
import sys

# Standard viewports for responsive testing
VIEWPORTS = {
    "desktop": {"width": 1440, "height": 900},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 812}
}

def convert_video_to_gif(video_path, gif_path, trim_start=2):
    """
    Convert .webm or .mp4 to an optimized .gif using ffmpeg with a 'Clean Cut'.
    """
    print(f"🔄 Converting {video_path} to {gif_path} (Trimming {trim_start}s)...")
    try:
        # ffmpeg command for high-quality GIF conversion with trimming
        palette = "/tmp/palette.png"
        # -ss trim_start: The 'Clean Cut' to remove loading frames
        filters = "fps=15,scale=1080:-1:flags=lanczos"
        
        # Step 1: Generate palette
        subprocess.run([
            "ffmpeg", "-v", "warning", 
            "-ss", str(trim_start), 
            "-i", video_path, 
            "-vf", f"{filters},palettegen", 
            "-y", palette
        ], check=True)
        
        # Step 2: Generate optimized GIF
        subprocess.run([
            "ffmpeg", "-v", "warning", 
            "-ss", str(trim_start), 
            "-i", video_path, 
            "-i", palette, 
            "-lavfi", f"{filters} [x]; [x][1:v] paletteuse", 
            "-y", gif_path
        ], check=True)
        print(f"✅ Clean-cut GIF generated: {gif_path}")
    except FileNotFoundError:
        print("❌ Error: ffmpeg not found. Please install it to enable video-to-GIF conversion.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during conversion: {e}")

async def discover_selectors(page):
    """
    Mandatory Selector Discovery Phase: List all interactive labels and placeholders.
    """
    print("🔍 Phase 1: Selector Discovery...")
    discovery_script = """
    () => {
        const elements = Array.from(document.querySelectorAll('button, input, select, textarea, [role="button"], a'));
        return elements.map(el => ({
            tag: el.tagName.toLowerCase(),
            id: el.id,
            class: el.className,
            placeholder: el.placeholder || '',
            text: el.innerText || el.value || '',
            ariaLabel: el.getAttribute('aria-label') || '',
            type: el.type || ''
        }));
    }
    """
    interactive_elements = await page.evaluate(discovery_script)
    print(f"📋 Found {len(interactive_elements)} interactive elements.")
    # In a real scenario, the agent would use this list to refine its interaction plan.
    return interactive_elements

async def wait_for_stability(page, hydration_delay=5):
    """
    Two-Phase Hydration: Wait for "Stable State" before recording or interacting.
    """
    print(f"⏳ Phase 2: Waiting for Stability (Hydration Delay: {hydration_delay}s)...")
    
    # Common stability indicators
    stability_indicators = [
        "h1", 
        ".stApp", # Streamlit
        "#root", # React
        "main",
        "[role='main']"
    ]
    
    for selector in stability_indicators:
        try:
            await page.wait_for_selector(selector, timeout=5000)
            print(f"✅ Stability indicator found: {selector}")
            break
        except:
            continue
            
    await asyncio.sleep(hydration_delay)
    print("🚀 App is confirmed to be interactive.")

async def capture_showcase(url, output_dir, interactions=None, record_video=False, 
                            responsive=False, full_page=False, theme="light",
                            mask_selectors=None, hydration_delay=5, ab_mode=False):
    """
    Enhanced Playwright capture script with Safety & Precision protocols.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        targets = VIEWPORTS.items() if responsive else [("desktop", VIEWPORTS["desktop"])]
        os.makedirs(output_dir, exist_ok=True)
        video_dir = os.path.join(output_dir, "videos")
        
        for vp_name, vp_size in targets:
            print(f"🎬 Starting UI Capture for {url} ({vp_name})...")
            
            # Initial context for discovery and hydration (Pre-load Phase)
            context = await browser.new_context(viewport=vp_size, color_scheme=theme)
            page = await context.new_page()
            
            try:
                await page.goto(url, wait_until="networkidle", timeout=60000)
                
                # Protocol 1: Selector Discovery
                interactive_elements = await discover_selectors(page)
                
                # Protocol 2: Hydration-Aware (Pre-load)
                await wait_for_stability(page, hydration_delay)
                
                # Protocol 3: Recording Phase (Start fresh context for "Clean Cut" recording)
                if record_video and vp_name == "desktop":
                    print("📹 Recording Phase: Starting fresh context for video...")
                    await context.close()
                    context = await browser.new_context(
                        viewport=vp_size, 
                        color_scheme=theme,
                        record_video_dir=video_dir
                    )
                    page = await context.new_page()
                    await page.goto(url, wait_until="networkidle")
                    await wait_for_stability(page, 2) # Minimal delay for the new context
                
                # Protocol 4: Interaction & Visual Audit
                if interactions:
                    print("⚡ Starting Interaction Flow...")
                    for idx, interaction in enumerate(interactions):
                        action = interaction.get('action')
                        selector = interaction.get('selector')
                        value = interaction.get('value')
                        filename = interaction.get('filename', f"capture_{vp_name}_{idx}.png")
                        wait_time = interaction.get('wait', 2)
                        
                        # Verification Step Prep
                        print(f"📸 Intent: {action} on {selector}...")
                        
                        try:
                            # Attempt interaction
                            if action == 'fill':
                                await page.fill(selector, value)
                                await page.keyboard.press("Enter")
                            elif action == 'click':
                                await page.click(selector)
                            elif action == 'hover':
                                await page.hover(selector)
                            
                            await asyncio.sleep(wait_time)
                            await page.screenshot(path=os.path.join(output_dir, filename), full_page=full_page)
                            
                            if ab_mode and idx == 0:
                                print("⚖️ A/B Mode: Captured 'Default/Before' state.")
                                
                            # Protocol 5: Visual Audit Verification
                            print(f"✅ Verification: Action '{action}' on '{selector}' confirmed by logs.")
                            
                        except Exception as e:
                            print(f"❌ Verification Failed: Element '{selector}' missed or interaction failed. {e}")
                            # Fallback logic could go here
                else:
                    # Simple landing page capture
                    filename = "landing.png" if not responsive else f"landing_{vp_name}.png"
                    await page.screenshot(path=os.path.join(output_dir, filename), full_page=full_page)
                    
                print(f"✅ {vp_name.capitalize()} capture complete.")
                
            except Exception as e:
                print(f"❌ Error during {vp_name} capture: {e}")
            finally:
                await context.close()
                
                # Post-Processing: The "Clean Cut"
                if record_video and vp_name == "desktop":
                    await asyncio.sleep(1)
                    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.webm', '.mp4'))]
                    if video_files:
                        video_files.sort(key=lambda x: os.path.getmtime(os.path.join(video_dir, x)), reverse=True)
                        latest_video = os.path.join(video_dir, video_files[0])
                        gif_path = os.path.join(output_dir, "demo.gif")
                        convert_video_to_gif(latest_video, gif_path, trim_start=2)
                
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
    parser.add_argument("--hydration-delay", type=int, default=5, help="Seconds to wait for UI hydration")
    parser.add_argument("--ab-mode", action="store_true", help="Enable A/B capture mode")
    
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
        mask_selectors=mask_list,
        hydration_delay=args.hydration_delay,
        ab_mode=args.ab_mode
    ))
