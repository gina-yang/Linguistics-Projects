import tweepy
from secrets import *

# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Construct the API instance
api = tweepy.API(auth)  # Creates an API object to provide access to all
                        # twitter RESTful API methods

