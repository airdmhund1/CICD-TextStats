"""
Core text analysis utilities for the textstat-mini package.

Functions here provide:
- tokenization with simple punctuation stripping
- summary statistics (chars/words/lines)
- top-N most frequent words
"""

from collections import Counter
from typing import Dict, List, Tuple

# Punctuation characters trimmed from token boundaries.
_PUNCT_TO_STRIP = ".,:;!?()[]{}\"'"


def _tokenize(text: str) -> List[str]:
    """
    Convert input text into a list of lowercase word tokens.

    Tokenization strategy:
    - Lowercase the input
    - Split on whitespace
    - Strip a small set of punctuation characters from token boundaries

    Parameters
    ----------
    text : str
        The raw text to tokenize.

    Returns
    -------
    List[str]
        List of tokens (possibly empty).

    Examples
    --------
    >>> _tokenize("Hello, world! Hello...")
    ['hello', 'world', 'hello']
    """
    raw = text.lower().split()
    return [t.strip(_PUNCT_TO_STRIP) for t in raw if t.strip(_PUNCT_TO_STRIP)]


def analyze_text(text: str) -> Dict[str, int]:
    """
    Compute simple statistics for a block of text.

    Statistics include:
      - 'chars': total number of characters
      - 'words': number of tokens after simple tokenization
      - 'lines': number of newline-delimited lines

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    Dict[str, int]
        A mapping with keys 'chars', 'words', and 'lines'.

    Raises
    ------
    TypeError
        If 'text' is not a string.

    Examples
    --------
    >>> analyze_text("Hello\\nworld")
    {'chars': 11, 'words': 2, 'lines': 2}
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    lines = text.splitlines()
    tokens = _tokenize(text)
    return {
        "chars": len(text),
        "words": len(tokens),
        "lines": len(lines),
    }


def top_n_words(text: str, n: int = 5) -> List[Tuple[str, int]]:
    """
    Return the top-N most frequent words.

    Parameters
    ----------
    text : str
        Input text to analyze.
    n : int, optional
        Number of words to return (default is 5). If 'n' <= 0,
        an empty list is returned.

    Returns
    -------
    List[Tuple[str, int]]
        A list of (word, count) pairs in descending frequency order.
        Ties follow the ordering of :meth:`collections.Counter.most_common`.

    Examples
    --------
    >>> top_n_words("a b a c a b d", n=2)
    [('a', 3), ('b', 2)]
    """
    if n <= 0:
        return []
    tokens = _tokenize(text)
    counts = Counter(tokens)
    return counts.most_common(n)
