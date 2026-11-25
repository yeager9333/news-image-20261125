"""Entry program for the make.fun news-image-20261125 bounty.

Copies the entry image beside this file to the output directory
($MAKEFUN_OUTPUT_DIR, or /output in the grader) as entry.png.
Standard library only; no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
