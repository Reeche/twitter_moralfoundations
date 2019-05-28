# twitter_moralfoundations

This is a small project for a university project to download and analyse tweets from followers of certain German parties. 
The project involves analysing tweets based on the moral foundation theory by Haidt. 
1. gettweets.py: downloads the tweets of the follower using tweepy 
2. deletedouble.py: finds unique follower, i.e. follower that only follows one party
3. postprocessing.py: 
    - remove retweets
    - remove words containing @ and http
    - replace corresponding unicode with äöüß
    - lower character and split
4. match.py: count occurences of moral dictionary words. Output is a dictionary with party and count for each category. This output need to be saved in a csv as input for chi_test.py.
5. chi_test.py: does chi-square test for scores
6. countfrequency.py: counts most most occuring words after omitting stopwords