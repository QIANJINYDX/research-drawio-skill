#!/usr/bin/env python3
"""Convert an SVG file into a draw.io-compatible data URI."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
import urllib.parse
from pathlib import Path


def validate_svg(svg_text: str, path: Path) -> None:
    try:
        root = ET.fromstring(svg_text)
    except ET.ParseError as exc:
        raise SystemExit(f"ERROR: invalid SVG XML in {path}: {exc}") from exc
    tag = root.tag.lower()
    if not (tag.endswith("svg") or tag == "svg"):
        raise SystemExit(f"ERROR: root element is not <svg>: {root.tag}")


def drawio_svg_data_uri(svg_text: str) -> str:
    """Return a data URI that is safe inside a draw.io style string.

    mxGraph styles use semicolons as field separators, so a raw
    ``data:image/svg+xml;base64,...`` URI is split at ``svg+xml;base64`` and
    does not render. URL-encoding keeps the image value as one style field.
    """

    return "data:image/svg+xml," + urllib.parse.quote(svg_text, safe="")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path, help="Path to an SVG file")
    parser.add_argument(
        "--style",
        action="store_true",
        help="Print a draw.io image style fragment instead of only the data URI",
    )
    args = parser.parse_args()

    svg_path = args.svg
    svg_text = svg_path.read_text(encoding="utf-8").lstrip("\ufeff")
    validate_svg(svg_text, svg_path)
    data_uri = drawio_svg_data_uri(svg_text)

    if args.style:
        print(f"shape=image;html=1;image={data_uri};aspect=fixed;imageAspect=1;")
    else:
        print(data_uri)
    return 0


if __name__ == "__main__":
    sys.exit(main())
