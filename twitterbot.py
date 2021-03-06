import tweepy
from selenium import webdriver
import time

path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(path)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_tweet_id(username):
    tweets = api.user_timeline(username, count=1)
    id_list = []
    tweets_id = [tweet.id for tweet in tweets]
    for t in tweets_id:
        id_list.append(t)
    return id_list
    
try:
    user = api.get_user(userID)
    name = user.screen_name
    tweet_id = get_tweet_id(name)[0]
    url = "https://twitter.com/"+str(name)+"/status/"+str(tweet_id)
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)
    for tweet in api.user_timeline(screen_name=userID):
    	print(tweet.text)
except tweepy.TweepError:
    print("An error occurred")
    