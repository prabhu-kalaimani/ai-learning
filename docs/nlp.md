# NLP Basiccs

Natural Language Processing or NLP is ues in Search engines, chatbots and various other AI applications.
Three are two tpe of Learning that is available in NLP.

**- Supervised Learning**
  - Learning using labeled data
  
**- Unsupervised Learning**
  - Learning unlabeled data

Topics Covered in this module
1. Text pre-processing
2. Extract Key components
3. Sentiment Analysis
4. Text Vectorization
5. Topic Modelling
6. Creating Custom Classifiers
7. Example application
8. Feature of NLP


Text Pre-Processing:

1. Lower Casing text
The first step in pre-processing is to convert the text to lower case. This will help to reduce the number of tokens
as computer sees apple and Apple as two different string. In python we use str.lower() method to convert to lower case

Example:
```python
--8<-- "src/ai_learning/nlp/nlp.py:1:60"
```

2. Removing Stop words
This is the first step in nlp. Stop words does not make any sense to machine learning. Example Stop words ( is, in , the, off)
We use nltk library from python to remove stop words in our example.