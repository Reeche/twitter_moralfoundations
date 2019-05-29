import tweepy
import csv

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
auth = tweepy.OAuthHandler("",
                           "")
auth.set_access_token("-",
                      "")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True, retry_count=5, retry_delay=5)

# Function to extract tweets
def get_tweets(username):

    # initialize a list to hold all Tweets
    alltweets = []
    try:
        new_tweets = api.user_timeline(screen_name=username, count = 20)
        if len(new_tweets) > 19:
            alltweets.extend(new_tweets)
    except tweepy.TweepError:
        print("Failed to run the command on that user ", username, " , Skipping...")

    # can adjust which information is required and add filters like only German tweets
    outtweets = [[username,
                  tweet.text.encode("utf-8"), ] for tweet in alltweets if tweet.lang == "de"]
        # Printing the tweets
    print(outtweets)
    with open('all_tweets.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
    pass


# Driver code
if __name__ == '__main__':
    # here add the list of users you want to extract
    users = ["spdde", "cdu", "fdp"]
    with open('all_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["party",
                         "text"])
    # whose tweets are to be extracted.
    for user in users:
        get_tweets(user)