import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Get all the people the user follows
friends = api.friends_ids("KingJames")

# Print out each one
for id in friends:
    print(api.get_user(id))
