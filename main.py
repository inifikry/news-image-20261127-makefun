#!/usr/bin/env python3
"""Copy the pre-rendered front-page image to /output/entry.png.

No network, no drawing at run time: the image was rendered offline
with PIL (see draw_news.py) and ships in this repository as entry.png.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return dst


if __name__ == "__main__":
    written = main()
    print("wrote", written, os.path.getsize(written), "bytes")
    sys.exit(0)
