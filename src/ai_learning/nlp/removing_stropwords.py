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

# Original string
inp_str = "It was too far to go to the shop and he did not want her to walk"

# store the stop words in a variable
en_stp = stopwords.words("English")
tam_stp = stopwords.words("Tamil")


# filter all the stop words and create a list ( list comprehension). Don't forget to create lower case
filtered_txt = " ".join(
    [item for item in inp_str.lower().split() if item not in en_stp]
)
print(f"Filtered text : {filtered_txt: >10}")

# You can add words to stop string because it's a list
en_stp.append("go")
filtered_txt = " ".join(
    [item for item in inp_str.lower().split() if item not in en_stp]
)
print(f"Filtered text : {filtered_txt: >10}")

# You can also add words to the stop word dictionary
en_stp.remove("the")
filtered_txt = " ".join(
    [item for item in inp_str.lower().split() if item not in en_stp]
)
print(f"Filtered text : {filtered_txt: >10}")
