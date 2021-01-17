def get_tweets(statuses):
    tweets = []

    for status in statuses:
        tweets.append(dict(text=status.text,
                           created_at=status.created_at.strftime("%m/%d/%Y, %H:%M:%S")))
    return tweets
