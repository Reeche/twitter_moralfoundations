# -*- coding: utf-8 -*-

import pandas as pd
import warnings
warnings.filterwarnings("ignore")


CDU = pd.read_csv('CDU_cleaned.csv', encoding='utf-8')
SPD = pd.read_csv('SPD_cleaned.csv', encoding='utf-8')
AFD = pd.read_csv('AFD_cleaned.csv', encoding='utf-8')
FDP = pd.read_csv('FDP_cleaned.csv', encoding='utf-8')
Gruene = pd.read_csv('Gruene_cleaned.csv', encoding='utf-8')
Linke = pd.read_csv('Linke_cleaned.csv', encoding='utf-8')

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

    # replace unicode to äöü
    for i in range(len(data['text'])):
       data['text'][i] = data['text'][i].replace("\\xc3\\xbc", "ü")
       data['text'][i] = data['text'][i].replace("\\xc3\\xa4", "ä")
       data['text'][i] = data['text'][i].replace("\\xc3\\xb6", "ö")
       data['text'][i] = data['text'][i].replace("\\xc3\\x9f", "ß")
       #data['text'][i] = data['text'][i].replace("&amp;", " ")
       data['text'][i] = data['text'][i].replace(";", " ")
       #data['text'][i] = data['text'][i].replace("'", " ")
       #data['text'][i] = data['text'][i].replace('"', " ")

    # convert to lowercase, best not to split but the further analysis was done using split()
    data['text'] = data['text'].str.lower().split()


    # remove multiple and trailing spaces. but why???

    print(data['text'][5])
    processed_data = data
    return processed_data


file1 = preprocessing(CDU)
file1.to_csv('CDU_processed_nosplit.csv', sep=";", index = None, header=True)

file2 = preprocessing(SPD)
file2.to_csv('SPD_processed_nosplit.csv', sep=";", index = None, header=True)

file3 = preprocessing(FDP)
file3.to_csv('FDP_processed_nosplit.csv', sep=";", index = None, header=True)

file4 = preprocessing(AFD)
file4.to_csv('AFD_processed_nosplit.csv', sep=";", index = None, header=True)

file5 = preprocessing(Gruene)
file5.to_csv('Gruene_processed_nosplit.csv', sep=";", index = None, header=True)

file6 = preprocessing(Linke)
file6.to_csv('Linke_processed_nosplit.csv', sep=";", index = None, header=True)

