# feature_engineering.py

import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    if not text or not isinstance(text, str):
        return 0.0
    return TextBlob(text).sentiment.polarity

def add_features(df):
    df["uses_celebrity"] = df["summary"].str.contains("celebrity", case=False, na=False).astype(int)
    df["uses_humor"] = df["summary"].str.contains("humor|funny|absurd|comedy", case=False, na=False).astype(int)
    df["avg_reddit_sentiment"] = df["comment_text"].apply(get_sentiment)
    return df
