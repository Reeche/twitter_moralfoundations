import os
import json
import pandas as pd
import re
import tweepy
import csv
import asyncio
import timeit


auth = tweepy.OAuthHandler("1LkXJ9SqzQm7an39boqQ5AW0v",
                           "eEDlvPcEEfJPKVR1HkIYCmR0BcsISQWXhzjudaNHvMYj3cGgh7")
auth.set_access_token("911681697577611264-lQDqG7lcZGjvL1vIvrR3qKTlaPZH3Xp",
                      "AZqWtegYKM7GrsN0AVmwaqMHQH72R85lzaEwQvpflam8x")

# set wait_on_rate_limit = True to wait automatically
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True, retry_count=10, retry_delay = 5)

# set number of pages
users = [api.get_user("CDU", page = x) for x in range(51, 101)]


follower = []
names = []
for user in users:
    print("get users")
    for friend in user.followers():
        #print("friend.id")
        follower.append(friend.id)
        names.append(friend.name)


#
# print(api.user_timeline(911681697577611264))
#
# file = open("testfile.json", "w")
# temp = []
# for id in follower:
#     try:
#         # print("start printing id", id)
#         # print(api.user_timeline(id))
#         temp.append(api.user_timeline(id))
#     except:
#         print("error")
# print(temp)
# print(type(temp))
# file.write(temp)
# file.close()


async def get_tweets(ids, party):
    await asyncio.sleep(1)
    print(ids)
    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make request for most recent tweets (200 is the maximum allowed count)
    try:
        new_tweets = api.user_timeline(id=ids, count=200)
        if len(new_tweets) > 19:
            print("length of tweet", len(new_tweets))
            alltweets.extend(new_tweets)
    except tweepy.TweepError:
        print("Failed to run the command on that user ", ids, " , Skipping...")

    # transform the tweepy tweets into a 2D array that will populate the csv	| you can comment out data you don't need
    outtweets = [[ids,
                #tweet.id_str,
                  tweet.created_at,
                  tweet.lang,
                  #tweet.favorite_count,
                  #tweet.retweet_count,
                  tweet.retweeted,
                  #tweet.source.encode("utf-8"),
                  tweet.text.encode("utf-8"), ] for tweet in alltweets if tweet.lang == "de"]

    # write the csv
    with open('%s_tweets.csv' % party, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
    pass
    #return outtweets


if __name__ == '__main__':

    party = "CDU2"
    with open('%s_tweets.csv' % party, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id",
                         "created_at",
                         "language",
                         #"favorites",
                         #"retweets",
                         "retweeted",
                         #"source",
                         "text"])

    loop = asyncio.get_event_loop()
    for ids in follower:
        loop.run_until_complete(get_tweets(ids, party))

    loop.close()


