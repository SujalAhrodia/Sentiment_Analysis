#Getting Data from Twitter Streaming API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret.
ckey='4EXZXXXXXXXXXXXXXSl'
csecret='uqaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0DxKUtJB2s'
atoken='354XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXL1kOrWl'
asecret='I5njXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX42OL'


class listener(StreamListener):

def on_data(self, data):
try:
#print(data)
tweet=data.split(',"text":"')[1].split('","source')[0]
print tweet

saveThis=str(tweet)
saveFile=open('happy.json','a')
saveFile.write(saveThis)
saveFile.write('\n')
saveFile.close()
return(True)
except BaseException, e:
print 'failed ondata,',str(e)
time.sleep(5)

def on_error(self, status):
print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["relationship","family","affection","friend","father","dad","mother","mom"])

#twitterStream.filter(track=["eid","christmas","diwali","new year","festival","celebration","holiday"])

#twitterStream.filter(track=["health","death","casualty","casualties","medical","treatment","medicine","medical facility"])
twitterStream.filter(locations=[72.503021,37.087769,80.345772,32.272221])
