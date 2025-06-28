
# 📊 Data Schema: Super Bowl Ad Analysis

This document describes the key datasets and features used in the project across raw, clean, and enriched formats.

---

## 📁 File: `video_summaries_sentiment.csv`
**Location:** `data/raw/youtube_gemini/`

**Source:** YouTube + Gemini API

| Column Name       | Type   | Description                                      |
|-------------------|--------|--------------------------------------------------|
| source_url        | string | YouTube video link                               |
| brand             | string | Brand or advertiser (e.g., Pepsi, Budweiser)     |
| year              | int    | Super Bowl year                                  |
| summary           | text   | Gemini-generated ad summary                      |
| sentiment         | string | 2–3 adjectives summarizing tone                  |

---

## 📁 File: `reddit_superbowl_comments.csv`
**Location:** `data/raw/reddit_threads/`

**Source:** Reddit (via PRAW)

| Column Name       | Type   | Description                                      |
|-------------------|--------|--------------------------------------------------|
| search_term       | string | Keyword used to find Reddit posts                |
| comment_text      | text   | Body of the Reddit comment                       |
| comment_score     | int    | Upvotes/downvotes score of comment               |
| post_score        | int    | Score of the parent Reddit post                  |
| subreddit         | string | Subreddit where the post was found               |
| timestamp         | datetime | Date/time comment was posted                   |

---

## 📁 File: `merged_ad_data_enriched.csv`
**Location:** `data/clean/`

**Source:** Merged YouTube + Reddit + Feature Engineering

| Column Name           | Type     | Description                                                 |
|-----------------------|----------|-------------------------------------------------------------|
| source_url            | string   | YouTube video link                                          |
| brand                 | string   | Brand or advertiser                                         |
| year                  | int      | Year of ad                                                  |
| summary               | text     | Gemini summary                                              |
| sentiment             | string   | Original adjectives                                         |
| search_term           | string   | Combined term used to find matching Reddit posts            |
| avg_comment_score     | float    | Mean Reddit comment score for this ad                       |
| avg_post_score        | float    | Mean score of Reddit posts                                  |
| avg_reddit_sentiment  | float    | Polarity score from TextBlob                                |
| uses_celebrity        | binary   | 1 = mentions celebrity, 0 = no mention                      |
| uses_humor            | binary   | 1 = mentions humor-related words, 0 = no humor              |
| editorial_rank        | int/null | Placeholder for article rankings (if available)             |
| success               | binary   | 1 = high sentiment (> 0.1), 0 = not successful               |

---

## 📌 Notes

- Missing values in `avg_reddit_sentiment` may indicate no Reddit match.
- `success` is a derived label used for ML classification tasks.
- `editorial_rank` is manually populated or future-scraped from NexisUni/Ad Meter.

