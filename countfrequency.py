# -*- coding: utf-8 -*-

import pandas as pd
import warnings
import matplotlib.pyplot as plt
import nltk
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', 200)


#CDU = pd.read_csv('CDU_processed.csv', sep=";", header=0, encoding='utf-8')
#SPD = pd.read_csv('SPD_processed.csv', sep=";", header=0, encoding='utf-8')
#AFD = pd.read_csv('AFD_processed.csv', sep=";", header=0, encoding='utf-8')
#FDP = pd.read_csv('FDP_processed.csv', sep=";", header=0, encoding='utf-8')
Gruene = pd.read_csv('Gruene_processed.csv', sep=";", header=0, encoding='utf-8')
#Linke = pd.read_csv('Linke_processed.csv', sep=";", header=0, encoding='utf-8')

Gruene = Gruene.head(10)

def countwords(data):
    count = sum(data['text'].str.count(' ') + 1)
    #count = sum(data['text'].str.len())
    return count

def countmostfrequent(party):
    results = pd.Series([y for x in party['text'].values.flatten() for y in x.split()]).value_counts()
    results = results.to_frame()
    results['index'] = results.index
    results['index'] = results['index'].str.replace("'", "").str.replace(",", "")

    file = open('german_stopwords.txt', 'r')
    manual_stop_words = file.read()
    manual_stop_words = manual_stop_words.split("\n")
    test = results[~results.index.str.contains('|'.join(manual_stop_words))]
    print(test)
    #test.to_csv('Gruene_mostfrequent.csv', index=False)
    pass



def countmostfrequentmfd(party):

    results = party['text'].tolist()
    #print(results[0])

    mfd = pd.read_csv('wertung_withoutstar.csv', sep=",", header=0, encoding='utf-8')
    words = mfd.iloc[:, 0].to_frame()
    words = words.set_index("word", drop=True)

    words['count'] = 0
    #words.columns = ['word', 'count']
    print("print", words.loc["gewalt", "count"])

    #countoccurences = []
    occurences = 0
    for word in words:
        for i in range(len(results)):
            occurences += results[i].count(str(word))
            print(occurences)
        words.loc[str(word), 'count'] = occurences
        #occurences = results[i].count(str(word))
    #countoccurences.append(occurences)
        #words.loc[words['word'] == word]['count'] = occurences
        #words['word'][word].append(occurences)

    print(words)

    #test.to_csv('Gruene_mostfrequent.csv', index=False)
    pass

countmostfrequentmfd(Gruene)

#mfd = pd.read_csv('wertung_withoutstar.csv', sep=",", header=0, encoding='utf-8')
#words = mfd.iloc[:, 0]
#liste = []
#for word in words:
#    counts = Gruene['text'].contain(word).sum()
#    liste.append(counts)
#print(len(liste))
