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


def remove_stopwords(inp_str: str, lang: str = "eng") -> str:
    if lang == "tamil":
        stp_list = stopwords.words("Tamil")
    else:
        stp_list = stopwords.words("English")

    status = " ".join([word for word in inp_str.lower().split() if word not in stp_list])
    return status


def append_stopwords_dict(word: str, stp_list: dict) -> None:
    stp_list.append(word)


def remove_stopwords_dict(word: str, stp_list: dict) -> None:
    stp_list.remove(word)
