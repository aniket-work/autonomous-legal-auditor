import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import time

def create_terminal_frame(text_lines, cursor_visible=True, width=800, height=600):
    # Create dark terminal background
    img = Image.new('RGB', (width, height), color='#1e1e1e')
    d = ImageDraw.Draw(img)
    
    # Load font (try to use a monospace font if available, fallback to default)
    try:
        # MacOS specific path, might need adjustment for other OS or ship a font
        font = ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", 18)
    except:
        font = ImageFont.load_default()

    margin_x = 20
    margin_y = 20
    line_height = 25

    for i, line in enumerate(text_lines):
        # Color logic for rich simulation
        fill = '#cccccc' # default grey
        
        if "PASS" in line: fill = '#4caf50'
        elif "FAIL" in line: fill = '#f44336'
        elif "Loading" in line: fill = '#ffffff'
        elif "Auditor" in line: fill = '#00bcd4'
        elif "$" in line: fill = '#ffff00' # Prompt
        
        d.text((margin_x, margin_y + i * line_height), line, font=font, fill=fill)

    # Draw cursor if it's the last line
    if cursor_visible:
        cursor_y = margin_y + (len(text_lines) - 1) * line_height
        # Approximate width of text to place cursor at end
        last_line = text_lines[-1] if text_lines else ""
        text_width = d.textlength(last_line, font=font)
        d.rectangle([margin_x + text_width + 2, cursor_y + 2, margin_x + text_width + 10, cursor_y + 22], fill='#cccccc')

    return np.array(img)

def generate_gif():
    frames = []
    
    # 1. Terminal Simulation Sequence
    command = "$ python main.py"
    output_sequence = [
        "",
        "Autonomous Legal Contract Auditor",
        "Compliance & Risk Intelligence Engine",
        "",
        "Loading Contract: vendor_service_agreement_v1.pdf",
        "Parsing natural language... [Done]",
        "Cross-referencing corporate policies... [Done]",
        "Generating risk assessment... [Done]",
        "",
        "Audit Results:",
        "--------------------------------------------------",
        "Rule ID   | Severity | Status | Details",
        "--------------------------------------------------",
        "PAY-001   | HIGH     | PASS   | Compliant.",
        "LIAB-001  | CRITICAL | FAIL   | Violation detected...",
        "TERM-001  | MEDIUM   | PASS   | Compliant.",
        "GOV-001   | HIGH     | PASS   | Compliant.",
        "--------------------------------------------------",
        "",
        "Compliance Score: 85/100",
        ""
    ]
    
    current_lines = ["$ "]
    
    # Typing the command
    for char in "python main.py":
        current_lines[-1] += char
        frames.append(create_terminal_frame(current_lines)) # Typing
    
    frames.append(create_terminal_frame(current_lines, cursor_visible=True)) # Pause after typing
    current_lines.append("") # Newline
    
    # Output scrolling
    for line in output_sequence:
        current_lines.append(line)
        # Keep only last 20 lines to fit screen
        if len(current_lines) > 22:
            current_lines.pop(0)
        frames.append(create_terminal_frame(current_lines, cursor_visible=False))
        # Add a few extra frames for "processing" pause on specific lines
        if "Loading" in line or "..." in line:
             for _ in range(3): frames.append(create_terminal_frame(current_lines, cursor_visible=False))

    # Freeze terminal end state
    final_terminal = create_terminal_frame(current_lines, cursor_visible=True)
    for _ in range(15):
        frames.append(final_terminal)

    # 2. Add Statistical Chart (Cross-fade or Cut)
    # Load the generated stats chart
    if os.path.exists("images/stats_chart.png"):
        stats_img = Image.open("images/stats_chart.png").convert('RGB').resize((800, 600))
        stats_frame = np.array(stats_img)
        
        # Show stats for a few seconds
        for _ in range(30):
            frames.append(stats_frame)

    # Save GIF
    print("Saving GIF...")
    imageio.mimsave('images/title-animation.gif', frames, fps=10, loop=0)
    print("Done: images/title-animation.gif")

if __name__ == "__main__":
    generate_gif()
