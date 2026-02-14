"""Render a single preview label with the new layout."""
from PIL import Image, ImageDraw, ImageFont
import math, os

LW, LH = 472, 189

# Sample config
cfg = {'size': 'M3', 'length': 50, 'head': 'CAP', 'drive': 'HX', 'material': 'Black'}
SIZE_BARS = {'M2':1,'M2.5':2,'M3':3,'M4':4,'M5':5,'M6':6}
HEADS = {'CAP':'Cap Head','BTN':'Button Head','CSK':'Countersunk','RCSK':'Raised Countersunk'}
DRIVES_FULL = {'PH':'Phillips','HX':'Hex'}
DRIVES_ABBR = {'PH':'PH','HX':'HEX'}

img = Image.new('RGB', (LW, LH), 'white')
draw = ImageDraw.Draw(img)

# --- Top bars: full width, taller ---
bar_count = SIZE_BARS[cfg['size']]
bar_h = 14
gap = 4
total_bar_w = LW - 8  # 4px margin each side
bar_w = (total_bar_w - (bar_count - 1) * gap) // bar_count
for i in range(bar_count):
    x0 = 4 + i * (bar_w + gap)
    draw.rectangle([x0, 3, x0 + bar_w, 3 + bar_h], fill='black')

ctop = 3 + bar_h + 4  # start below bars

# --- Text zone: ~52% width ---
tz_pct = 0.52
tzW = int(LW * tz_pct)
tx = 8

# Fonts - bigger across the board
try:
    font_size_line = ImageFont.truetype('arialbd.ttf', 62)   # M3 x 50
    font_head_line = ImageFont.truetype('arialbd.ttf', 32)   # HEX CAP
    font_detail    = ImageFont.truetype('arial.ttf', 22)      # Socket: Hex - Head: Cap Head
    font_material  = ImageFont.truetype('arialbd.ttf', 22)    # Black
except:
    font_size_line = ImageFont.truetype('arial.ttf', 62)
    font_head_line = ImageFont.truetype('arial.ttf', 32)
    font_detail    = ImageFont.truetype('arial.ttf', 22)
    font_material  = ImageFont.truetype('arial.ttf', 22)

# Line 1: M3 x 50
size_text = f"{cfg['size']} x {cfg['length']}"
draw.text((tx, ctop - 8), size_text, fill='black', font=font_size_line)

# Line 2: HEX CAP
head_line = f"{DRIVES_ABBR[cfg['drive']]} {cfg['head']}"
draw.text((tx, ctop + 46), head_line, fill='black', font=font_head_line)

# Line 3: Socket: Hex
draw.text((tx, ctop + 78), f"Socket: {DRIVES_FULL[cfg['drive']]}", fill='black', font=font_detail)

# Line 4: Head: Cap Head
draw.text((tx, ctop + 100), f"Head: {HEADS[cfg['head']]}", fill='black', font=font_detail)

# Line 5: Material
draw.text((tx, ctop + 124), cfg['material'], fill='black', font=font_material)

# --- Divider ---
divX = tzW - 4
draw.line([(divX, ctop), (divX, LH - 6)], fill='black', width=1)

# --- Drawing zone (right side) ---
dzStart = tzW
dzW = LW - dzStart - 4
tdZW = int(dzW * 0.48)
sideZW = dzW - tdZW
contentH = LH - ctop - 4
tdCx = dzStart + tdZW // 2
tdCy = ctop + contentH // 2
tdR = min(tdZW * 0.42, contentH * 0.42)

filled = cfg['material'] == 'Black'

# Top-down view
if filled:
    draw.ellipse([tdCx - tdR, tdCy - tdR, tdCx + tdR, tdCy + tdR], fill='black')
    ir = tdR * 0.78
    draw.ellipse([tdCx - ir, tdCy - ir, tdCx + ir, tdCy + ir], outline='white', width=2)
    dr = tdR * 0.42
    hex_pts = []
    for i in range(6):
        a = math.radians(60 * i - 30)
        hex_pts.append((tdCx + dr * math.cos(a), tdCy + dr * math.sin(a)))
    draw.polygon(hex_pts, fill='white')
else:
    draw.ellipse([tdCx - tdR, tdCy - tdR, tdCx + tdR, tdCy + tdR], outline='black', width=3)
    ir = tdR * 0.78
    draw.ellipse([tdCx - ir, tdCy - ir, tdCx + ir, tdCy + ir], outline='black', width=2)
    dr = tdR * 0.42
    hex_pts = []
    for i in range(6):
        a = math.radians(60 * i - 30)
        hex_pts.append((tdCx + dr * math.cos(a), tdCy + dr * math.sin(a)))
    draw.polygon(hex_pts, fill='black')

# Side profile: CAP silhouette
sx0 = dzStart + tdZW
sw = sideZW - 4
sh = contentH - 4
scx = sx0 + sw // 2
sL = scx - sw * 0.15
sR = scx + sw * 0.15
sB = ctop + 2 + sh * 0.88
stip = ctop + 2 + sh * 0.96
hL = scx - sw * 0.30
hR = scx + sw * 0.30
hT = ctop + 2 + sh * 0.04
hB = ctop + 2 + sh * 0.37
ch_s = sw * 0.04

if filled:
    silhouette = [
        (hL + ch_s, hT), (hR - ch_s, hT), (hR, hT + ch_s),
        (hR, hB), (sR, hB), (sR, sB),
        (scx, stip), (sL, sB), (sL, hB),
        (hL, hB), (hL, hT + ch_s)
    ]
    draw.polygon(silhouette, fill='black')
    for y_val in range(int(hB + 8), int(sB - 2), 7):
        draw.line([(sL + 2, y_val), (sR - 2, y_val + 1)], fill='white', width=1)
else:
    draw.rectangle([hL, hT, hR, hB], outline='black', width=3)
    draw.line([(sL, hB), (sL, sB)], fill='black', width=3)
    draw.line([(sR, hB), (sR, sB)], fill='black', width=3)
    draw.line([(sL, sB), (scx, stip)], fill='black', width=3)
    draw.line([(sR, sB), (scx, stip)], fill='black', width=3)
    for y_val in range(int(hB + 8), int(sB - 2), 7):
        draw.line([(sL + 2, y_val), (sR - 2, y_val + 1)], fill='black', width=1)

# Border
draw.rectangle([1, 1, LW - 2, LH - 2], outline='black', width=2)

out = os.path.join(os.path.dirname(__file__), 'label_preview.png')
img_2x = img.resize((LW * 2, LH * 2), Image.NEAREST)
img_2x.save(out)
print(f"Saved to {out}")
