#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
# ]
# ///
import argparse
import subprocess
import os
import sys
from PIL import Image, ImageDraw, ImageFont

def main():
    parser = argparse.ArgumentParser(description="Generate a Pinterest pin with text overlay (Jarvis Brand Style)")
    parser.add_argument("--title", required=True, help="Title text (e.g. '3-6 MONTH MILESTONES')")
    parser.add_argument("--keywords", required=True, help="Keywords (e.g. 'ROLLING OVER, GRABBING TOYS, GIGGLING')")
    parser.add_argument("--bullets", required=True, help="Bullet points (comma separated)")
    parser.add_argument("--prompt", required=True, help="Prompt for background image")
    parser.add_argument("--output", required=True, help="Output filename")
    parser.add_argument("--api-key", help="Gemini API key")
    
    args = parser.parse_args()
    
    # 1. Generate base image
    temp_bg = "temp_bg.png"
    gen_cmd = [
        "uv", "run", "/app/skills/nano-banana-pro/scripts/generate_image.py",
        "--prompt", f"{args.prompt}, high-quality photography, parenting lifestyle, warm lighting, soft focus background, vertical orientation",
        "--filename", temp_bg,
        "--aspect-ratio", "9:16"
    ]
    if args.api_key:
        gen_cmd.extend(["--api-key", args.api_key])
    
    print(f"Generating background with prompt: {args.prompt}")
    try:
        subprocess.run(gen_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating background: {e}", file=sys.stderr)
        sys.exit(1)
    
    # 2. Setup Canvas
    W, H = 1000, 1500
    BEIGE = (233, 224, 217)
    WHITE = (255, 255, 255)
    HEAD_COLOR = (51, 51, 51)
    BODY_COLOR = (74, 74, 74)
    
    # Load and crop background
    src = Image.open(temp_bg).convert("RGB")
    sw, sh = src.size
    scale = max(W / sw, H / sh)
    new_size = (int(sw * scale), int(sh * scale))
    src_resized = src.resize(new_size, Image.Resampling.LANCZOS)
    left = (new_size[0] - W) // 2
    top = (new_size[1] - H) // 2
    img = src_resized.crop((left, top, left + W, top + H))
    
    draw = ImageDraw.Draw(img)
    
    # Right beige stripe
    right_margin = int(0.06 * W)
    draw.rectangle([W - right_margin, 0, W, H], fill=BEIGE)
    
    # White card
    card_left = int(0.54 * W)
    card_top = int(0.06 * H)
    card_right = W - right_margin
    card_bottom = H - int(0.06 * H)
    draw.rectangle([card_left, card_top, card_right, card_bottom], fill=WHITE)
    
    # Text Area
    pad_h = int(0.06 * (card_right - card_left))
    pad_top = int(0.08 * (card_bottom - card_top))
    text_area_left = card_left + pad_h
    text_area_right = card_right - pad_h
    text_area_width = text_area_right - text_area_left
    text_area_top = card_top + pad_top
    
    # Fonts
    serif_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    sans_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    
    HEAD_SIZE = int(0.064 * W)
    BODY_SIZE = int(0.028 * W)
    
    try:
        head_font = ImageFont.truetype(serif_font_path, HEAD_SIZE)
        body_font = ImageFont.truetype(sans_font_path, BODY_SIZE)
    except:
        head_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        
    # Helper to draw centered wrapped text
    def draw_centered_multiline(draw, text, font, x_left, y_top, max_width, fill, line_spacing=1.1):
        lines = []
        for line in text.split("\n"):
            words = line.split()
            if not words:
                lines.append("")
                continue
            current_line = words[0]
            for w in words[1:]:
                test = current_line + " " + w
                if draw.textlength(test, font=font) <= max_width:
                    current_line = test
                else:
                    lines.append(current_line)
                    current_line = w
            lines.append(current_line)
            
        y = y_top
        for line in lines:
            w_line = draw.textlength(line, font=font)
            x = x_left + (max_width - w_line) / 2
            draw.text((x, y), line, font=font, fill=fill)
            # Use textbbox to get actual height of the line
            bbox = draw.textbbox((x, y), line, font=font)
            y += (bbox[3] - bbox[1]) * line_spacing + 5
        return y

    # Combine Title and Keywords for the headline area
    # Style: Title in small caps/caps, Keywords in larger caps
    headline = f"{args.title}\n{args.keywords}".upper()
    
    # Draw Headline
    next_y = draw_centered_multiline(draw, headline, head_font, text_area_left, text_area_top, text_area_width, HEAD_COLOR, line_spacing=0.95)
    
    # Gap
    next_y += HEAD_SIZE * 1.5
    
    # Draw Bullets
    bullets = [b.strip() for b in args.bullets.split(",")]
    for bullet in bullets:
        bullet_text = f"• {bullet}"
        w_bullet = draw.textlength(bullet_text, font=body_font)
        x = text_area_left + (text_area_width - w_bullet) / 2
        draw.text((x, next_y), bullet_text, font=body_font, fill=BODY_COLOR)
        bbox = draw.textbbox((x, next_y), bullet_text, font=body_font)
        next_y += (bbox[3] - bbox[1]) * 1.5 + 5
        
    # Save final
    img.save(args.output)
    print(f"Pin saved to {args.output}")
    print(f"MEDIA: {os.path.abspath(args.output)}")
    
    # Cleanup
    if os.path.exists(temp_bg):
        os.remove(temp_bg)

if __name__ == "__main__":
    main()
