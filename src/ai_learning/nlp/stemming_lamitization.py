"""
Stemming and Lemmatization

This module provides utilities for reducing words to their base or root forms
using two common NLP techniques: stemming and lemmatization.

Stemming:
    Stemming is the process of reducing a word to its root form by applying
    rule‑based heuristics. For example:
        - "connecting" → "connect"
        - "connected"  → "connect"

    Stemming is useful in NLP tasks where different inflected forms of a word
    should be treated as the same term. However, because stemming is purely
    rule‑based, the results are not always linguistically accurate. For example:
        - "worse" → "wors"

    This module uses the Porter Stemmer, a classic and widely used
    rule‑based stemming algorithm.

Lemmatization:
    Lemmatization reduces a word to its dictionary (lemma) form using lexical
    knowledge bases such as WordNet. This approach is more linguistically
    accurate than stemming, but often requires downloading and loading
    external lexical resources.

    The first step is to download the WordNet lexical database and then use
    the WordNetLemmatizer to obtain the correct lemma for each word.

    Lemmatization Example:
        Lemmatization uses lexical knowledge to return the true dictionary form
        of a word. Unlike stemming, it produces linguistically correct results.

        Examples:
            - "running"  → "run"
            - "mice"     → "mouse"
            - "better"   → "good"
            - "cars"     → "car"

        Comparison with stemming:
            - Stemming:     "running" → "run"
            - Lemmatizing:  "running" → "run"

            - Stemming:     "better" → "better"   (incorrect)
            - Lemmatizing:  "better" → "good"     (correct)

    Lemmatization typically produces cleaner and more accurate results, but
    many words may already be in their lemma form and therefore remain
    unchanged.
"""

import nltk
from nltk.stem import PorterStemmer
from ai_learning import logger_config
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")

logger = logger_config.get_logger(__name__)


class Stemming:
    """A utility class for performing stemming using the Porter Stemmer."""

    def __init__(self):
        self.ps = PorterStemmer()

    def porter_stemming(self, txt: str) -> str:
        """
        Stem a single word using the Porter stemming algorithm.

        Args:
            txt (str): The input word to stem.

        Returns:
            str: The stemmed (root) form of the word.

        Raises:
            ValueError: If the input is not a string.
        """
        if not isinstance(txt, str):
            raise ValueError("Input must be a string")
        stemmed_output = self.ps.stem(txt)
        logger.info(f"{txt} : {stemmed_output}")
        return stemmed_output


class Lemmatization:
    """A utility class for performing lemmatization using WordNet."""

    def __init__(self):
        self.lam = WordNetLemmatizer()

    def word_lemmatizer(self, txt: str) -> str:
        """
        Lemmatize a single word using the WordNet lemmatizer.

        Args:
            txt (str): The input word to lemmatize.

        Returns:
            str: The lemma (dictionary root form) of the word.

        Raises:
            ValueError: If the input is not a string.
        """
        if not isinstance(txt, str):
            raise ValueError("Input must be a string")
        lam_output = self.lam.lemmatize(txt.lower())
        logger.info(f"{txt} : {lam_output}")
        return lam_output
