import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
consumer_key = 'I2oo9CeNPr2qhIzGaMvZaIE7W'
consumer_secret = 'avSLkPnMkvLGxJ0qWocCCncHtFRcjQcOsihBoUvCSr2eUFrfIY'
access_token = '1164473914161950720-x3hyaHFOTQO6HLHJv5OvkAbLW08yAo'
access_secret = 'F3akRpISv8GBK4jlFjWKdkI7aSPNnQVFwiOL45iTKVBiH'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])