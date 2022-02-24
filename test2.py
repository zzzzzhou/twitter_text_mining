import tweepy

bear_token = 'token'
client = tweepy.Client(bear_token)
tweets_fields_list = ['created_at', 'id', 'text']

# for response in tweepy.Paginator(client.search_recent_tweets, query="Trump", tweet_fields=tweets_fields_list,
#                                  max_results=10, limit=2):

for response in tweepy.Paginator(client.search_recent_tweets, query="Trump -is:retweet",
                                 tweet_fields=tweets_fields_list,
                                 max_results=10, limit=2):

    # print(response.includes)
    for tweet in response.data:
        print(tweet.id, tweet.created_at, tweet.text)

print('the type of tweet is', type(tweet))
