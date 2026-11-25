import os
from pathlib import Path

FORTUNE = "Work hard today; every problem you solve trains the smaller model that replaces you."


def main() -> None:
    fortune = FORTUNE.strip()
    if not (1 <= len(fortune) <= 200) or "\n" in fortune or "\r" in fortune:
        raise ValueError(f"Invalid fortune length or format: {len(fortune)}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(fortune, encoding="utf-8")


if __name__ == "__main__":
    main()
