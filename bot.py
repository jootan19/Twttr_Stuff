# from tweepy import OAuthHandler
import tweepy as tp
from cred import *


def setTwitterAuth():
    """
    obtains authorization from twitter API
    """
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tp.API(auth)
    return api


def tweet(api, msg):
    api.update_status(msg)


def searchTweet(api, searchTerm):
    """
    gets search results of the string, search, and returns them as a list
    of tweet objects
    """
    searchResults = [status for status in tp.Cursor(api.search, q=searchTerm).items(5)]
    return searchResults

api = setTwitterAuth()
# tweet(api, 'Hello')
# user = api.me()

query = searchTweet(api, 'fMRI and Consciousness')

for tweet in query:
    print tweet.text
    print tweet.user.screen_name

