# -*- coding: utf-8 -*-
"""
@author: David Jose Cotilla Martin
"""

import tweepy
from textblob import TextBlob

consumer_key = 'HxTwHU4NS9ozBy5umXh5Y0VYv'
consumer_secret = 'gnlrkkoYNUNZT2B2sshoVIvfkjvRRosI7DWcLNlZ89Ubwrkqbt'

access_token = '741468980-hirgAI1iuJr8RyLlWS4zX86YsFVTsvnH84cNw4ND'
access_token_secret = 'FcUyRls8TBRQkloHTiWMqxzt1kboBnKXe7zDA8KEIZIjJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

i = 0

while i <= 10:
    
    public_tweets = api.search('Suicide')
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
    i = i+1

