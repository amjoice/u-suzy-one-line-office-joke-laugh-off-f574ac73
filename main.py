"""One-line office joke entry writer."""

from pathlib import Path

_PARTS = (
    "I invited my burnout to a recurring meeting and it declined",
    "\u2014",
    "already fully booked.",
)


def _compose() -> str:
    return " ".join(_PARTS)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_compose(), encoding="utf-8")

if __name__ == "__main__":
    main()
