"""
Test Suite for NLP Stopword Filtering

This module contains unit tests for validating the functionality of the
FilterStopWords class, which provides stopword loading, filtering, and
dynamic modification capabilities for NLP preprocessing.
"""

import copy
from ai_learning.logger_config import get_logger
from ai_learning.nlp.removing_stropwords import FilterStopWords

logger = get_logger(__name__)


def test_filter_stop_words_1():
    """
    Test Case: Basic English stopword filtering

    Purpose:
        Ensures that the stopword filtering logic correctly removes common
        English stopwords from a natural-language sentence.

    Expected Behavior:
        Only meaningful, non-stopword tokens should remain in the output.
    """
    text = "It was too far to go to the shop and he did not want her to walk"
    status = FilterStopWords.filter_stop_words(text)
    logger.info(f"Filtered Text : {status: >25}")

    assert status == "far go shop want walk", f"Output = {status}"


def test_filter_stop_words_2():
    """
    Test Case: Stopword filtering with punctuation

    Purpose:
        Verifies that punctuation is preserved and only stopwords are removed.
        Ensures lowercase normalization and correct token filtering.

    Expected Behavior:
        Non-stopword tokens remain intact, including punctuation.
    """
    text = "Hello world... welcome to nlp testing..."
    status = FilterStopWords.filter_stop_words(text)
    logger.info(f"Filtered Text : {status: >25}")

    assert status == "hello world... welcome nlp testing...", f"Output = {status}"


def test_remove_stopwords():
    """
    Test Case: Dynamic stopword removal

    Purpose:
        Validates that removing a word from the stopword list correctly affects
        subsequent filtering operations.

    Notes:
        - A deep copy is required because get_stopwords() returns a reference
          to the same underlying list.
        - Removing a stopword should cause it to appear in the filtered output.

    Expected Behavior:
        - The removed word must exist in the original stopword list.
        - The removed word must NOT exist in the updated stopword list.
    """
    # Load default English stopwords
    FilterStopWords.load_stop_words()

    # Deep copy to avoid reference sharing
    org_stp_words = copy.deepcopy(FilterStopWords.get_stopwords())

    remove_word = "all"  # Removing this should allow it to appear in filtered text
    FilterStopWords.remove_stopwords(remove_word)

    removed_stp_words = FilterStopWords.get_stopwords()

    # Assertions
    assert remove_word in org_stp_words, "Word should exist in original stopword list"
    assert remove_word not in removed_stp_words, (
        "Word should be removed from stopword list"
    )
