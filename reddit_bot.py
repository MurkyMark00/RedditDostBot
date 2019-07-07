import praw
import twitter_link
from os import path

directory_path = path.dirname(path.realpath(__file__))

tweet_id = twitter_link.get_id()
with open(f"{directory_path}/tweet_id.txt", "r") as f:
    # If it already posted the same id
    if f.readline() == tweet_id:
        with open("temp.txt", "a") as g:
            g.write("same\n")

    else:
        reddit = praw.Reddit("bot1")
        subreddit = reddit.subreddit("dostkayaoglu")

        subreddit.submit(
            twitter_link.get_title(tweet_id), url=f"https://twitter.com/DostKayaoglu/status/{tweet_id}").mod.distinguish(sticky=True)

        with open(f"{directory_path}/tweet_id.txt", "w") as f:
            f.write(tweet_id)
