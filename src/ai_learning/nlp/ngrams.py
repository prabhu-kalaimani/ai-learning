"""
Ngrams Utility

N-grams are contiguous sequences of N items extracted from text. They are a
fundamental concept in Natural Language Processing (NLP) and help capture
local context within text.

Example:
    Sentence: "I love NLP"

    When n = 1 (unigrams):
        ["I", "love", "NLP"]

    When n = 2 (bigrams):
        [("I", "love"), ("love", "NLP")]

Real‑world applications of N‑grams include:
    - Autocomplete and next‑word prediction
    - Spell correction and error detection
    - Search engine ranking and query expansion
    - Text similarity and document comparison
    - Sentiment analysis and feature extraction

This module provides:
    - extract_ngrams: Generate N‑grams from strings or token lists
    - extract_ngram_freq: Compute and visualize N‑gram frequency distributions

Dependencies:
    - nltk        : for generating N‑grams
    - pandas      : for frequency counting
    - matplotlib  : for plotting N‑gram distributions
"""

import nltk
import pandas as pd
import matplotlib.pyplot as plot
from ai_learning import logger_config

logger = logger_config.get_logger(__name__)


class Ngrams:
    """
    A utility class for generating and analyzing N‑grams.

    This class provides two main capabilities:
        - Generating N‑grams from either raw strings or token lists
        - Computing and visualizing N‑gram frequency distributions

    It supports both character‑level and word‑level N‑grams depending on the
    input type. Frequency plots can be displayed normally or automatically
    closed after a specified duration.
    """

    def __init__(self):
        pass

    def extract_ngrams(self, text, ngram_weight):
        """
        Generate N‑grams from the given input sequence.

        This method accepts either a string or a list. When a list is provided,
        it is treated as a sequence of tokens and word‑level N‑grams are
        produced. When a string is provided, it is treated as a sequence of
        characters and character‑level N‑grams are generated.

        Args:
            text (str or list):
                Input text to generate N‑grams from. Can be a raw string or a
                list of tokens.
            ngram_weight (int):
                The size of the N‑gram window (e.g., 1 for unigrams,
                2 for bigrams).

        Returns:
            list:
                A list of N‑gram tuples generated from the input.
        """
        return list(nltk.ngrams(text, ngram_weight))

    def extract_ngram_freq(self, text: list, ngram_weight: int, duration=None):
        """
        Compute and visualize N‑gram frequency counts.

        This method generates N‑grams from the provided token list, computes
        their frequency distribution using pandas Series.value_counts(), and
        plots the top 10 most frequent N‑grams using matplotlib. The plot can
        either remain open or automatically close after a specified duration.

        Args:
            text (list):
                A list of tokens from which N‑grams will be generated. This
                method expects pre‑tokenized input.
            ngram_weight (int):
                The size of the N‑gram window (e.g., 1 for unigrams,
                2 for bigrams).
            duration (int or None):
                Number of seconds to keep the plot open. If None, the plot
                remains open until manually closed. If an integer is provided,
                the plot will auto‑close after the specified number of seconds.

        Returns:
            pandas.Series:
                A Series where the index contains N‑gram tuples and the values
                represent their frequency counts.
        """
        freq = pd.Series(nltk.ngrams(text, ngram_weight)).value_counts()
        logger.info(freq)

        freq[:10].sort_values().plot(kind="bar")
        plot.title(f"N - {ngram_weight} gram plotting")

        if duration is None:
            plot.show()
        else:
            plot.pause(duration)
            plot.close()
        return freq
