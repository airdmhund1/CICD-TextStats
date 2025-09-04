"""
CLI entry point for the cicd-textstats package.

This module provides a command-line interface (CLI) for analyzing text.
Users can supply inline text, a file path, or pipe input via STDIN.
The CLI computes basic statistics (characters, words, lines) and
displays the top-N most frequent words.
"""

import argparse
import sys
from pathlib import Path

from .core import analyze_text, top_n_words


def _read_input(text: str | None, file: str | None) -> str:
    """
    Retrieve the input text from one of the supported sources.

    Exactly one of 'text' or 'file`' should be provided. If neither is
    specified, the function falls back to reading from STDIN.

    Parameters
    ----------
    text : str | None
        Inline text content passed via CLI argument.
    file : str | None
        Path to a text file containing the input.

    Returns
    -------
    str
        The full text content to analyze.

    Raises
    ------
    ValueError
        If both 'text' and 'file' are provided simultaneously.
    FileNotFoundError
        If a file path is supplied but does not exist.
    """
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
    """
    Command-line entry point for the CICD-Textstats tool.

    This function parses CLI arguments, reads the input text, runs
    analysis, and prints results to STDOUT. Errors are written to STDERR
    and result in a non-zero exit code.

    Parameters
    ----------
    argv : list[str] | None, optional
        Argument list to parse (default is None, which uses sys.argv).

    Returns
    -------
    int
        Exit code. '0' indicates success, non-zero indicates failure.
    """
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
