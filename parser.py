from bs4 import BeautifulSoup


def get_tweet_text(statuses):

    for status in statuses:
        print(status.text)
        print(status.created_at)
