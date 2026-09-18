#!/usr/bin/env python3
"""Generate/check SWIR Progress SVG PRO assets for the T303UA EFI reference.

There is no authoritative product roadmap with a verified denominator, so product
progress is intentionally N/A. The published EFI release is tracked separately.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "readme"

CARD = (ASSETS / "progress-card.svg").read_text(encoding="utf-8") if (ASSETS / "progress-card.svg").exists() else ""
MINI = (ASSETS / "progress-mini.svg").read_text(encoding="utf-8") if (ASSETS / "progress-mini.svg").exists() else ""

REQUIRED_CARD = ("T303UA OPENCORE EFI REFERENCE", "N/A", "NO AUTHORITATIVE ROADMAP", "no verified denominator")
REQUIRED_MINI = ("PRODUCT ROADMAP", "N/A", "No verified denominator")


def validate(text: str, required: tuple[str, ...]) -> bool:
    return bool(text) and all(token in text for token in required) and "width=\"XXX\"" not in text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate committed generated SVGs")
    args = parser.parse_args()
    if not args.check:
        print("This repository has N/A product progress; committed SVGs are the canonical generated output. Use --check to validate them.")
        return 0
    stale = []
    if not validate(CARD, REQUIRED_CARD):
        stale.append("progress-card.svg")
    if not validate(MINI, REQUIRED_MINI):
        stale.append("progress-mini.svg")
    if stale:
        print("invalid or stale progress assets: " + ", ".join(stale))
        return 1
    print("progress assets are current: product roadmap = N/A")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
