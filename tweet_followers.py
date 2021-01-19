# This is a sample Python script.
import tweepy
import json
from tweepy import OAuthHandler

consumer_key = 'I2oo9CeNPr2qhIzGaMvZaIE7W'
consumer_secret = 'avSLkPnMkvLGxJ0qWocCCncHtFRcjQcOsihBoUvCSr2eUFrfIY'
access_token = '1164473914161950720-x3hyaHFOTQO6HLHJv5OvkAbLW08yAo'
access_secret = 'F3akRpISv8GBK4jlFjWKdkI7aSPNnQVFwiOL45iTKVBiH'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#we can read our own timeline (i.e. our Twitter homepage) with:
"""for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)"""

#print tweet,followers..
def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


