# -*- coding: utf-8 -*-
import pandas as pd
from ast import literal_eval
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)



df1 = pd.read_csv('FDP_processed.csv', sep=";", header=0, encoding="utf-8", low_memory=False)
df1['scores'] = np.nan
df1['party'] = 'fdp'
data = df1

#df2 = pd.read_csv('SPD_processed_v2.csv', sep=";", header=0, encoding="utf-8", low_memory=False)
#df2['scores'] = np.nan
#df2['party'] = 'spd'

#df3 = pd.read_csv('Gruene_processed_v2.csv', sep=";", header=0, encoding="utf-8", low_memory=False)
#df3['scores'] = np.nan
#df3['party'] = 'gruene'
#data = df1.append([df2, df3], ignore_index=True)


# this creates a list of all words and corresponding number
wertung = pd.read_csv('wertung_original.csv', sep=",", encoding="utf-8", low_memory=False)
wertung['word'] = wertung['word'].astype(str)
df1 = wertung[['word', 'score_1']].dropna()
df1.rename(index=str, columns={'score_1': 'scores'}, inplace=True)
df2 = wertung[['word', 'score_2']].dropna()
df2.rename(index=str, columns={'score_2': 'scores'}, inplace=True)
df3 = wertung[['word', 'score_3']].dropna()
df3.rename(index=str, columns={'score_3': 'scores'}, inplace=True)
wertung = df1.append(df2.append(df3, ignore_index=True), ignore_index=True)

#%%
#print(data.columns)
#print(wertung.head(500))

for index in data.index:
    word_list = literal_eval(data.get_value(index, 'text'))
    #print(word_list)
    word_matched = []
    for word in word_list:
        for index_ in wertung.index:
            word_ = wertung.get_value(index_, 'word')
            # match word from wertung list
            if word.find(word_) != -1:
                # if found, get the score of the found word and append to the list
                score = wertung.get_value(index_, 'scores')
                word_matched.append(score)
    data.iloc[index, 6] = str(word_matched)
#print(data.iloc[index, 6])

def f(x):
    return pd.Series(dict(scores="{%s}" % ', '.join(x['scores'])))


party_count = pd.DataFrame(data=data, columns=['party', 'scores']).groupby('party').apply(f)
for index in party_count.index:
    score_dict = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
    }
    scores = party_count.get_value(index, 'scores').replace("[", "").replace("]", "").replace(",", "").replace("{",
                                                                                                               "").replace(
        "}", "").split(' ')
    for score in scores:
        if score != '':
            try:
                number = str(int(float(score)))
                if number in score_dict:
                    score_dict[number] += 1
            except:
                pass
    print(index, score_dict)
