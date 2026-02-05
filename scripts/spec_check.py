from __future__ import annotations

from pathlib import Path
import sys


REQUIRED = [
    "specs/_meta.md",
    "specs/functional.md",
    "specs/technical.md",
    "research/specs/",
    "skills/README.md",
]


def main() -> int:
    missing = [path for path in REQUIRED if not Path(path).exists()]
    if missing:
        print("Missing required spec artifacts:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("Spec check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
