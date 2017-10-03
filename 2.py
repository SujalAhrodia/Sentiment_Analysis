#Download tweets for specific locations using geolocation api
import tweepy
import json


def fnc():

ckey='4EXZXXXXXXXXXXXXXSl'
csecret='uqaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0DxKUtJB2s'
atoken='354XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXL1kOrWl'
asecret='I5njXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX42OL'


text_file = open("assam.txt", "a")

auth = tweepy.OAuthHandler(ckey, csecret)
auth.secure = True
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
places = api.geo_search(query="assam", granularity="city")
place_id = places[0].id

data = []

tweets = api.search(q="place:%s" % place_id)
for tweet in tweets:
title = tweet.text
data.append(title)
print tweet.text + " \n\n " + tweet.place.name if tweet.place else "Undefined place"

with open('assam.json', 'a') as outfile:
json.dump(data, outfile)
