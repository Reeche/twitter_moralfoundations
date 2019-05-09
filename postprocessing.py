# -*- coding: utf-8 -*-

import pandas as pd


CDU = pd.read_csv('CDU_cleaned.csv', encoding='utf-8')
#CDU = CDU.astype(str)
#CDU = CDU.head(100)

def preprocessing(data):

    # if b'RT is contained in the tweet, it is a retweet and will be removed
    data = data[~data['text'].str.contains("b'RT")]
    data = data.reset_index()

    # remove @usernames
    for i in range(len(data['text'])):
        txt = data['text'][i]
        data['text'][i] = ' '.join(word for word in txt.split(' ') if not "@" in word)

    # remove punctuation except for apostrophes, excluding hashtag symbols
    #punctuations = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    #for i in range(len(data['text'])):
    #    data['text'][i] = data['text'][i].replace(punctuations, "")


    # remove URLS
    for i in range(len(data['text'])):
        txt = data['text'][i]
        #data['text'][i] = ' '.join(word for word in txt.split(' ') if not word.startswith("http"))
        data['text'][i] = ' '.join(word for word in txt.split(' ') if not "http" in word)


    # convert to lowercase
    data['text'] = data['text'].str.lower()

    # replace unicode to äöü
    for i in range(len(data['text'])):
       data['text'][i] = data['text'][i].replace("\\xc3\\xbc", "ü")
       data['text'][i] = data['text'][i].replace("\\xc3\\xa4", "ä")
       data['text'][i] = data['text'][i].replace("\\xc3\\xb6", "ö")


    # remove multiple and trailing spaces. but why???

    #print(data['text'][5])
    processed_data = data
    return processed_data


file = preprocessing(CDU)
file.to_csv('output.csv', index = None, header=True)
