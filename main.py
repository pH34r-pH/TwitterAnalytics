# https://python-twitter.readthedocs.io/en/latest/getting_started.html
import twitter
from keys import keys

class TwitterAnalyzer:
    def __init__(self):
        key = keys()
        self.api = twitter.Api(consumer_key = key.consumer_key,
                    consumer_secret = key.consumer_secret,
                    access_token_key = key.access_token,
                    access_token_secret = key.access_token_secret)