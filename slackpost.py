# -*- coding: utf-8 -*-
import tweepy
import json
import requests

def postToSlack(text):
	payload = {
		"channel": "#channel", 
		"username": "usename", 
		"icon_emoji": ":innocent:",
		"text": text
	}
	url = "Webhook URL by Incoming WebHooks"
	payloadJson = json.dumps(payload)
	requests.post(url, data=payloadJson)
	
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		postToSlack(status.text)

	def on_error(self, status_code):
		if status_code == 420:
			return False

def initialize():
	#your consumer_key,consumer_secret,access_token,access_token_secret
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth_handler=auth, api_root='/1.1')
	startStream(api.auth)

def startStream(auth):
	myStreamListener = MyStreamListener()
	myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
	myStream.filter(follow=['456660410'])
	#456660410 is UserID of shopon1201
	
def main():
	initialize()

if __name__ == "__main__":
	main()