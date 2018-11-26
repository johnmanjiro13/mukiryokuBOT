import os
import tweepy

def create_twitter_api():
    consumer_key = os.getenv("MUKIRYOKU_API_KEY")
    consumer_secret = os.getenv("MUKIRYOKU_API_SECRET")
    access_token = os.getenv("MUKIRYOKU_ACCESS_TOKEN")
    access_secret = os.getenv("MUKIRYOKU_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    api.update_status("なぁなぁ佐古さん。望遠鏡、使ってみてええ？ (榎町鈴乃/Normalize Human Communication)")
