# -*- coding: utf-8 -*-
import tweepy
import json
import requests

def postToSlack(text):
	payload = {
		"channel": "#general", 
		"username": "@fukutax on Twitter", 
		"icon_emoji": ":innocent:",
		"text": text
	}
	url = "https://hooks.slack.com/services/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"
	payloadJson = json.dumps(payload)
	requests.post(url, data=payloadJson)
	
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		postToSlack(status.text)

	def on_error(self, status_code):
		if status_code == 420:
			return False

def initialize():
	auth = tweepy.OAuthHandler("QpmoV4yKcgBGHa2CSV9qJVWCn", "cTfPA0wHa4jHhbE5iPgTJJbVlkTrF94dbii4KFiWwcabdgVhUY")
	auth.set_access_token("456660410-lp8FVaNtFOLstNAJeP7f4C0Q0N9Je2zWunU0Ey51", "y5FiyIumf00fbQlOBrbUEi0NRE7vjnabHPaSTEWjsArkN")
	api = tweepy.API(auth_handler=auth, api_root='/1.1')
	startStream(api.auth)

def startStream(auth):
	myStreamListener = MyStreamListener()
	myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
	#myStream.userstream()
	#myStream.filter(track=["#"])
	myStream.filter(follow=['6815212'])
	#fukutax=6815212
	#shopon1201=456660410
	
def main():
	initialize()

if __name__ == "__main__":
	main()