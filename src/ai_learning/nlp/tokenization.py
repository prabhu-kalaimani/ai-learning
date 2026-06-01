"""Tokenization of words and sentences

Tokenization is the process of splitting text into smaller units called tokens.
Tokens can be words, sentences, sub‑words, or characters. This is an essential
step in NLP because it helps us analyze the structure and statistics of text.

We use NLTK for tokenization. Before using NLTK's tokenizers, we must download
the 'punkt' model, which contains rules for identifying sentence and word
boundaries.

NLTK provides:
- sent_tokenize()  → splits text into sentences
- word_tokenize()  → splits text into words
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# download punk_tab which is used to find where the sentences begin
nltk.download("punkt_tab")


class Tokenize:
    """Utility class for NLTK-based text tokenization."""

    @staticmethod
    def word_tokenize(txt: str) -> list[str]:
        """
        Args:
            txt: The input text to tokenize.

        Returns:
            A list of word token strings.

        Example:
        >>> word_tokenize("Hello world")
        ['Hello', 'world']
        """
        if not isinstance(txt, str):
            raise TypeError("Input text must be a string")
        return word_tokenize(txt.lower())

    @staticmethod
    def sentence_tokenize(txt: str) -> list[str]:
        """
        This method tokenizes sentences. If there are multiple sentences then it is extracted and
        returned as a list of sentences
        Args:
            txt: Input sentences

        Returns:
            List of sentences
        """
        if not isinstance(txt, str):
            raise TypeError("Input text must be a string")
        return sent_tokenize(txt.lower())
