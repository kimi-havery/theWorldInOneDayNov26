#!/usr/bin/env python3
"""Entry program for make.fun "Sum up 26 November's world news in one image".

Standard library only. Copies the pre-rendered front page (entry.png,
drawn at build time by render.py from the verified facts in sources.md)
to /output/entry.png. Byte-for-byte deterministic; no network access.

Run outside the grader with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
