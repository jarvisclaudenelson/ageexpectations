#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
# ]
# ///
"""
Generate Pinterest pins in the Jarvis brand style.
Matches the 3-6 Month Milestones reference design:
- 1024x1792 (9:16 ratio for Pinterest)
- Photo on left (~55%), white card on right (~45%)
- Title + colon, large headline, bullet points
- All centered in white card
"""
import argparse
import subprocess
import os
import sys
from PIL import Image, ImageDraw, ImageFont

def main():
    parser = argparse.ArgumentParser(description="Generate a Pinterest pin (Jarvis Brand Style)")
    parser.add_argument("--title", required=True, help="Title with colon (e.g. '3-6 MONTH MILESTONES:')")
    parser.add_argument("--headline", required=True, help="Main headline (e.g. 'ROLLING OVER, GRABBING TOYS, GIGGLING.')")
    parser.add_argument("--bullets", required=True, help="Bullet points (comma separated)")
    parser.add_argument("--prompt", required=True, help="Prompt for background image")
    parser.add_argument("--output", required=True, help="Output filename")
    parser.add_argument("--api-key", help="Gemini API key")
    
    args = parser.parse_args()
    
    # Canvas size matching reference (9:16 Pinterest ratio)
    W, H = 1024, 1792
    
    # Brand colors
    BEIGE = (245, 240, 235)  # Light warm beige for stripe
    WHITE = (255, 255, 255)
    TITLE_COLOR = (60, 60, 60)  # Dark gray, not pure black
    HEADLINE_COLOR = (40, 40, 40)  # Slightly darker for headline
    BULLET_COLOR = (80, 80, 80)  # Medium gray for bullets
    
    # 1. Generate base image with vertical orientation
    temp_bg = f"temp_bg_{os.getpid()}.png"
    gen_prompt = f"{args.prompt}, professional parenting photography, soft natural lighting, warm tones, cozy home setting, high quality, 4:5 aspect ratio photo"
    
    gen_cmd = [
        "uv", "run", "/app/skills/nano-banana-pro/scripts/generate_image.py",
        "--prompt", gen_prompt,
        "--filename", temp_bg,
        "--resolution", "1K"
    ]
    if args.api_key:
        gen_cmd.extend(["--api-key", args.api_key])
    
    print(f"Generating background...")
    try:
        subprocess.run(gen_cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating background: {e}", file=sys.stderr)
        sys.exit(1)
    
    # 2. Create canvas and load background
    img = Image.new('RGB', (W, H), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Load and resize background to fill left portion
    bg = Image.open(temp_bg).convert('RGB')
    bg_w, bg_h = bg.size
    
    # Check if background is sideways and fix if needed
    if bg_w > bg_h:
        # Landscape orientation - rotate to portrait
        bg = bg.rotate(-90, expand=True)
        bg_w, bg_h = bg.size
    
    # Calculate crop to fill left 55% of canvas
    target_w = int(W * 0.55)
    target_h = H
    
    # Resize background to cover the target area
    scale = max(target_w / bg_w, target_h / bg_h)
    new_w = int(bg_w * scale)
    new_h = int(bg_h * scale)
    bg_resized = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Center crop
    crop_left = (new_w - target_w) // 2
    crop_top = (new_h - target_h) // 2
    bg_cropped = bg_resized.crop((crop_left, crop_top, crop_left + target_w, crop_top + target_h))
    
    # Paste background on left
    img.paste(bg_cropped, (0, 0))
    
    # 3. Draw right side elements
    # Beige stripe at far right (4%)
    stripe_w = int(W * 0.04)
    draw.rectangle([W - stripe_w, 0, W, H], fill=BEIGE)
    
    # White card (40% width, centered vertically with 6% margins)
    card_w = int(W * 0.40)
    card_h = H - int(H * 0.12)  # 6% margin top and bottom
    card_x = int(W * 0.55)  # Start after photo
    card_y = int(H * 0.06)
    
    draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill=WHITE)
    
    # 4. Setup fonts
    try:
        # Try to use nice serif fonts if available
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 42)
        headline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 72)
        bullet_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    except:
        title_font = ImageFont.load_default()
        headline_font = ImageFont.load_default()
        bullet_font = ImageFont.load_default()
    
    # 5. Text layout
    # Padding inside card
    pad_x = int(card_w * 0.08)
    text_w = card_w - (pad_x * 2)
    text_x = card_x + pad_x
    
    # Helper to wrap and center text
    def wrap_text(text, font, max_width):
        words = text.split()
        lines = []
        current = words[0] if words else ""
        for word in words[1:]:
            test = current + " " + word
            if draw.textlength(test, font=font) <= max_width:
                current = test
            else:
                lines.append(current)
                current = word
        lines.append(current)
        return lines
    
    def draw_centered_text(draw, lines, font, x, y, max_width, color, line_spacing=1.2):
        for line in lines:
            w = draw.textlength(line, font=font)
            draw.text((x + (max_width - w) / 2, y), line, font=font, fill=color)
            bbox = draw.textbbox((0, 0), line, font=font)
            y += (bbox[3] - bbox[1]) * line_spacing
        return y
    
    # Calculate content height for vertical centering
    title_lines = wrap_text(args.title.upper(), title_font, text_w)
    headline_lines = wrap_text(args.headline.upper(), headline_font, text_w)
    bullets = [b.strip() for b in args.bullets.split(",")]
    
    # Measure heights
    title_h = len(title_lines) * 50 * 1.3
    headline_h = len(headline_lines) * 80 * 1.1
    bullet_h = len(bullets) * 40 * 1.5
    gaps = 60 + 80  # Space between sections
    
    total_content_h = title_h + headline_h + bullet_h + gaps
    start_y = card_y + (card_h - total_content_h) / 2
    
    # Draw title
    y = draw_centered_text(draw, title_lines, title_font, text_x, start_y, text_w, TITLE_COLOR, 1.3)
    y += 60
    
    # Draw headline
    y = draw_centered_text(draw, headline_lines, headline_font, text_x, y, text_w, HEADLINE_COLOR, 1.1)
    y += 80
    
    # Draw bullets (centered)
    for bullet in bullets:
        text = f"• {bullet}"
        w = draw.textlength(text, font=bullet_font)
        draw.text((text_x + (text_w - w) / 2, y), text, font=bullet_font, fill=BULLET_COLOR)
        bbox = draw.textbbox((0, 0), text, font=bullet_font)
        y += bbox[3] - bbox[1] + 20
    
    # Save
    img.save(args.output, 'PNG')
    print(f"Pin saved: {args.output}")
    print(f"MEDIA: {os.path.abspath(args.output)}")
    
    # Cleanup
    if os.path.exists(temp_bg):
        os.remove(temp_bg)

if __name__ == "__main__":
    main()
