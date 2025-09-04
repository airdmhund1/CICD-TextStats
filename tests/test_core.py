"""
Unit tests for textstat_mini.core.

These tests validate the core functionality:
- Text statistics (chars, words, lines)
- Word frequency analysis
"""

import pytest

from textstat_mini.core import _tokenize, analyze_text, top_n_words


def test_analyze_text_basic():
    """analyze_text should correctly count characters, words, and lines."""
    text = "Hello world!\nHello again."
    stats = analyze_text(text)
    assert stats["lines"] == 2
    assert stats["words"] == 4
    assert stats["chars"] == len(text)


def test_top_n_words_default():
    """top_n_words should return the most frequent tokens in order."""
    text = "a b a c a b d"
    top = top_n_words(text)
    assert top[0] == ("a", 3)
    assert top[1] == ("b", 2)


def test_top_n_words_n_zero():
    assert top_n_words("a b c", 0) == []


def test_analyze_text_type_error():
    with pytest.raises(TypeError):
        analyze_text(123)


def test_tokenize_strips_punct_and_lowercases():
    tokens = _tokenize("Wow!! This, THIS... wow?")
    assert tokens == ["wow", "this", "this", "wow"]
