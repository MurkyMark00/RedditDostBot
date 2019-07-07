import praw
import twitter_link


tweet_id = twitter_link.get_id()
with open("tweet_id.txt", "r") as f:
    # If it already posted the same id
    if f.readline() == tweet_id:
        with open("temp.txt", "a") as g:
            g.write("same\n")

    else:
        reddit = praw.Reddit("bot1")
        subreddit = reddit.subreddit("dostkayaoglu")

        subreddit.submit(
            twitter_link.get_title(tweet_id), url=f"https://twitter.com/DostKayaoglu/status/{tweet_id}").mod.distinguish(sticky=True)

        with open("tweet_id.txt", "w") as f:
            f.write(tweet_id)
