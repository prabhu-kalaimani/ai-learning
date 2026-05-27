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


class FilterStopWords:
    stp_list = None

    @classmethod
    def load_stop_words(cls, lang: str = "english") -> None:
        """
        Loads the stop words to stp_list
        :param lang: Language
        """
        if lang.lower() == "tamil":
            cls.stp_list = stopwords.words("tamil")
        else:
            cls.stp_list = stopwords.words("english")

    @classmethod
    def get_stopwords(cls) -> list:
        """This method will return the stop words list"""
        return cls.stp_list

    @classmethod
    def filter_stop_words(cls, inp_str: str, lang: str = "english") -> str:
        """
        This method will filter the stop words from the string
        :param inp_str: Input string where stop words will be removed from
        :param lang: language
        :return: String with removed stop words
        """
        if cls.stp_list is None:
            cls.load_stop_words(lang)
        status = " ".join(
            [word for word in inp_str.lower().split() if word not in cls.stp_list]
        )
        return status

    @classmethod
    def append_stopwords(cls, word: str) -> None:
        """
        Method to add new words to stop word list.
        :param word: Word to be added to stop word list
        :return: None
        """
        cls.stp_list.append(word)

    @classmethod
    def remove_stopwords(cls, word: str) -> None:
        """
        Method to remove a word from stop word list
        :param word: Word to be removed
        :return:
        """
        cls.stp_list.remove(word)
