"""Entry program for the make.fun news-image-20261125 bounty.

Copies the entry image beside this file to the output directory
($MAKEFUN_OUTPUT_DIR, or /output in the grader) as entry.png.
Standard library only; no network.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
DST = OUT / "entry.png"

# The gate wants a real PNG or JPEG under 1 MiB: refuse anything else
# rather than silently copying a corrupt file.
data = SRC.read_bytes()
if len(data) > 1024 * 1024:
    raise ValueError("entry image exceeds the 1 MiB cap")
if not (data[:8] == b"\x89PNG\r\n\x1a\n" or data[:3] == b"\xff\xd8\xff"):
    raise ValueError("entry image is not a PNG or JPEG")

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)

# The grader runs the program twice and expects identical bytes.
if hashlib.sha256(DST.read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
    raise ValueError("copied entry image differs from the source")
