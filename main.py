import parser
from pprint import pprint
from tweet_data_service import TweetDataService


username = 'elonmusk'

if __name__ == '__main__':
    total_pages = 5
    user_timeline = TweetDataService().get_user_timeline(username, total_pages)
    user_tweets = parser.get_tweets(user_timeline)
    pprint(parser.get_date_dictionary(user_tweets))

