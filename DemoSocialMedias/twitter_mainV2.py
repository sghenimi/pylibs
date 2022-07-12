import tweepy
import requests
import pandas as pd

client = tweepy.Client( bearer_token='AAAAAAAAAAAAAAAAAAAAAKpTegEAAAAAjUvGzJXhX%2BabXYjahojQFxC%2FML0%3DvWfo4NjqG5yunKZbjwCPPtDRNpqPyarjXO4V9iZeXhj7JkEipv',
                        consumer_key='pMGSrx2uKSwvxDmmvYXkPdTkO',
                        consumer_secret='25L9KzLCm3SYmjXTbrncJUCzo1LhGaoDvzkx9RFmnAI2ZrS6w4',
                        access_token='48482795-PHv6y8vtKpTC7hiWJAp641nNJDdnyPDPs26e5Dmny',
                        access_token_secret='178BSrHs6UW9rVAPobJpFHNLS7KwQX3WhURHfN8Rwe6Zb',
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

# Define query
query = 'from:sghenimi -is:retweet'

# get max. 100 tweets
tweets = client.search_recent_tweets(query=query,
                                    tweet_fields=['author_id', 'created_at'],
                                     max_results=100)

# Save data as dictionary
tweets_dict = tweets.json()

# Extract "data" value from dictionary
tweets_data = tweets_dict['data']

# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data)

# save df
df.to_csv("tweets-obama.csv", index=False)
