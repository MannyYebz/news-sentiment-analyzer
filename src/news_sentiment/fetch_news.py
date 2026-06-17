import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")
BASE_URL = "https://newsapi.org/v2"

CATEGORIES = [
    "business",
    "technology",
    "health",
    "science",
    "sports",
    "entertainment",
]


def get_top_headlines(category, country="us", page_size=20):
    url = f"{BASE_URL}/top-headlines"
    params = {
        "category": category,
        "country": country,
        "pageSize": page_size,
        "apiKey": API_KEY,
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"  Error fetching {category}: {response.json().get('message')}")
        return []

    data = response.json()
    articles = []

    for article in data.get("articles", []):
        articles.append({
            "category": category,
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "source": article.get("source", {}).get("name", "Unknown"),
            "published_at": article.get("publishedAt", ""),
            "url": article.get("url", ""),
        })

    return articles


def fetch_all_headlines():
    print()
    print("=" * 55)
    print("  FETCHING NEWS HEADLINES")
    print("=" * 55)

    all_articles = []

    for category in CATEGORIES:
        articles = get_top_headlines(category)
        all_articles.extend(articles)
        print(f"  {category:<15} {len(articles)} articles")

    df = pd.DataFrame(all_articles)
    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

    print()
    print(f"  Total articles loaded: {len(df)}")
    print()

    return df


if __name__ == "__main__":
    df = fetch_all_headlines()
    print(df[["category", "title", "source"]].head(10).to_string(index=False))

