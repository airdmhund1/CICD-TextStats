import pytest

from textstat_mini.core import analyze_text, top_n_words


def test_analyze_text_basic():
    text = "Hello world!\nHello again."
    stats = analyze_text(text)
    assert stats["lines"] == 2
    assert stats["words"] == 3
    assert stats["chars"] == len(text)


def test_top_n_words_default():
    text = "a b a c a b d"
    top = top_n_words(text)
    assert top[0] == ("a", 3)
    assert top[1] == ("b", 2)


def test_top_n_words_n_zero():
    assert top_n_words("a b c", 0) == []


def test_analyze_text_type_error():
    with pytest.raises(TypeError):
        analyze_text(123)
