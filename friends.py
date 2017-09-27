import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

nbaplayers = ['KingJames','KyrieIrving']
followers = {}
verified = {}
nba_followers = {}

# Get all the people the user follows
for x in nbaplayers:
    friends = api.friends_ids(x)
    for y in friends:
        current_friend = api.get_user(y)
        if current_friend.screen_name not in followers:
            followers[current_friend.screen_name] = current_friend.followers_count
            verified[current_friend.screen_name] = current_friend.verified
        if current_friend.screen_name not in nba_followers:
            nba_followers[current_friend.screen_name] = []
        nba_followers[current_friend.screen_name].append(x)
        print(len(followers))
        print(len(verified))
        print(len(nba_followers))

# Print the results
print(followers)
print(verified)
print(nba_followers)
