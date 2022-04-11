import requests
import os
import json
import append_to_csv as apc
import time
import pandas as pd

# To set your environment variables in your terminal run the following line:
os.environ['BEARER_TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAGPBWgEAAAAAedocddgJGmU%2FY5VlTRIPQSkME6M' \
                             '%3DV05hdBJfmWVwWWZxSEXFqrSCbRcnLwSAf57vpz337OYgxXKKEx '
bearer_token = os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/recent"

io = r'D:\ebm\dissertation\twitter api project\cosmetics.csv'
brands = pd.read_csv(io)

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# json_response = connect_to_endpoint(search_url, query_params)
# print(json.dumps(json_response, indent=4, sort_keys=True))
for each in brands['keyword']:
    keyword = '"'+each+'"'
    # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
    # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
    query = keyword + ' lang:en -is:retweet -has:links'
    max_result = 100
    next_token = None
    query_params = {'query': query,
                    'tweet.fields': 'author_id,public_metrics,conversation_id,source',
                    'max_results': max_result,
                    'next_token': next_token}

    count = 0  # Counting tweets per time period
    #max_count = 30  # Max tweets per time period
    flag = True
    total_tweets = 0
    # Check if flag is true
    while flag:
        # Check if max_count reached
        # if count >= max_count:
        # break
        print("-------------------")
        print("Token: ", next_token)
        json_response = connect_to_endpoint(search_url, query_params)
        result_count = json_response['meta']['result_count']

        if 'next_token' in json_response['meta']:
            # Save the token to use for next call
            query_params['next_token'] = json_response['meta']['next_token']  #
            # 赋值只是传入一个地址，如果传的是字符，数字等变量，则是指向一个地址，当变量被重新赋值，是变量的地址变了，而字典指向的地址并没有改变；如果初始化是list或者字典，则是可变的，从外部修改list会同步影响字典中的值
            next_token = json_response['meta']['next_token']
            print("Next Token: ", next_token)
            if result_count is not None and result_count > 0 and next_token is not None:
                # print("Start Date: ", start_list[i])
                apc.append_to_csv(json_response, keyword.strip('"') + '.csv')  # you need to define the file name here
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(5)
                # If no next token exists
        else:
            if result_count is not None and result_count > 0:
                print("-------------------", "no next token")
                apc.append_to_csv(json_response, keyword.strip('"') + ".csv")  # you need to define the file name here
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(5)

            # Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        time.sleep(5)
    print("Total number of results: ", total_tweets)


