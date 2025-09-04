import argparse
import sys
from pathlib import Path

from .core import analyze_text, top_n_words


def _read_input(text: str | None, file: str | None) -> str:
    if text and file:
        raise ValueError("Provide either --text or --file, not both.")
    if text:
        return text
    if file:
        path = Path(file)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file}")
        return path.read_text(encoding="utf-8")
    return sys.stdin.read()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="textstat-mini",
        description="Compute simple text statistics and top words.",
    )
    parser.add_argument("--text", help="Inline text to analyze", default=None)
    parser.add_argument("--file", help="Path to a text file", default=None)
    parser.add_argument("--top", type=int, default=5, help="Number of top words to display")

    args = parser.parse_args(argv)
    try:
        content = _read_input(args.text, args.file)
        stats = analyze_text(content)
        top = top_n_words(content, args.top)

        print("# Text Stats")
        for k, v in stats.items():
            print(f"{k}: {v}")

        print("\n# Top Words")
        for w, c in top:
            print(f"{w}: {c}")

        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
