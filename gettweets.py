import tweepy
import csv

auth = tweepy.OAuthHandler("",
                           "")
auth.set_access_token("",
                      "")

# set wait_on_rate_limit = True to wait automatically, code will wait 15 minutes if limit is hit
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True, retry_count=5, retry_delay=5)

# set number of pages, get a list of followers
users = tweepy.Cursor(api.followers, screen_name="spdde").items(5000)


def get_tweets(ids, party):
    """

    :param ids: user ids
    :param party: party (screen_name) whose follower you are interested in
    :return: outputs a csv with up to 200 tweets of the followers of the selected party
    """
    # initialize a list to hold all Tweets
    alltweets = []

    # make request for most recent tweets (200 is the maximum allowed count)
    try:
        new_tweets = api.user_timeline(id=ids, count=200)
        if len(new_tweets) > 19:
            print(ids, "length of tweet", len(new_tweets))
            alltweets.extend(new_tweets)
    except tweepy.TweepError:
        print("Failed to run the command on that user ", ids, " , Skipping...")

    # can adjust which information is required and add filters like only German tweets
    outtweets = [[ids,
                  tweet.created_at,
                  tweet.lang,
                  tweet.retweeted,
                  #tweet.source.encode("utf-8"),
                  tweet.text.encode("utf-8"), ] for tweet in alltweets if tweet.lang == "de"]

    # write the csv
    with open('%s_tweets.csv' % party, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
    pass


if __name__ == '__main__':

    party = "bla"
    with open('%s_tweets.csv' % party, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id",
                         "created_at",
                         "language",
                         "retweeted",
                         #"source",
                         "text"])
    # n is a counter
    n = 0
    for user in users:
        n += 1
        get_tweets(user.id, party)
        print(n)



