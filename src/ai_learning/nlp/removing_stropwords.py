"""
Utilities for removing stop words as part of the NLP preprocessing pipeline.

Stop words are high‑frequency terms—such as "the", "is", and "and"—that typically
carry little meaningful information for downstream machine learning tasks. This
module uses the NLTK library to identify and remove these words from raw text,
resulting in cleaner and more informative input for NLP models.

Steps:
1. import the nltk  module and download the stopwords. Note. If this is the first time then it will take some time to download
2. From the corpus import stop words
3. Create a variable and extract the stop words

"""

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")


def filter_stop_words(inp_str: str, lang: str = "eng") -> str:
    """
    This method will filter the stop words from the string
    :param inp_str: Input string where stop words will be removed from
    :param lang: language
    :return: String with removed stop words
    """
    if lang == "tamil":
        stp_list = stopwords.words("tamil")
    else:
        stp_list = stopwords.words("english")

    status = " ".join(
        [word for word in inp_str.lower().split() if word not in stp_list]
    )
    return status


def append_stopwords(word: str, stp_list: list) -> None:
    """
    Method to add new words to stop word list.
    :param word: Word to be added to stop word list
    :param stp_list: Stop word list
    :return: None
    """
    stp_list.append(word)


def remove_stopwords(word: str, stp_list: dict) -> None:
    """
    Method to remove a word from stop word list
    :param word: Word to be removed
    :param Stop word list : stop word list
    :return:
    """
    stp_list.remove(word)
