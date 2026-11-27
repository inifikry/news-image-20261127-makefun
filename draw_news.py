#!/usr/bin/env python3
"""Draw the front-page image for Friday 27 November 2026.

Renders entry.png (1024x1024, PIL only, no network, no copied art).
Run: python3 draw_news.py  -> writes entry.png next to this script.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
RED = (180, 35, 24)
GOLD = (201, 162, 39)
GREY = (90, 86, 78)
CARD = (255, 255, 255)
TEAL = (14, 116, 109)
BLUE = (30, 90, 168)
GREEN = (46, 125, 50)
PURPLE = (106, 62, 158)
ORANGE = (196, 94, 10)

FDIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FDIR + "DejaVuSerif-Bold.ttf"
SERIF = FDIR + "DejaVuSerif.ttf"
SANS_B = FDIR + "DejaVuSans-Bold.ttf"
SANS = FDIR + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color):
    f = font(SANS_B, 16)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return y + 22


def card(draw, x0, y0, x1, y1, accent):
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=CARD,
                           outline=(210, 203, 188), width=2)
    draw.rectangle([x0 + 10, y0, x1 - 10, y0 + 5], fill=accent)


def story_panel(draw, x0, y0, x1, y1, kicker_text, accent, headline,
                body, icon):
    card(draw, x0, y0, x1, y1, accent)
    ix = x0 + 18
    iy = y0 + 46
    icon(draw, ix, iy)
    tx = x0 + 104
    tw = x1 - tx - 18
    y = kicker(draw, tx, y0 + 14, kicker_text, accent)
    hl = wrap(draw, headline, font(SERIF_B, 26), tw)
    y = draw_text_block(draw, tx, y + 2, hl[:2], font(SERIF_B, 26),
                        INK, 31)
    bl = wrap(draw, body, font(SANS, 19), tw)
    draw_text_block(draw, tx, y + 6, bl[:3], font(SANS, 19), (60, 58, 52), 24)


# ---- small icons, drawn with PIL primitives only ---------------------

def icon_drone(d, x, y):
    d.ellipse([x + 8, y + 26, x + 56, y + 42], fill=NAVY)
    d.ellipse([x + 24, y + 30, x + 40, y + 38], fill=RED)
    for cx in (x + 4, x + 60):
        d.line([cx, y + 32, x + 14, y + 34], fill=NAVY, width=3)
        d.line([cx, y + 32, x + 50, y + 34], fill=NAVY, width=3)
        d.ellipse([cx - 10, y + 18, cx + 10, y + 26], outline=NAVY, width=3)
    d.line([x + 32, y + 42, x + 32, y + 52], fill=NAVY, width=3)
    d.ellipse([x + 27, y + 50, x + 37, y + 60], fill=GOLD)


def icon_storm(d, x, y):
    d.ellipse([x + 6, y + 14, x + 34, y + 38], fill=BLUE)
    d.ellipse([x + 22, y + 6, x + 52, y + 34], fill=BLUE)
    d.ellipse([x + 38, y + 16, x + 62, y + 40], fill=BLUE)
    d.rectangle([x + 8, y + 30, x + 60, y + 42], fill=BLUE)
    d.polygon([(x + 34, y + 40), (x + 22, y + 62), (x + 32, y + 62),
               (x + 26, y + 76), (x + 44, y + 50), (x + 34, y + 50)],
              fill=GOLD)


def icon_ballot(d, x, y):
    d.rounded_rectangle([x + 8, y + 26, x + 56, y + 62], radius=4,
                        fill=(255, 255, 255), outline=TEAL, width=4)
    d.line([x + 22, y + 18, x + 42, y + 18], fill=TEAL, width=5)
    d.polygon([(x + 18, y + 44), (x + 28, y + 54), (x + 48, y + 30)],
              fill=TEAL)
    d.line([x + 18, y + 44, x + 28, y + 54], fill=TEAL, width=4)
    d.line([x + 28, y + 54, x + 48, y + 30], fill=TEAL, width=4)


def icon_chess(d, x, y):
    s = 15
    for r in range(4):
        for c in range(4):
            fill = INK if (r + c) % 2 == 0 else (255, 255, 255)
            d.rectangle([x + c * s, y + r * s, x + (c + 1) * s,
                         y + (r + 1) * s], fill=fill,
                        outline=(150, 145, 135), width=1)
    d.rectangle([x, y, x + 4 * s, y + 4 * s], outline=INK, width=3)
    d.text((x + 17, y + 66), "G - S", font=font(SANS_B, 15), fill=INK)


def icon_bank(d, x, y):
    d.polygon([(x + 4, y + 24), (x + 32, y + 6), (x + 60, y + 24)],
              fill=GREEN)
    d.rectangle([x + 8, y + 28, x + 56, y + 32], fill=GREEN)
    for cx in (x + 14, x + 28, x + 42):
        d.rectangle([cx, y + 36, cx + 6, y + 58], fill=GREEN)
    d.rectangle([x + 6, y + 58, x + 58, y + 64], fill=GREEN)


def icon_chart(d, x, y):
    d.line([x + 8, y + 8, x + 8, y + 60], fill=PURPLE, width=4)
    d.line([x + 8, y + 60, x + 60, y + 60], fill=PURPLE, width=4)
    d.line([x + 12, y + 18, x + 26, y + 26, x + 38, y + 38, x + 54, y + 52],
           fill=RED, width=5)
    d.polygon([(x + 54, y + 52), (x + 62, y + 52), (x + 54, y + 44)],
              fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ---------------------------------------------------
    d.rectangle([0, 0, W, 112], fill=NAVY)
    d.rectangle([0, 112, W, 116], fill=GOLD)
    d.text((24, 14), "THE WORLD IN ONE DAY",
           font=font(SANS_B, 20), fill=GOLD)
    d.text((24, 40), "FRIDAY 27 NOVEMBER 2026",
           font=font(SERIF_B, 52), fill=(255, 255, 255))
    d.text((W - 24, 18), "SIX STORIES", font=font(SANS_B, 18),
           fill=(255, 255, 255), anchor="ra")
    d.text((W - 24, 44), "ONE DAY", font=font(SANS_B, 18),
           fill=GOLD, anchor="ra")

    # ---- lead story: Kuwait ----------------------------------------
    lx0, ly0, lx1, ly1 = 24, 128, 1000, 416
    card(d, lx0, ly0, lx1, ly1, RED)
    y = kicker(d, 48, ly0 + 16, "Middle East  |  Lead story", RED)
    hl = wrap(d, "Drone strike in Kuwait kills two Italians",
              font(SERIF_B, 40), 600)
    y = draw_text_block(d, 48, y + 2, hl, font(SERIF_B, 40), INK, 47)
    body = ("Italy and Kuwait blame Iran for the attack on an "
            "air-defence station; Tehran denies any role. "
            "The two dead were technicians for Rheinmetall, "
            "working on Kuwaiti military systems.")
    bl = wrap(d, body, font(SANS, 21), 600)
    draw_text_block(d, 48, y + 10, bl, font(SANS, 21), (60, 58, 52), 27)

    # lead illustration: night sky, drone, burst
    ix0, iy0, ix1, iy1 = 676, 146, 976, 398
    d.rounded_rectangle([ix0, iy0, ix1, iy1], radius=10, fill=(16, 24, 48))
    for sx, sy, r in [(700, 170, 2), (740, 200, 2), (820, 165, 3),
                      (900, 190, 2), (950, 230, 2), (710, 260, 2),
                      (860, 290, 2), (940, 320, 3), (780, 330, 2)]:
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 255, 255))
    for r in (40, 70, 100):
        d.arc([ix0 + 150 - r, iy0 + 130 - r, ix0 + 150 + r, iy0 + 130 + r],
              start=200, end=340, fill=(120, 160, 220), width=2)
    # drone
    d.ellipse([ix0 + 96, iy0 + 108, ix0 + 150, iy0 + 124], fill=(200, 205, 215))
    d.ellipse([ix0 + 116, iy0 + 112, ix0 + 130, iy0 + 120], fill=RED)
    for cx in (ix0 + 92, ix0 + 154):
        d.line([cx, iy0 + 116, ix0 + 104, iy0 + 117], fill=(200, 205, 215),
               width=3)
        d.line([cx, iy0 + 116, ix0 + 142, iy0 + 117], fill=(200, 205, 215),
               width=3)
        d.ellipse([cx - 11, iy0 + 102, cx + 11, iy0 + 110],
                  outline=(200, 205, 215), width=3)
    # burst
    bx, by = ix0 + 236, iy0 + 190
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = 34 if i % 2 == 0 else 14
        pts.append((bx + rr * math.cos(ang), by + rr * math.sin(ang)))
    d.polygon(pts, fill=(255, 176, 32))
    d.ellipse([bx - 12, by - 12, bx + 12, by + 12], fill=(255, 220, 120))
    d.text((ix0 + 14, iy1 - 34), "KUWAIT CITY",
           font=font(SANS_B, 16), fill=(180, 200, 235))

    # ---- grid rows --------------------------------------------------
    story_panel(d, 24, 428, 500, 592, "United States", BLUE,
                "Storm stops the Macy's parade",
                "First weather postponement in 100 years; "
                "850,000+ homes lost power.",
                icon_storm)
    story_panel(d, 524, 428, 1000, 592, "New Zealand", TEAL,
                "Final vote keeps coalition in power",
                "Slim majority confirmed: 67 of 131 seats "
                "after the final count.",
                icon_ballot)
    story_panel(d, 24, 604, 500, 768, "Sport  |  Chess", PURPLE,
                "Chess title deadlocked",
                "Gukesh and Sindarov draw marathon Game 3; "
                "all square after three.",
                icon_chess)
    story_panel(d, 524, 604, 1000, 768, "Argentina", GREEN,
                "Milei wins in Congress",
                "Senate suspends 2027 primaries; central bank "
                "barred from funding the state.",
                icon_bank)

    # ---- full-width row: UK ----------------------------------------
    x0, y0, x1, y1 = 24, 780, 1000, 900
    card(d, x0, y0, x1, y1, ORANGE)
    icon_chart(d, x0 + 18, y0 + 26)
    tx = x0 + 104
    y = kicker(d, tx, y0 + 12, "United Kingdom", ORANGE)
    hl = wrap(d, "UK net migration falls to 77,000",
              font(SERIF_B, 26), x1 - tx - 18)
    y = draw_text_block(d, tx, y + 2, hl[:1], font(SERIF_B, 26), INK, 31)
    bl = wrap(d, "Lowest since 1997 outside the pandemic, the ONS says "
                 "— down from 204,000 a year earlier.",
              font(SANS, 19), x1 - tx - 18)
    draw_text_block(d, tx, y + 4, bl[:2], font(SANS, 19), (60, 58, 52), 24)

    # ---- footer -----------------------------------------------------
    d.line([24, 920, 1000, 920], fill=(190, 183, 168), width=2)
    d.text((512, 934), "Six stories from Friday 27 November 2026",
           font=font(SERIF_B, 20), fill=INK, anchor="ma")
    d.text((512, 964),
           "Sources: Reuters  •  The New York Times  •  BBC  •  ONS  •  "
           "Newstalk ZB  •  India Today",
           font=font(SANS, 16), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
