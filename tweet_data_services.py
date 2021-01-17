import os
import tweepy
from dotenv import load_dotenv


def get_tweepy_api():
    load_dotenv()
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    api_token = os.getenv('TWITTER_ACCESS_TOKEN')
    api_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(api_token, api_token_secret)

    return tweepy.API(auth)


def get_user_timeline(screen_name, page_count=1):
    api = get_tweepy_api()
    tweets = []
    return tweepy.Cursor(api.user_timeline,
                                screen_name=screen_name,
                                trim_user=True,
                                exclude_replies=True,
                                include_rts=False).items(page_count)



