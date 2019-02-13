import re, string, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from PIL import Image
from nltk.corpus import stopwords
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)


def remove_punctuations_and_stopwords(tokens):
    stop = stopwords.words('english')
    taboo = [p for p in string.punctuation] + stop 
    cleaned_tokens = [tok for tok in tokens if tok.lower() not in taboo if not tok.startswith('http')]
    return cleaned_tokens


def preprocess(s, lowercase=True, join=True):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
#     tokens = [t for t in tokens if not t.startswith('http')]
    tokens = remove_punctuations_and_stopwords(tokens)    
    if join:
        return ' '.join(tokens)
    else:
        return tokens