import tweepy
import csv



auth = tweepy.OAuthHandler("1LkXJ9SqzQm7an39boqQ5AW0v",
                           "eEDlvPcEEfJPKVR1HkIYCmR0BcsISQWXhzjudaNHvMYj3cGgh7")
auth.set_access_token("911681697577611264-lQDqG7lcZGjvL1vIvrR3qKTlaPZH3Xp",
                      "AZqWtegYKM7GrsN0AVmwaqMHQH72R85lzaEwQvpflam8x")

# set wait_on_rate_limit = True to wait automatically
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True, retry_count=5, retry_delay=5)

# set number of pages, get a list of followers
users = tweepy.Cursor(api.followers, screen_name="spdde").items(5000)


def get_tweets(ids, party):
    #print(ids)
    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make request for most recent tweets (200 is the maximum allowed count)
    try:
        new_tweets = api.user_timeline(id=ids, count=200)
        if len(new_tweets) > 19:
            print(ids, "length of tweet", len(new_tweets))
            alltweets.extend(new_tweets)
    except tweepy.TweepError:
        print("Failed to run the command on that user ", ids, " , Skipping...")

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

    party = "bla"
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
    n = 0
    for user in users:
        n += 1
        get_tweets(user.id, party)
        print(n)



