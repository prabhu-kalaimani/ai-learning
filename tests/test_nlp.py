"""
Test for NLP modules

This test module tests the nlp features implemented
"""

from ai_learning.logger_config import get_logger

logger = get_logger(__name__)


def test_hello_nlp():
    logger.info(f"Testing hello world for NLP module")
    assert True
