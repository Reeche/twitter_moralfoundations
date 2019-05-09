import pandas as pd


CDU_original = pd.read_csv('CDUall_tweets.csv', encoding='utf-8')
SPD_original = pd.read_csv('SPDall_tweets.csv', encoding='utf-8')
CDU_original = CDU_original.astype(str)
SPD_original = SPD_original.astype(str)

# drop all duplicated IDs, do this for all parties
cdu_unique = CDU_original['id'].drop_duplicates(keep='first')
spd_unique = SPD_original['id'].drop_duplicates(keep='first')


# concatenate all unique ids into one list and then remove the duplicates
# keep = false will cause all duplicates one to be removed, i.e. only ids that appear only in ONE party will stay
id_list = pd.concat([cdu_unique, spd_unique])
unique_id = id_list.drop_duplicates(keep=False)


CDU_cleaned = CDU_original[~CDU_original['id'].isin(unique_id)]
SPD_cleaned = SPD_original[~SPD_original['id'].isin(unique_id)]
#print(len(CDU_cleaned))


CDU_cleaned.to_csv('CDU_cleaned.csv', index = None, header=True)