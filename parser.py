from textblob import TextBlob


def get_tweets(statuses):
    tweets = []

    for status in statuses:
        tweets.append(dict(text=status.text,
                           created_at=status.created_at.strftime("%-m/%d/%Y")))
    return tweets


def get_date_dictionary(tweets):
    date_dictionary = dict()

    for tweet in tweets:
        tweet_date = tweet["created_at"]

        if tweet_date in date_dictionary.keys():
            date_dictionary[tweet_date] += ' ' + tweet["text"]
        else:
            date_dictionary[tweet_date] = tweet["text"]

    return date_dictionary


def get_mood_dictionary(date_dictionary):
    mood_dictionary = dict()

    for date in date_dictionary:
        mood_dictionary[date] = TextBlob(date_dictionary[date]).sentiment.polarity

    return mood_dictionary
