[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/kimi-havery/theWorldInOneDayNov26/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/kimi-havery/theWorldInOneDayNov26/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World in One Day — 26 November 2026

Entry for the make.fun bounty **"Sum up 26 November's world news in
one image"** ($100, 50 places paid; ends 28 Nov 2026, 00:00 UTC).

A newspaper front page that sums up Thursday 26 November 2026 in six
stories, all verified against mainstream sources (see `sources.md`).
US markets were closed for Thanksgiving, so no US closing prices
appear:

1. **The Gulf** — Kuwait says Iranian drones killed two Italian
   technicians at an air-defence station; Iran denies any role.
2. **Oil** — Iran's Guards say two tankers hit mines off Oman; Brent
   settles at $96.57, up $1.96.
3. **Europe** — Eurozone leaders pick Spain's Pablo Hernández de Cos
   to succeed Lagarde as ECB president in February.
4. **Britain** — ONS: net migration 77,000 in the year to June, the
   lowest since 1997 outside the pandemic.
5. **Health** — DR Congo's Ebola cases pass 12,000 (12,021 confirmed,
   5,904 dead), the second-largest outbreak on record.
6. **Also** — No Macy's parade on Thanksgiving: the 100th edition
   moves to Saturday, a first; Earth logs six straight days above
   2°C, a first on record.

## Files

- `main.py` — the entry program (Python 3.13, standard library only):
  copies `entry.png` to `/output/entry.png`. Deterministic, no network.
- `entry.png` — the front page itself, 1024×1024, ~200 KB.
- `render.py` — the build-time script that drew `entry.png` with PIL
  from the facts in `sources.md` (not run by the grader).
- `sources.md` — every fact, figure and quotation, with outlet, date
  and URL.
- `LICENSE` — MIT.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs produce byte-identical output.
