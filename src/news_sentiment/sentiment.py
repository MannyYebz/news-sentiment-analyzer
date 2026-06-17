from textblob import TextBlob
import pandas as pd


def analyze_sentiment(text):
    """
    Takes a string and returns a sentiment score.

    TextBlob returns two values:
    - polarity: -1.0 (very negative) to +1.0 (very positive)
    - subjectivity: 0.0 (objective fact) to 1.0 (personal opinion)

    We use polarity as our main sentiment score.
    """
    if not text or pd.isna(text):
        return 0.0, 0.0

    blob = TextBlob(str(text))
    return blob.sentiment.polarity, blob.sentiment.subjectivity


def classify_sentiment(score):
    """
    Convert a polarity score into a human readable label.
    """
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"


def add_sentiment_scores(df):
    """
    Takes a DataFrame of articles and adds sentiment columns.
    Analyzes the title and description combined for better accuracy.
    """
    print("  Running sentiment analysis...")

    scores = []
    for _, row in df.iterrows():
        text = f"{row.get('title', '')} {row.get('description', '')}"
        polarity, subjectivity = analyze_sentiment(text)
        scores.append({
            "polarity": round(polarity, 4),
            "subjectivity": round(subjectivity, 4),
            "sentiment": classify_sentiment(polarity),
        })

    scores_df = pd.DataFrame(scores)
    df = pd.concat([df.reset_index(drop=True), scores_df], axis=1)

    print(f"  Analyzed {len(df)} headlines")
    print()

    return df


def print_sentiment_summary(df):
    """
    Print a clean summary of sentiment breakdown by category.
    """
    print("=" * 60)
    print("  SENTIMENT SUMMARY BY CATEGORY")
    print("=" * 60)

    header = f"  {'Category':<16} {'Positive':>9} {'Neutral':>9} {'Negative':>9} {'Avg Score':>10}"
    print(header)
    print("-" * 60)

    for category in df["category"].unique():
        cat_df = df[df["category"] == category]
        pos = len(cat_df[cat_df["sentiment"] == "Positive"])
        neu = len(cat_df[cat_df["sentiment"] == "Neutral"])
        neg = len(cat_df[cat_df["sentiment"] == "Negative"])
        avg = cat_df["polarity"].mean()

        print(f"  {category:<16} {pos:>9} {neu:>9} {neg:>9} {avg:>+10.3f}")

    print()
    overall = df["polarity"].mean()
    most_positive = df.loc[df["polarity"].idxmax(), "title"]
    most_negative = df.loc[df["polarity"].idxmin(), "title"]

    print(f"  Overall sentiment : {overall:+.3f}")
    print(f"  Most positive     : {most_positive[:70]}")
    print(f"  Most negative     : {most_negative[:70]}")
    print()


if __name__ == "__main__":
    from fetch_news import fetch_all_headlines
    df = fetch_all_headlines()
    df = add_sentiment_scores(df)
    print_sentiment_summary(df)