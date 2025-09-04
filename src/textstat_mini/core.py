from collections import Counter
from typing import Dict, List, Tuple


def _tokenize(text: str) -> List[str]:
    raw = text.lower().split()
    return [t.strip(".,:;!?()[]{}\"'") for t in raw if t.strip(".,:;!?()[]{}\"'")]


def analyze_text(text: str) -> Dict[str, int]:
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
    if n <= 0:
        return []
    tokens = _tokenize(text)
    counts = Counter(tokens)
    return counts.most_common(n)
