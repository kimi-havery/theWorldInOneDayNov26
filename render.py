#!/usr/bin/env python3
"""Render the 26 November 2026 world-news front page (1024x1024 PNG).

Build-time tool only: it draws entry.png from the verified facts in
sources.md. The submitted program is main.py, which copies entry.png.
Run:  python3 render.py   (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- palette: newsprint ----
PAPER = (247, 243, 233)
INK = (20, 20, 20)
RED = (179, 39, 30)
GREY = (110, 106, 96)
LIGHT = (226, 220, 205)
GREEN = (0, 110, 60)

FDIR = "/usr/share/fonts/truetype/noto"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FDIR, name), size)
    except OSError:
        return ImageFont.truetype(os.path.join(FDIR, "NotoSans-Regular.ttf"), size)


SERIF_BLACK = lambda s: font("NotoSerifDisplay-Black.ttf", s)
SERIF_BOLD = lambda s: font("NotoSerif-Bold.ttf", s)
SERIF = lambda s: font("NotoSerif-Regular.ttf", s)
SERIF_IT = lambda s: font("NotoSerif-Italic.ttf", s)
SANS = lambda s: font("NotoSans-Regular.ttf", s)
SANS_BOLD = lambda s: font("NotoSans-Bold.ttf", s)

W = H = 1024
M = 40  # margin
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if fnt.getlength(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, lines, fnt, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.28)
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def kicker(x, y, s, size=17):
    d.text((x, y), s, font=SANS_BOLD(size), fill=RED)
    return y + size + 10


def hrule(x0, x1, y, width=2, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


def vrule(x, y0, y1, width=1, fill=GREY):
    d.line([(x, y0), (x, y1)], fill=fill, width=width)


# ---- outer frame ----
d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)

# ---- masthead (34-174) ----
d.text((M, 34), "The World in One Day", font=SERIF_BLACK(66), fill=INK)
d.text((W - M, 42), "THURSDAY", font=SANS_BOLD(20), fill=INK, anchor="ra")
d.text((W - M, 68), "26 NOVEMBER 2026", font=SANS_BOLD(20), fill=RED, anchor="ra")
d.text((M, 118), "Drones over Kuwait, mines off Oman, a new ECB chief, Britain\u2019s migration",
       font=SERIF_IT(21), fill=INK)
d.text((M, 146), "low and Ebola\u2019s grim milestone \u2014 the day the world turned, in six stories.",
       font=SERIF_IT(21), fill=INK)
hrule(M, W - M, 178, 3)
hrule(M, W - M, 184, 1)

# ---- LEAD: KUWAIT (196-428) ----
kicker(M, 196, "T H E   G U L F   \u00b7   K U W A I T")
d.text((M, 226), "Drones kill two Italians", font=SERIF_BOLD(50), fill=INK)
d.text((M, 282), "in Kuwait attack", font=SERIF_BOLD(50), fill=INK)
deck = wrap("Kuwait says Iranian drones hit an air-defence station. "
            "The dead were Rheinmetall Italia technicians. "
            "Iran denies any role; two more were wounded.",
            SERIF(21), 600)
text_block(M, 348, deck, SERIF(21), leading=27)

# right column: big 2 + attack facts
rx = 690
d.text((rx, 200), "2", font=SERIF_BLACK(96), fill=RED)
d.text((rx + 78, 236), "ITALIANS", font=SANS_BOLD(20), fill=INK)
d.text((rx + 78, 262), "KILLED", font=SANS_BOLD(20), fill=INK)
d.text((rx + 4, 312), "2 MORE WOUNDED", font=SANS_BOLD(15), fill=INK)
d.text((rx + 4, 334), "2ND ATTACK ON KUWAIT", font=SANS_BOLD(15), fill=INK)
d.text((rx + 4, 356), "THIS MONTH", font=SANS_BOLD(15), fill=INK)
d.text((rx + 4, 384), "Iran: \u201cNo military or", font=SANS(14), fill=GREY)
d.text((rx + 4, 404), "offensive operations\u201d", font=SANS(14), fill=GREY)
hrule(M, W - M, 436, 2)

# ---- ROW 2: OIL | ECB (452-716) ----
col_w = 452
kicker(M, 452, "O I L   \u00b7   H O R M U Z")
kicker(540, 452, "E U R O P E   \u00b7   B R U S S E L S")
d.text((M, 482), "Tankers hit mines off", font=SERIF_BOLD(29), fill=INK)
d.text((M, 516), "Oman; Brent tops $96", font=SERIF_BOLD(29), fill=INK)
d.text((540, 482), "Spain\u2019s de Cos picked", font=SERIF_BOLD(29), fill=INK)
d.text((540, 516), "to lead the ECB", font=SERIF_BOLD(29), fill=INK)

# oil body + big price
obody = wrap("Iran\u2019s Guards say two tankers exploded and caught fire "
             "after hitting mines north of Khasab. One was a "
             "supertanker carrying 2m+ barrels of crude.",
             SERIF(19), col_w - 8)
text_block(M, 560, obody, SERIF(19), leading=25)
d.text((M, 660), "$96.57", font=SERIF_BLACK(52), fill=RED)
d.text((M + 205, 674), "BRENT, UP $1.96", font=SANS_BOLD(16), fill=INK)
d.text((M + 205, 696), "THURSDAY SETTLE", font=SANS_BOLD(16), fill=INK)

# ecb body + first-meeting chip
ebody = wrap("Eurozone leaders choose the former Bank of Spain chief "
             "\u2014 now running the BIS \u2014 to succeed Lagarde when "
             "she steps down on 7 February. First Spaniard in the job.",
             SERIF(19), col_w - 8)
text_block(540, 560, ebody, SERIF(19), leading=25)
d.rectangle([540, 664, 540 + 268, 664 + 40], outline=INK, width=2)
d.text((540 + 134, 672), "BOARD: BOONE \u00b7 BRUNNERMEIER",
       font=SANS_BOLD(13), fill=INK, anchor="ma")

vrule(512, 452, 706, 1)
hrule(M, W - M, 720, 2)

# ---- ROW 3: UK MIGRATION | EBOLA (736-906) ----
kicker(M, 730, "B R I T A I N   \u00b7   L O N D O N")
kicker(540, 730, "H E A L T H   \u00b7   K I N S H A S A")
d.text((M, 758), "UK net migration falls", font=SERIF_BOLD(27), fill=INK)
d.text((M, 790), "to a 29-year low", font=SERIF_BOLD(27), fill=INK)
d.text((540, 758), "Congo Ebola cases pass", font=SERIF_BOLD(27), fill=INK)
d.text((540, 790), "12,000", font=SERIF_BOLD(27), fill=INK)

# migration body (full column) + peak stat line
mbody = wrap("ONS: 77,000 in the year to June, down from 204,000. "
             "738,000 arrived, 661,000 left \u2014 about 90% below "
             "the 2023 peak.", SERIF(18), col_w - 8)
text_block(M, 828, mbody, SERIF(18), leading=23)
d.text((M, 898), "2023 PEAK 944K  \u00b7  2025 204K  \u00b7  2026 77K",
       font=SANS_BOLD(13), fill=RED)

# ebola body (full column) + deadliest-outbreak stat line
ebody2 = wrap("12,021 confirmed, 5,904 dead \u2014 the second-largest "
              "outbreak on record. No approved vaccine for the "
              "Bundibugyo strain.", SERIF(18), col_w - 8)
text_block(540, 828, ebody2, SERIF(18), leading=23)
d.text((540, 898), "DRC\u2019S 17TH OUTBREAK \u2014 ITS DEADLIEST",
       font=SANS_BOLD(13), fill=RED)

vrule(512, 730, 906, 1)

# ---- FOOTER (922-996) ----
hrule(M, W - M, 922, 3)
d.text((M, 934), "ALSO \u2014", font=SANS_BOLD(15), fill=RED)
ticker = ("No Macy\u2019s parade today: the 100th edition moves to Saturday \u2014 "
          "the first weather postponement in its history. Earth logs six "
          "straight days above 2\u00b0C, a first on record, peaking at 2.24\u00b0C.")
tlines = wrap(ticker, SANS(15), W - 2 * M - 70)
text_block(M + 70, 934, tlines, SANS(15), leading=19)
d.text((M, 978), "Sources: Reuters \u00b7 ONS \u00b7 AP \u00b7 UN News \u00b7 Copernicus",
       font=SANS(12), fill=GREY)
d.text((W - M, 978), "All events of Thursday 26 November 2026",
       font=SANS(12), fill=GREY, anchor="ra")

out = os.path.join(HERE, "entry.png")
img.save(out, optimize=True)
print("saved", out, img.size, os.path.getsize(out), "bytes")
