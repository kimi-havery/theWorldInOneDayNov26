#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261126 bounty.

The submitted image lives in the repository as entry.png. This program
simply places a byte-identical copy of it where the grader expects it,
so the two runs the grader performs produce exactly the same bytes.

Standard library only; no network access.
"""

import os
import shutil
from pathlib import Path


def entry_source() -> Path:
    """The image shipped in this repository, next to this script."""
    return Path(__file__).resolve().parent / "entry.png"


def output_path() -> Path:
    """Where the grader wants the image.

    MAKEFUN_OUTPUT_DIR names the directory when set; otherwise the
    default output directory is used.
    """
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(directory) / "entry.png"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(entry_source(), target)


if __name__ == "__main__":
    main()
