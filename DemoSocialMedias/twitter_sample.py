import requests
import os
import json
import pandas as pd

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
#bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token ='AAAAAAAAAAAAAAAAAAAAAKpTegEAAAAAjUvGzJXhX%2BabXYjahojQFxC%2FML0%3DvWfo4NjqG5yunKZbjwCPPtDRNpqPyarjXO4V9iZeXhj7JkEipv'

recent_search_url = "https://api.twitter.com/2/tweets/search/recent"
full_search_url = "https://api.twitter.com/2/tweets/search/all"

twitter_account = 'elonmusk'
query_params = {'query': f'(from:{twitter_account})',
                'start_time':   '2022-07-05T00:00:00.000Z',
                'max_results': 11,
                #'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                #'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                }


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


def main():
    json_response = connect_to_endpoint(recent_search_url, query_params)
    tweets_data = json_response['data']
    df = pd.json_normalize(tweets_data)
    #df.to_csv("tweets-moi.csv")
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()