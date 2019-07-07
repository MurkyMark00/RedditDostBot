import re
from bs4 import BeautifulSoup
import requests


# Get Latest tweet id
def get_id() -> str:
    html = requests.get("https://twitter.com/DostKayaoglu").content

    soup = BeautifulSoup(html, 'html.parser')
    tweets = soup.find_all(
        "li", {"id": re.compile("^stream-item-tweet-[0-9]+$")})
    latest_tweet_id = 0

    for tweet in tweets:
        if "js-pinned" not in tweet["class"]:
            latest_tweet_id = tweet["id"][len("stream-item-tweet-"):]
            break

    return latest_tweet_id


# Get Latest tweet's title
def get_title(tweet_id: str) -> str:
    tweet_url = f"https://twitter.com/DostKayaoglu/status/{tweet_id}"

    html = requests.get(tweet_url).content
    soup = BeautifulSoup(html, 'html.parser')
    tweet_text = soup.find(
        "p", {"class": "TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text"})

    return tweet_text.text
