"""make.fun entry program for the news-image-20261125 bounty.

Takes the image file stored next to this script and places a copy of it
in the output directory as entry.png. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable and defaults to /output when the
variable is not set. Only the standard library is used, and nothing here
touches the network.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

MAX_IMAGE_BYTES = 1024 * 1024

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def die(message):
    """Print an error to stderr and exit non-zero."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    script_dir = Path(__file__).resolve().parent
    source = script_dir / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target = output_dir / "entry.png"

    if not source.is_file():
        die(f"entry image not found: {source}")

    image = source.read_bytes()

    if len(image) > MAX_IMAGE_BYTES:
        die(f"entry image is {len(image)} bytes, over the 1 MiB limit")

    if not (image.startswith(PNG_MAGIC) or image.startswith(JPEG_MAGIC)):
        die("entry image is not a PNG or JPEG (bad magic bytes)")

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)

    # The entry must be reproducible: the grader runs this program twice
    # and compares the bytes, so confirm the copy matches the source.
    source_hash = hashlib.sha256(image).hexdigest()
    copy_hash = hashlib.sha256(target.read_bytes()).hexdigest()
    if copy_hash != source_hash:
        die("copied entry image does not match the source image")


if __name__ == "__main__":
    main()
