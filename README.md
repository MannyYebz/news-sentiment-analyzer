# News Sentiment Analyzer

A data analysis pipeline that pulls live news headlines from the NewsAPI
and runs sentiment analysis on them using NLP. Breaks down sentiment
by category and surfaces insights about how positive or negative the
news is on any given day.

Built as part of a series of API projects to learn REST API integration,
NLP, and data analysis with Python.

---

## What It Does

- Fetches top headlines across 6 categories: business, technology,
  health, science, sports, and entertainment
- Runs sentiment analysis on every headline using TextBlob
- Scores each headline from -1.0 (very negative) to +1.0 (very positive)
- Classifies headlines as Positive, Neutral, or Negative
- Surfaces the most positive and most negative headline of the day
- Generates four analysis charts saved to `/charts`

---

## Charts Generated

- **Sentiment by Category** - Positive, neutral, and negative counts per category
- **Average Polarity** - Mean sentiment score per category
- **Overall Distribution** - Pie chart of sentiment breakdown across all headlines
- **Polarity Distribution** - Histogram of raw polarity scores

---

## Requirements

- Python 3.12+
- NewsAPI key (free tier works, 100 requests/day)
- [uv](https://docs.astral.sh/uv/) package manager

---

## Setup

**Step 1: Get an API key**

Go to [newsapi.org](https://newsapi.org), create a free account,
and copy your API key.

**Step 2: Clone the project**

```bash
git clone https://github.com/MannyYebz/news-sentiment-analyzer.git
cd news-sentiment-analyzer
```

**Step 3: Install dependencies**

```bash
uv sync
```

**Step 4: Add your API key**

Create a `.env` file in the project root: