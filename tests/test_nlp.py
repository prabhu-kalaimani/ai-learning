"""
Test for NLP modules

This test module tests the nlp features implemented
"""

from ai_learning.logger_config import get_logger
from ai_learning.nlp.removing_stropwords import filter_stop_words

logger = get_logger(__name__)


def test_remove_stop_words_1():
    text = "It was too far to go to the shop and he did not want her to walk"
    status = filter_stop_words(text)
    logger.info(f"Filtered Text : {status: >25}")
    assert status == "far go shop want walk", f"Output = {status}"


def test_remove_stop_words_2():
    text = "Hello world... welcome to nlp testing..."
    status = filter_stop_words(text)
    logger.info(f"Filtered Text : {status: >25}")
    assert status == "hello world... welcome nlp testing...", f"Output = {status}"
