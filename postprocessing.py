import pandas as pd
import string
import re

CDU = pd.read_csv('CDU_tweets.csv', encoding='utf-8')
CDU = CDU.astype(str)

def preprocessing(data):
    # remove @usernames
    for i in range(len(data['text'])):
        txt = data['text'][i]
        txt2 = ' '.join(word for word in txt.split(' ') if not word.startswith("b'@"))
        data['text'][i] = ' '.join(word for word in txt2.split(' ') if not word.startswith("@"))


    # if b'RT is contained in the tweet, it is a retweet and will be removed
    data = data[~data['text'].str.contains("b'RT")]
    data = data.reset_index()


    # remove punctuation except for apostrophes, excluding hashtag symbols
    punctuations = '''!()-[]{};:"\,<>./?@$%^&*_~'''
    for i in range(len(data['text'])):
        data['text'][i] = data['text'][i].replace(punctuations, "")


    # remove URLS
    for i in range(len(data['text'])):
        txt = data['text'][i]
        data['text'][i] = ' '.join(word for word in txt.split(' ') if not word.startswith("http"))


    # convert to lowercase
    data['text'] = data['text'].str.lower()

    # remove multiple and trailing spaces. but why???

    print(data['text'][14])
    processed_data = data
    return processed_data

print(preprocessing(CDU))