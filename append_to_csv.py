import csv
import json
import dateutil.parser


def append_to_csv(json_response, fileName):
    # this code is adapted from Towardsdatascience blog:
    # https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic
    # -research-using-python-3-518fcb71df2a

    # A counter variable
    counter = 0

    # Open OR create the target CSV file
    csvFile = open(fileName, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    # Loop through each tweet
    for tweet in json_response['data']:
        # We will create a variable for each since some of the keys might not exist for some tweets You can change
        # the variables based on what you want. Check the available variable from here:
        # https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet

        # 1. Author ID
        author_id = tweet['author_id']

        # 2. Time created
        #created_at = dateutil.parser.parse(tweet['created_at'])

        # 4. Tweet ID
        tweet_id = tweet['id']

        # 5. Conversation ID
        conversation_id = tweet['conversation_id']

        # 6. Tweet metrics
        retweet_count = tweet['public_metrics']['retweet_count']
        reply_count = tweet['public_metrics']['reply_count']
        like_count = tweet['public_metrics']['like_count']
        quote_count = tweet['public_metrics']['quote_count']

        # 7. source
        source = tweet['source']

        # 8. Tweet text
        text = json.dumps(tweet['text'])

        # Assemble all data in a list
        res = [author_id, tweet_id, conversation_id, like_count, quote_count, reply_count, retweet_count,
               source, text]

        # Append the result to the CSV file
        csvWriter.writerow(res)
        counter += 1

    # When done, close the CSV file
    csvFile.close()

    # Print the number of tweets for this iteration
    print("# of Tweets added from this response: ", counter)
