import parser
from pprint import pprint
from tweet_data_service import TweetDataService


username = 'elonmusk'

if __name__ == '__main__':
    pprint(parser.get_date_dictionary(parser.get_tweets(TweetDataService().get_user_timeline(username, 5))))

