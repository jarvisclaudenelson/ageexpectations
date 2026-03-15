#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
# ]
# ///
"""
Generate Pinterest pins in the Jarvis brand style.
Supports multiple layouts and prevents text overflow.
"""
import argparse
import subprocess
import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont

def main():
    parser = argparse.ArgumentParser(description="Generate a Pinterest pin (Jarvis Brand Style)")
    parser.add_argument("--title", required=True, help="Title (e.g. '3-6 MONTH MILESTONES:')")
    parser.add_argument("--headline", required=True, help="Main headline")
    parser.add_argument("--bullets", required=True, help="Bullet points (comma separated)")
    parser.add_argument("--prompt", required=True, help="Prompt for background image")
    parser.add_argument("--output", required=True, help="Output filename")
    parser.add_argument("--layout", default="split", choices=["split", "overlay", "card-bottom"], help="Layout style")
    parser.add_argument("--rotate", type=int, default=0, help="Rotate background image (degrees counter-clockwise)")
    parser.add_argument("--api-key", help="Gemini API key")
    
    args = parser.parse_args()
    
    W, H = 1024, 1792
    BEIGE = (245, 240, 235)
    WHITE = (255, 255, 255)
    TITLE_COLOR = (60, 60, 60)
    HEADLINE_COLOR = (40, 40, 40)
    BULLET_COLOR = (80, 80, 80)
    
    # 1. Generate background
    temp_bg = f"temp_bg_{os.getpid()}.png"
    gen_prompt = f"{args.prompt}, professional photography, high quality, soft natural light"
    
    gen_cmd = [
        "uv", "run", "/app/skills/nano-banana-pro/scripts/generate_image.py",
        "--prompt", gen_prompt,
        "--filename", temp_bg,
        "--resolution", "1K"
    ]
    if args.api_key:
        gen_cmd.extend(["--api-key", args.api_key])
    
    print(f"Generating background...")
    subprocess.run(gen_cmd, check=True, capture_output=True)
    
    # 2. Setup Canvas
    img = Image.new('RGB', (W, H), WHITE)
    draw = ImageDraw.Draw(img)
    
    bg = Image.open(temp_bg).convert('RGB')
    
    # Check EXIF orientation and fix it
    try:
        from PIL import ImageOps
        bg = ImageOps.exif_transpose(bg)
    except:
        pass

    # Apply manual rotation if specified
    if args.rotate != 0:
        bg = bg.rotate(args.rotate, expand=True)

    bg_w, bg_h = bg.size
        
    # Layout configuration
    if args.layout == "split":
        photo_w = int(W * 0.55)
        card_x, card_y = photo_w, int(H * 0.06)
        card_w, card_h = W - photo_w - int(W * 0.04), H - int(H * 0.12)
        stripe_w = int(W * 0.04)
        
        # Paste photo
        scale = max(photo_w / bg_w, H / bg_h)
        bg_s = bg.resize((int(bg_w * scale), int(bg_h * scale)), Image.Resampling.LANCZOS)
        img.paste(bg_s.crop(((bg_s.width - photo_w)//2, (bg_s.height - H)//2, (bg_s.width + photo_w)//2, (bg_s.height + H)//2)), (0,0))
        
        # Draw stripe
        draw.rectangle([W - stripe_w, 0, W, H], fill=BEIGE)
        # Draw card
        draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill=WHITE)
        
    elif args.layout == "card-bottom":
        photo_h = int(H * 0.60)
        card_x, card_y = int(W * 0.10), photo_h - int(H * 0.05)
        card_w, card_h = int(W * 0.80), H - photo_h
        
        # Paste photo
        scale = max(W / bg_w, photo_h / bg_h)
        bg_s = bg.resize((int(bg_w * scale), int(bg_h * scale)), Image.Resampling.LANCZOS)
        img.paste(bg_s.crop(((bg_s.width - W)//2, 0, (bg_s.width + W)//2, photo_h)), (0,0))
        
        # Draw card
        draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill=WHITE)

    elif args.layout == "overlay":
        card_x, card_y = int(W * 0.10), int(H * 0.55)
        card_w, card_h = int(W * 0.80), int(H * 0.40)
        
        # Paste photo (full)
        scale = max(W / bg_w, H / bg_h)
        bg_s = bg.resize((int(bg_w * scale), int(bg_h * scale)), Image.Resampling.LANCZOS)
        img.paste(bg_s.crop(((bg_s.width - W)//2, (bg_s.height - H)//2, (bg_s.width + W)//2, (bg_s.height + H)//2)), (0,0))
        
        # Draw card (higher opacity white)
        overlay = Image.new('RGBA', (card_w, card_h), (255, 255, 255, 245)) # Increased to 245
        img.paste(overlay, (card_x, card_y), overlay)

    # 3. Text Fitting Logic
    pad_x = int(card_w * 0.10)
    text_w = card_w - (pad_x * 2)
    text_x = card_x + pad_x
    
    serif = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    serif_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    
    def get_layout(t_size, h_size, b_size):
        try:
            f_title = ImageFont.truetype(serif, t_size)
            f_head = ImageFont.truetype(serif_bold, h_size)
            f_bullet = ImageFont.truetype(sans, b_size)
        except:
            f_title = f_head = f_bullet = ImageFont.load_default()
            
        def wrap(text, font, max_w):
            words = text.split()
            lines = []
            if not words: return []
            curr = words[0]
            for w in words[1:]:
                if draw.textlength(curr + " " + w, font=font) <= max_w:
                    curr += " " + w
                else:
                    lines.append(curr)
                    curr = w
            lines.append(curr)
            return lines

        t_lines = wrap(args.title.upper(), f_title, text_w)
        h_lines = wrap(args.headline.upper(), f_head, text_w)
        b_items = [f"• {b.strip()}" for b in args.bullets.split(",")]
        
        # Measure height
        def get_h(lines, font, spacing):
            if not lines: return 0
            h = 0
            for l in lines:
                bbox = draw.textbbox((0,0), l, font=font)
                h += (bbox[3] - bbox[1]) * spacing
            return h
            
        th = get_h(t_lines, f_title, 1.3)
        hh = get_h(h_lines, f_head, 1.1)
        bh = get_h(b_items, f_bullet, 1.5)
        
        gap1, gap2 = h_size * 0.8, h_size * 1.0
        total_h = th + hh + bh + gap1 + gap2
        return total_h, t_lines, h_lines, b_items, f_title, f_head, f_bullet, gap1, gap2

    # Fit text by scaling down
    t_sz, h_sz, b_sz = 40, 68, 32 # Slightly smaller starting point for split
    if args.layout != "split": 
        t_sz, h_sz, b_sz = 46, 80, 36
        
    for _ in range(12): # More iterations
        total_h, t_lines, h_lines, b_items, f_t, f_h, f_b, g1, g2 = get_layout(t_sz, h_sz, b_sz)
        if total_h <= card_h * 0.85: # More breathing room (85% instead of 90%)
            break
        t_sz = int(t_sz * 0.9)
        h_sz = int(h_sz * 0.9)
        b_sz = int(b_sz * 0.9)

    # 4. Draw Text
    curr_y = card_y + (card_h - total_h) / 2
    
    def draw_centered(lines, font, y, color, spacing):
        for l in lines:
            w = draw.textlength(l, font=font)
            draw.text((text_x + (text_w - w)/2, y), l, font=font, fill=color)
            bbox = draw.textbbox((0,0), l, font=font)
            y += (bbox[3] - bbox[1]) * spacing
        return y

    curr_y = draw_centered(t_lines, f_t, curr_y, TITLE_COLOR, 1.3)
    curr_y += g1
    curr_y = draw_centered(h_lines, f_h, curr_y, HEADLINE_COLOR, 1.1)
    curr_y += g2
    curr_y = draw_centered(b_items, f_b, curr_y, BULLET_COLOR, 1.5)
    
    img.save(args.output)
    print(f"Pin saved: {args.output} (Layout: {args.layout})")
    print(f"MEDIA: {os.path.abspath(args.output)}")
    if os.path.exists(temp_bg): os.remove(temp_bg)

if __name__ == "__main__":
    main()
