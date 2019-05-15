import pandas as pd


CDU_original = pd.read_csv('CDUall_tweets.csv', encoding='utf-8')
SPD_original = pd.read_csv('SPDall_tweets.csv', encoding='utf-8')
AFD_original = pd.read_csv('AFD_tweets.csv', encoding='utf-8')
FDP_original = pd.read_csv('FDP_tweets.csv', encoding='utf-8')
Gruene_original = pd.read_csv('Gruene_tweets.csv', encoding='utf-8')
Linke_original = pd.read_csv('dieLinkeall-tweets.csv', encoding='utf-8')


# drop all duplicated IDs, do this for all parties
cdu_unique = CDU_original['id'].drop_duplicates(keep='first')
spd_unique = SPD_original['id'].drop_duplicates(keep='first')
afd_unique = AFD_original['id'].drop_duplicates(keep='first')
fdp_unique = FDP_original['id'].drop_duplicates(keep='first')
gruene_unique = Gruene_original['id'].drop_duplicates(keep='first')
linke_unique = Linke_original['id'].drop_duplicates(keep='first')


# concatenate all unique ids into one list and then remove the duplicates
# keep = false will cause all duplicates one to be removed, i.e. only ids that appear only in ONE party will stay
id_list = pd.concat([cdu_unique, spd_unique, afd_unique, fdp_unique, gruene_unique, linke_unique])
unique_id = id_list.drop_duplicates(keep=False)


CDU_cleaned = CDU_original[~CDU_original['id'].isin(unique_id)]
SPD_cleaned = SPD_original[~SPD_original['id'].isin(unique_id)]
AFD_cleaned = AFD_original[~AFD_original['id'].isin(unique_id)]
FDP_cleaned = FDP_original[~FDP_original['id'].isin(unique_id)]
Gruene_cleaned = Gruene_original[~Gruene_original['id'].isin(unique_id)]
Linke_cleaned = Linke_original[~Linke_original['id'].isin(unique_id)]
#print(len(CDU_cleaned))


CDU_cleaned.to_csv('CDU_cleaned.csv', index = None, header=True)
SPD_cleaned.to_csv('SPD_cleaned.csv', index = None, header=True)
AFD_cleaned.to_csv('AFD_cleaned.csv', index = None, header=True)
FDP_cleaned.to_csv('FDP_cleaned.csv', index = None, header=True)
Gruene_cleaned.to_csv('Gruene_cleaned.csv', index = None, header=True)
Linke_cleaned.to_csv('Linke_cleaned.csv', index = None, header=True)