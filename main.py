import tweet_data_services
import parser
from pprint import pprint


username = 'elonmusk'

if __name__ == '__main__':
    pprint(tweet_data_services.get_user_timeline(username, 5))

