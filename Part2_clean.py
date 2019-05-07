# Part 2
# Repeat this code twice swapping around user and otheruser
# What do I do if I have 6 groups?
# Can I copy part 2 six times for each party?
# Sind Umlaute ein Problem?

user = 'CDU'
otheruser = ''  # idk what to type in here?

total = 15000  # specify max number of follower timelines to collect here (expect 180 every 15 min)
inclusion = 20  # specify minimum number of tweets per follower timeline inclusion criteria

APP_KEY = '1LkXJ9SqzQm7an39boqQ5AW0v'
APP_SECRET = 'eEDlvPcEEfJPKVR1HkIYCmR0BcsISQWXhzjudaNHvMYj3cGgh7'
OAUTH_TOKEN = '911681697577611264-lQDqG7lcZGjvL1vIvrR3qKTlaPZH3Xp'
OAUTH_TOKEN_SECRET = 'AZqWtegYKM7GrsN0AVmwaqMHQH72R85lzaEwQvpflam8x'

from twython import Twython, TwythonError
import time
import random
import re
import unicodedata

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

print('Twython initialized...')

# check both files and remove user ID's that appear in both - eliminating user that follower all accounts from the analysis
# so I don't know how to do it for six parties
# the following are the original codes

followerlistfinal = []
lines_seen = set()
with open(user + 'FollowersIDsCleaned.txt', 'r') as fin:
    with open(otheruser + 'FollowersIDsCleaned.txt', 'r') as fax:
        same = set(fin).difference(fax)

with open(user + 'FollowersIDsCleanedAgain.txt', 'w') as final:
    for line in same:
        final.write(line)
        followerlistfinal.append(line)
fin.close()
fax.close()
final.close()
print('total follower IDs = ', len(followerlistfinal))
random.shuffle(followerlistfinal)
print('done')

# collect up to 200 of each followers most recent Tweets
# rate limited to 180 requests per 15 minutes
# http: // dev.twitter.com / docs / api / 1.1 / get / statuses / user_timeline
# file outputs: <user>Tweets.txt <user>Followers.txt <user>TweetTimes.txt

print('Collecting Tweets from up to ' + str(total) + 'randomly selected follower timelines...')
iter = 0
totalcount = 0
final = open(user + 'FollowersIDsCleanedAgain.txt', 'r')
TweetText = open(user + 'Tweets.txt', 'w')
TweetTimes = open(user + 'TweetTimes.txt', 'w')
UserInfo = open(user + 'Followers.txt', 'w')
for person in followerlistfinal:
    totalcount += 1
    iter += 1
    if iter == 180:
        print('waiting 15 mins for new rate limit window...')
        time.sleep(910)
        iter = 0
    if totalcount == total:
        break
    print(totalcount)
    try:
        user_timeline = twitter.get_user_timeline(user_id=person, count=200)
        total_tweets = len(user_timeline)
        if total_twets > 0:
            all_tweets = ""
            tweet_times = ""
            for tweet in user_timeline:
                if not tweet['retweeted'] and 'RT @' not in tweet['text']:  # removes retweeted tweets
                    text = tweet['text']
                    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')  # gets rid of emojis
                    text_created_at = tweet['created_at']
                    user_id = tweet['user']['id_str']
                    user_lang = tweet['user']['lang']
                    user_location = tweet['user']['location']
                    user_time_zone = tweet['user']['time_zone']
                    user_account_created_at = tweet['user']['created_at']
                    user_screen_name = tweet['user']['screen_name']
                    all_tweets = all_tweets + str(text)
                    tweet_times = tweet_times + str(text_created_at)
                    user_info = '%s\t %s\t %s\t %s\t %s\t %s\t %s\n' % (
                    user_id, total_tweets, user_lang, user_location, user_time_zone, user_account_created_at,
                    user_screen_name)
        TweetText.write(user_id + '\t' + all_tweets + '\n')
        TweetTimes.write(user_id + '\t' + tweet_times + '\n')
        UserInfo.write(user_info)
    except:
        pass
TweetText.close()
TweetTimes.close()
UserInfo.close()

# Apply inclusion criteria
# File outputs: <user> Tweets_InclusionCriteriaMet.txt, <user>Followers_InclusionCriteriaMet.txt
print('Filtering out followers w/ less than' + str(inclusion) + 'tweets in their timeline...')

TweetText = open(user + 'Tweets.txt', 'r')
FollowerInfo = open(user + 'Followers.txt', 'r')

TweetText_Cleaned = open(user + 'Tweets_InclusionCriteriaMet.txt', 'w')
FollowerInfo_Cleaned = open(user + 'Followers_InclusionCriteriaMet.txt', 'w')

# create array of UserID's that meet inclusion criteria (german language and 20+ tweets)
ids = []
for line in FollowerInfo:
    sections = line.split('\t')
    if len(sections) == 7:
        id = sections[0].strip()
        total_tweets = inf(sections[1])
        language = sections[2]
        if total_tweets >= inclusion and language == 'de':
            ids.append(id)

# close users file and re-open for another loop
FollowerInfo.close()
FollowerInfo = open(user + 'Followers.txt', 'r')

# write user info to cleaned file if they meet the inclusion criteria
for line in TweetText:
    sections = line.split('\t')
    if len(sections) == 7:
        folloewr = sections[0].strip()
        if follower in ids:
            FollowerInfo_Cleaned.write(line)

# write tweets to cleaned file if they come from a user who meets the inclusion criteria
for line in TweetText:
    sections = line.split('\t')
    if len(sections) > 1:
        follower = sections[0].strip()
        if follower in ids:
            TweetText_Cleaned.write(line)
TweetText.close()
FollowerInfo.close()
TweetText_Cleaned.close()
FollowerInfo_Cleaned.close()

# clean timelines for natural language processing
# file outputs: <user>Tweets_InclusionCriteriaMet_CLEANED.txt
print('Cleaning timelines for natural language processing...')

punct = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
fin = open(user + 'Tweets_InclusionCriteriaMet.txt', 'r')
fout = open(user + 'Tweets_InclusionCriteriaMet_CLEANED.txt','w', encoding='utf-8')

for line in fin:
 line = re.sub('(http://*[^\w\s]\S*)',"",line) # remove hyperlinks
 line = re.sub('([0-9])', "",line) # remove numbers
 line = re.sub('@\w+', "",line) # remove @username handles
 line = re.sub('(http\w+)', "",line) # remove hyperlinks
 line = re.sub('\n|\r|\t', "",line) # remove newline, carriage return, and tab characters
 line = line.lower()  # convert to lowercase
for p in punct:  # remove punctuation except apostrophe's
    line = line.replace(p, "")
line = line.strip()  # remove leading and trailing whitespace
line = re.sub('tco\w+', "", line) # remove picture links
fout.write(line + '\n')
fin.close()
fout.close()

print('Done!')

