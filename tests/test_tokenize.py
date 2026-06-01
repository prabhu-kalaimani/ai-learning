"""Test module for the Tokenize class."""

import pytest
from ai_learning.nlp.tokenization import Tokenize
from ai_learning.logger_config import get_logger

logger = get_logger(__name__)


def test_wt():
    """Test that valid input is correctly split into word tokens."""
    inp_txt = "Hello world welcome to text tokenization"
    res = Tokenize.word_tokenize(txt=inp_txt)
    logger.info(f"Tokenized output: {res}")
    assert res == ["Hello", "world", "welcome", "to", "text", "tokenization"]


def test_wt_empty_string():
    """Test that empty string input returns an empty list."""
    res = Tokenize.word_tokenize(txt="")
    logger.info(f"Tokenized output: {res}")
    assert res == []


def test_wt_none():
    """Test that None input raises TypeError

    Args:
        None

    Raises:
        TypeError: If txt is not a string.
    """
    with pytest.raises(TypeError):
        Tokenize.word_tokenize(txt=None)


def test_st():
    """Test sentence tokenizer"""
    inp_txt = "HeLLo there. Welcome to sentence tokenizer"
    result = Tokenize.sentence_tokenize(inp_txt)
    assert len(result) == 2
    assert "hello there." in result
    assert "welcome to sentence tokenizer" in result
