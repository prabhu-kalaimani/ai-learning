"""
Tests for the Stemming module.

This test suite validates the behavior of the `Stemming` class and its
`porter_stemming` method. It covers:

- Basic stemming behavior for common verb forms
- Case-insensitive stemming
- Parametrized stemming tests for multiple word variations
"""

import pytest
from ai_learning import logger_config
from ai_learning.nlp.stemming_lamitization import Stemming, Lamitization

logger = logger_config.get_logger(__name__)


@pytest.mark.parametrize("word", ["connecting", "connected", "connecting", "connects"])
def test_ps_connect(word):
    """Test that different forms of 'connect' stem to 'connect'.

    Args:
        word (str): A variation of the word "connect".

    Asserts:
        The stemmed output equals "connect".
    """
    st = Stemming()
    result = st.porter_stemming(word)
    assert result == "connect"


@pytest.mark.parametrize(
    "word, expected",
    [
        ("learn", "learn"),
        ("leaning", "lean"),
        ("learnt", "learnt"),
        ("learners", "learner"),
    ]
)
def test_ps_learn(word, expected):
    """Test stemming for variations of the word 'learn'.

    Args:
        word (str): Input word to stem.
        expected (str): Expected stemmed output.

    Asserts:
        The stemmed output matches the expected value.
    """
    st = Stemming()
    result = st.porter_stemming(word.lower())
    assert result == expected


def test_ps_check_case():
    """Test that stemming is case-insensitive.

    This test ensures that mixed-case variations of 'connect' all stem
    to the same lowercase root.

    Asserts:
        All variations stem to "connect".
    """
    inpt_txt = ["coNNecting", "Connected", "ConnectinG", "connectS"]
    st = Stemming()
    for word in inpt_txt:
        result = st.porter_stemming(word)
        assert result == "connect"

@pytest.mark.parametrize("word, expected", [
    ("coNNecting","connecting"),
    ("Connected", "connected"),
    ("connectivity","connectivity"),
    ("connectS", "connects"),
    ("likes","like"),
    ("worse","worse")
])
def test_lam(word, expected):
    lm = Lamitization()
    result = lm.word_lamitizer(word)
    logger.info(f"{word} : {result}")
    assert result == expected
