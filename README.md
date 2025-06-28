
# 🏈 Super Bowl Ad Analysis: Rogue Ridge Campaign Support

This project supports the launch of Forge & Field’s new personal care line, **Rogue Ridge**, by analyzing 25 years of Super Bowl commercials. As a business analyst at Northlight Media, I used AI models and sentiment analytics to uncover what makes a Super Bowl ad succeed. The project combines technical depth with actionable strategy, guiding the creative direction of a $7–8 million ad investment.

---

## 📌 Project Objectives

- Collect and analyze viewer reactions from **YouTube**, **Reddit**, and **editorial rankings**
- Use AI tools (e.g., **Gemini API**) to summarize and assess ad sentiment
- Engineer features from multi-source text data
- Train interpretable ML models to identify success patterns
- Provide insights and guidance for a **30-second Super Bowl commercial**

---

## 🧱 Repository Structure

```
super-bowl-ad-analysis/
├── data/
│   ├── raw/                  ← Collected data from Gemini, Reddit, articles
│   ├── clean/                ← Merged and enriched data
│   └── final/                ← Ready-to-model datasets
├── notebooks/
│   ├── youtube_gemini_summarizer.ipynb
│   ├── reddit_scraper_praw.ipynb
│   ├── scrape_super_bowl_com.ipynb
│   ├── data_merge_and_feature_build.ipynb
│   ├── model_training_decision_tree.ipynb
│   └── model_training_random_forest.ipynb
├── scripts/                  ← Extraction and enrichment scripts (WIP)
├── models/                   ← Trained models (future enhancement)
├── docs/
│   ├── data_schema.md
│   └── deliverable_reports/ ← Final PDF/docx deliverables (tech + business)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Key Technologies

| Category          | Tool / Library             |
|------------------|----------------------------|
| Language          | Python                     |
| Development       | Google Colab               |
| APIs              | Gemini (YouTube), Reddit   |
| AI/ML             | scikit-learn, TextBlob     |
| Data Format       | CSV, JSON                  |
| Visualization     | matplotlib, seaborn        |
| Version Control   | GitHub                     |

---

## 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/winniewyl/super-bowl-ad-analysis.git
```

### 2. Open in Google Colab

- Open `notebooks/` and follow notebook order:
  1. `youtube_gemini_summarizer.ipynb`
  2. `reddit_scraper_praw.ipynb`
  3. `scrape_super_bowl_com.ipynb`
  4. `data_merge_and_feature_build.ipynb`
  5. `model_training_decision_tree.ipynb`
  6. `model_training_random_forest.ipynb`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Credentials

- Store Gemini and Reddit keys in a Colab cell or environment variables (do **not** hard-code).

---

## 🔬 AI Model Outputs

- **Decision Tree**: Simple rule-based insights (Reddit sentiment > 0.1 predicts success)
- **Random Forest**: Improved accuracy with cross-validation (~81%)
- **Top Feature**: Reddit sentiment polarity was the dominant predictor of ad success

---

## 📊 Sample Feature Importances (Random Forest)

| Feature              | Importance |
|----------------------|------------|
| avg_reddit_sentiment | 0.85       |
| avg_comment_score    | 0.12       |
| uses_celebrity       | 0.01       |
| uses_humor           | 0.01       |

---

## 📑 Final Deliverables

- ✅ **Deliverable 1**: Data strategy and tech stack
- ✅ **Deliverable 2**: AI model development and early insights
- ✅ **Deliverable 3**: Final technical report and client-facing business recommendations

---

## 📬 Contact

For questions or collaboration, contact: **wang6687@purdue.edu**

---

## ⚠️ Notes

- This repository is currently **private**. It contains educational content and API usage logs.
- Any proprietary datasets or credentials have been redacted for security.
- To make this public later, ensure `.env` and sensitive paths are excluded via `.gitignore`.
