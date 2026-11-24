#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news infographic, 1024x1024 PNG.
All text is set from verified 23 Nov 2026 reporting; icons are simple
vector shapes drawn with PIL. No photos, no downloaded artwork."""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

NAVY = (16, 34, 64)
NAVY2 = (24, 48, 88)
GOLD = (212, 175, 55)
BG = (245, 243, 238)
CARD = (255, 255, 255)
INK = (24, 24, 28)
GREY = (96, 96, 104)

F_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(F_DIR, name), size)

F_TAG = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 29)
F_BODY = font("DejaVuSans.ttf", 20)
F_DATE = font("DejaVuSans-Bold.ttf", 66)
F_SUB = font("DejaVuSans.ttf", 22)
F_KICK = font("DejaVuSans-Bold.ttf", 24)
F_FOOT_H = font("DejaVuSans-Bold.ttf", 20)
F_FOOT = font("DejaVuSans.ttf", 19)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def wrap(text, fnt, width):
    """Greedy wrap by measured pixel width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def rr(x0, y0, x1, y1, r, fill):
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=fill)

# ---------- header ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((28, 22), "MONDAY  \u2022  WORLD NEWS", font=F_KICK, fill=(150, 180, 220))
d.text((28, 48), "23 NOVEMBER 2026", font=F_DATE, fill=(255, 255, 255))
d.text((30, 118), "The day in six stories", font=F_SUB, fill=(170, 195, 225))
# globe icon, top right
cx, cy, r = 936, 72, 46
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=4)
d.ellipse([cx - 22, cy - r, cx + 22, cy + r], outline=(255, 255, 255), width=3)
d.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=3)
d.arc([cx - r + 8, cy - 26, cx + r - 8, cy + 26], 200, 340, fill=(255, 255, 255), width=3)
d.arc([cx - r + 8, cy - 26, cx + r - 8, cy + 26], 20, 160, fill=(255, 255, 255), width=3)
d.rectangle([0, 148, W, 154], fill=GOLD)

# ---------- icons ----------
def icon_chip(x, y, c):
    d.rectangle([x, y, x + 44, y + 44], outline=c, width=5)
    d.rectangle([x + 14, y + 14, x + 30, y + 30], fill=c)
    for i in range(3):
        d.line([x + 10 + i * 12, y - 8, x + 10 + i * 12, y], fill=c, width=4)
        d.line([x + 10 + i * 12, y + 44, x + 10 + i * 12, y + 52], fill=c, width=4)
        d.line([x - 8, y + 10 + i * 12, x, y + 10 + i * 12], fill=c, width=4)
        d.line([x + 44, y + 10 + i * 12, x + 52, y + 10 + i * 12], fill=c, width=4)

def icon_ship(x, y, c):
    d.polygon([(x, y + 26), (x + 52, y + 26), (x + 44, y + 44), (x + 8, y + 44)], fill=c)
    d.line([x + 26, y, x + 26, y + 26], fill=c, width=4)
    d.polygon([(x + 26, y + 4), (x + 44, y + 16), (x + 26, y + 16)], fill=c)
    # explosion star above
    ex, ey = x + 44, y - 2
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line([ex, ey, ex + 13 * math.cos(a), ey + 13 * math.sin(a)], fill=(200, 40, 30), width=3)

def icon_scales(x, y, c):
    d.line([x + 26, y, x + 26, y + 40], fill=c, width=4)
    d.line([x + 4, y + 8, x + 48, y + 8], fill=c, width=4)
    d.arc([x, y + 14, x + 20, y + 34], 0, 180, fill=c, width=3)
    d.arc([x + 32, y + 14, x + 52, y + 34], 0, 180, fill=c, width=3)
    d.line([x + 6, y + 44, x + 46, y + 44], fill=c, width=4)

def icon_flame(x, y, c):
    d.polygon([(x + 26, y), (x + 44, y + 22), (x + 34, y + 20), (x + 40, y + 36),
               (x + 26, y + 48), (x + 12, y + 36), (x + 18, y + 20), (x + 8, y + 22)], fill=c)

def icon_plane(x, y, c):
    d.polygon([(x, y + 22), (x + 20, y + 14), (x + 52, y + 8), (x + 52, y + 16),
               (x + 28, y + 26), (x + 44, y + 34), (x + 44, y + 40), (x + 26, y + 34),
               (x + 12, y + 44), (x + 8, y + 38), (x + 16, y + 28)], fill=c)

def icon_crystal(x, y, c):
    d.polygon([(x + 26, y), (x + 46, y + 14), (x + 40, y + 46), (x + 12, y + 46),
               (x + 6, y + 14)], fill=c)
    d.line([x + 26, y, x + 26, y + 46], fill=(255, 255, 255), width=3)
    d.line([x + 6, y + 14, x + 46, y + 14], fill=(255, 255, 255), width=3)

ICONS = [icon_chip, icon_ship, icon_scales, icon_flame, icon_plane, icon_crystal]

PANELS = [
    ("MARKETS  \u2022  US", (18, 110, 140), "Huang returns to Nvidia",
     "Nvidia reinstates Jensen Huang as CEO, 11 days after he resigned. Shares jump 31%."),
    ("UKRAINE  \u2022  WAR", (178, 44, 44), "Ukraine sinks Russian warship off Libya",
     "Seven sea drones sink the corvette Merkury in Benghazi; the cargo ship Angara is hit too."),
    ("LAW  \u2022  US", (120, 60, 150), "Two states sue SpaceX over Grok deepfakes",
     "Virginia and Oregon, the first states to sue, say Grok made sexual images of children and failed to stop them."),
    ("MIDDLE EAST  \u2022  IRAN", (150, 105, 25), "Iran vows to defy US blockade",
     "Tehran says it will use all means against the US naval blockade, as three tankers hit mines in Hormuz."),
    ("EUROPE  \u2022  SPAIN", (150, 40, 130), "Puigdemont free to come home",
     "Spain's top court drops the case against the Catalan ex-leader, clearing his return after nearly a decade in exile."),
    ("AFRICA  \u2022  ECONOMY", (30, 130, 90), "Congo halts cobalt exports",
     "DR Congo suspends cobalt exports from 30 November to tackle oversupply and weak prices, the minerals regulator says."),
]

# ---------- grid ----------
GX, GY = 24, 170
CW, CH, GAP = 480, 238, 16
for i, (tag, color, head, body) in enumerate(PANELS):
    col, row = i % 2, i // 2
    x0 = GX + col * (CW + GAP)
    y0 = GY + row * (CH + GAP)
    x1, y1 = x0 + CW, y0 + CH
    rr(x0, y0, x1, y1, 14, CARD)
    d.rectangle([x0, y0 + 14, x0 + 8, y1 - 14], fill=color)
    d.text((x0 + 24, y0 + 16), tag, font=F_TAG, fill=color)
    ICONS[i](x1 - 78, y0 + 14, color)
    # headline, max 2 lines (kept clear of the icon at top right)
    hl = wrap(head, F_HEAD, CW - 100)
    hy = y0 + 46
    for ln in hl[:2]:
        d.text((x0 + 24, hy), ln, font=F_HEAD, fill=INK)
        hy += 34
    # body, max 3 lines
    bl = wrap(body, F_BODY, CW - 48)
    by = hy + 8
    for ln in bl[:3]:
        d.text((x0 + 24, by), ln, font=F_BODY, fill=(52, 52, 58))
        by += 26

# ---------- footer ----------
FY = GY + 3 * CH + 2 * GAP + 14
rr(24, FY, W - 24, FY + 76, 12, NAVY)
d.text((44, FY + 8), "ALSO TODAY", font=F_FOOT_H, fill=(150, 180, 220))
foot = ("US seeks to recover $1bn in crypto stolen in the Binance hack  \u2022  "
        "Bomb threats hit about 450 German schools  \u2022  "
        "US blacklists AI firm Megaspeed after the Nvidia scandal")
fl = wrap(foot, F_FOOT, W - 88)
fy = FY + 32
for ln in fl[:2]:
    d.text((44, fy), ln, font=F_FOOT, fill=(255, 255, 255))
    fy += 22

img.save(OUT, "PNG")
print("saved", OUT, img.size, os.path.getsize(OUT), "bytes")
