# reddit_scraper.py

import praw
import pandas as pd
from textblob import TextBlob

# Configure Reddit API (keys should be stored securely, e.g., via environment variables)
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='SuperBowlAdAnalysisBot',
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

def fetch_reddit_threads(search_term, limit=50):
    results = []
    for submission in reddit.subreddit("all").search(search_term, sort="top", limit=limit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            results.append({
                "search_term": search_term,
                "comment_text": comment.body,
                "comment_score": comment.score,
                "post_score": submission.score,
                "subreddit": submission.subreddit.display_name,
                "timestamp": comment.created_utc
            })
    return results

# Example run (replace with actual terms)
# terms = ["Budweiser Super Bowl 2023 ad", "Pepsi Super Bowl commercial"]
# data = []
# for term in terms:
#     data.extend(fetch_reddit_threads(term))

# df = pd.DataFrame(data)
# df.to_csv("reddit_superbowl_comments.csv", index=False)
