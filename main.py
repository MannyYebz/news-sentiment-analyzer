from src.news_sentiment.fetch_news import fetch_all_headlines
from src.news_sentiment.sentiment import add_sentiment_scores, print_sentiment_summary
from src.news_sentiment.analyze import (
    plot_sentiment_by_category,
    plot_avg_polarity,
    plot_sentiment_pie,
    plot_polarity_distribution,
)


def main():
    print()
    print("  NEWS SENTIMENT ANALYZER")
    print("  ========================")

    # Step 1: Fetch headlines
    df = fetch_all_headlines()

    # Step 2: Run sentiment analysis
    df = add_sentiment_scores(df)
    print_sentiment_summary(df)

    # Step 3: Generate charts
    print("  Generating charts...")
    print()

    plot_sentiment_by_category(df)
    plot_avg_polarity(df)
    plot_sentiment_pie(df)
    plot_polarity_distribution(df)

    print()
    print("  Done. Charts saved to /charts")


if __name__ == "__main__":
    main()