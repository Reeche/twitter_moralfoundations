# Python code to look at specific words in their original context
# MUSS noch angepassst werden!!

import nltk.corpus
from nltk.text import Text

# Open the text file you wish to search (user = labour or conservative)
f=open('userTweets_inclusionCriteriaMet_CLEANED.txt','rU')
raw=f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
# words= list of words to search for in context e.g. words = ['peace','family']
words = []
# search the file for words in the list and return them in context (100characters wide) up to 20 times
for items in words:
    text.concordance(items,width=100, lines=20)

# output appears in the python console
