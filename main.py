import parser
from pprint import pprint
from tweet_data_service import TweetDataService
import eel

total_pages = 8
username = 'elonmusk'


def get_date_dictionary():
    user_timeline = TweetDataService().get_user_timeline(username, total_pages)
    user_tweets = parser.get_tweets(user_timeline)
    return parser.get_date_dictionary(user_tweets)


@eel.expose
def get_mood_dictionary():
    return parser.get_mood_dictionary(get_date_dictionary())


if __name__ == '__main__':
    eel.init('static_web')
    eel.start('main.html')


