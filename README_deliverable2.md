# README – Deliverable 2

## 🏈 Super Bowl Ad Analysis: Rogue Ridge Campaign Support

This project supports the launch of **Forge & Field’s new personal care line, Rogue Ridge**, through an evidence-based analysis of past Super Bowl commercials.  
As a business analyst at Northlight Media, I analyze 25 years of ad performance to identify key success factors using **sentiment analysis**, **machine learning**, and **public engagement data**.

---

## 📌 Project Objectives

- Collect and analyze viewer reactions from **YouTube**, **Reddit**, and **editorial rankings**
- Use AI tools (like **Gemini API**) to summarize **sentiment and themes**
- Train models to uncover patterns behind successful ads
- Provide insights and **design guidance** for a 30-second Super Bowl commercial

---

## 📁 Folder Structure

```
super-bowl-ad-analysis/
├── data/
│   ├── raw/
│   │   ├── youtube_gemini/
│   │   ├── reddit_threads/
│   │   └── articles_rankings/
│   ├── clean/
│   └── final/
├── notebooks/
│   ├── youtube_gemini_summarizer.ipynb
│   ├── reddit_scraper_praw.ipynb
│   ├── article_extractor.ipynb
│   └── model_training.ipynb
├── scripts/
├── models/
├── docs/
│   └── data_schema.md
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🔧 Key Technologies

| Category         | Tool / Library           |
|------------------|--------------------------|
| Language         | Python                   |
| Development      | Google Colab, VSCode     |
| APIs             | Gemini (YouTube), Reddit |
| Data Formats     | JSON, CSV                |
| Modeling         | scikit-learn             |
| Visualization    | matplotlib, seaborn      |
| Version Control  | GitHub                   |

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/winniewyl/super-bowl-ad-analysis.git
```

Open notebooks in Google Colab or VSCode.

Install required dependencies:

```bash
pip install -r requirements.txt
```

Add your Gemini API key in the `.env` file or directly into the notebook/script.

---

## 📊 Sample Gemini API Workflow

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-pro")

video_url = "https://www.youtube.com/watch?v=EXAMPLE"
prompt = f"Summarize the viewer sentiment and themes from comments on this ad: {video_url}"
response = model.generate_content(prompt)

print(response.text)
```

---

## 🧠 Outputs

- Labeled dataset of ad features (sentiment, tags, upvotes, themes)
- Trained ML model predicting ad impact
- Visualizations for key trends
- Final technical and client-facing reports

---

## ✅ Status

- ✅ Deliverable 1 complete (Data strategy, tech stack, initial data collection)
- ✅ Deliverable 2 complete (Model training, exploratory analysis)

---

## 📬 Contact

For questions or feedback, please email: **wang6687@purdue.edu**
