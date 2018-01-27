import tweepy
from secrets import *
import time
from random import randint


# Deal with authentication for tweepy and twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)  # create an API object


while True:
    tweets = []

    # Get all tweets that arent retweets
    for tweet in tweepy.Cursor(api.user_timeline).items(200):
        if not tweet.retweeted:
            tweets.append(tweet)

    # generate random number
    tweetLength = len(tweets)
    tweetIndx = randint(0, tweetLength)

    # update Status
    api.update_status(tweets[tweetIndx])

    # sleep for three hours
    time.sleep(3600 * 3)
