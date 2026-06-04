"""
Unit tests for the Ngrams utility class.

This module validates both n-gram generation and n-gram frequency
computation for different input types. It ensures that the Ngrams class
correctly handles:

    - Character-level n-grams from raw strings
    - Word-level n-grams from token lists
    - Frequency counting of n-grams using pandas Series
    - Auto-closing matplotlib plots during frequency visualization

The tests cover unigrams, bigrams, and frequency-based assertions to verify
that the underlying NLP logic behaves consistently and produces accurate,
deterministic results.
"""

from ai_learning.nlp.ngrams import Ngrams
import pandas as pd

inp_txt = [
    'the', 'rise', 'of', 'artificial', 'intelligence', 'has', 'led', 'to',
    'significant', 'advancements', 'in', 'natural', 'language', 'processing',
    'computer', 'vision', 'and', 'other', 'fields', 'machine', 'learning',
    'algorithms', 'are', 'becoming', 'more', 'sophisticated', 'enabling',
    'computers', 'to', 'perform', 'complex', 'tasks', 'that', 'were', 'once',
    'thought', 'to', 'be', 'the', 'exclusive', 'domain', 'of', 'humans',
    'with', 'the', 'advent', 'of', 'deep', 'learning', 'neural', 'networks',
    'have', 'become', 'even', 'more', 'powerful', 'capable', 'of',
    'processing', 'vast', 'amounts', 'of', 'data', 'and', 'learning', 'from',
    'it', 'in', 'ways', 'that', 'were', 'not', 'possible', 'before', 'as',
    'a', 'result', 'ai', 'is', 'increasingly', 'being', 'used', 'in', 'a',
    'wide', 'range', 'of', 'industries', 'from', 'healthcare', 'to',
    'finance', 'to', 'transportation', 'and', 'its', 'impact', 'is', 'only',
    'set', 'to', 'grow', 'in', 'the', 'years', 'to', 'come'
]


def test_unigram_string():
    """
    Test character-level n-gram generation from a string.

    Ensures that extract_ngrams treats a raw string as a sequence of
    characters and returns the correct 2-gram (bigram) tuples.
    """
    ng = Ngrams()
    text = "Python"
    result = ng.extract_ngrams(text, 2)

    assert result == [
        ('P', 'y'),
        ('y', 't'),
        ('t', 'h'),
        ('h', 'o'),
        ('o', 'n')
    ]


def test_unigram_array():
    """
    Test word-level n-gram generation from a list of tokens.

    Ensures that extract_ngrams correctly generates word-level bigrams
    when a list of tokens is provided.
    """
    ng = Ngrams()
    txt_list = "I love python".split()
    result = ng.extract_ngrams(txt_list, 2)

    assert result == [
        ("I", "love"),
        ("love", "python")
    ]


def test_unigram_freq():
    """
    Test unigram frequency computation from a token list.

    Ensures that extract_ngram_freq correctly counts 1-gram occurrences
    and returns a pandas Series where specific unigrams have expected
    frequencies.
    """
    ng = Ngrams()
    result = ng.extract_ngram_freq(inp_txt, 1, duration=5)

    # 'to' appears 7 times in the sample text
    assert result[('to',)] == 7


def test_bigram_freq():
    """
    Test bigram frequency computation from a token list.

    Ensures that extract_ngram_freq correctly counts 2-gram occurrences
    and returns accurate frequency values for known bigrams.
    """
    ng = Ngrams()
    result = ng.extract_ngram_freq(inp_txt, 2, duration=5)

    # ('that', 'were') appears exactly twice in the sample text
    assert result[('that', 'were')] == 2
