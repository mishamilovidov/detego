import tweepy
import json
import xlsxwriter

from config import consumer_key, consumer_secret, access_token, access_token_secret
from nba_twitter_handles import nba_players

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True)

followers = {}
verified = {}
nba_followers = {}

# Get all the people the user follows
for player in nba_players:
    friends = api.friends_ids(player)
    for friend in friends:
        current_friend = api.get_user(friend)
        if current_friend.screen_name not in followers:
            followers[current_friend.screen_name] = current_friend.followers_count
            verified[current_friend.screen_name] = current_friend.verified
        if current_friend.screen_name not in nba_followers:
            nba_followers[current_friend.screen_name] = []
        nba_followers[current_friend.screen_name].append(player)
        print(len(followers))
        print(len(verified))
        print(len(nba_followers))

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 1

for key in followers.keys():
    row += 1
    worksheet.write(row, col, key)
    worksheet.write(row, col + 1, followers[key])
    worksheet.write(row, col + 2, verified[key])
    #worksheet.write(row, col + 3, nba_followers[key])
    worksheet.write(row, col + 3, len(nba_followers[key]))

workbook.close()