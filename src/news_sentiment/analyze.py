import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs("charts", exist_ok=True)

plt.rcParams.update({
    "figure.facecolor": "#0d0d0d",
    "axes.facecolor": "#0d0d0d",
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#cccccc",
    "xtick.color": "#888888",
    "ytick.color": "#888888",
    "text.color": "#cccccc",
    "grid.color": "#1a1a1a",
    "grid.linestyle": "--",
    "font.family": "monospace",
})

ACCENT = "#ffffff"
POSITIVE_COLOR = "#1DB954"
NEGATIVE_COLOR = "#FF6B6B"
NEUTRAL_COLOR = "#888888"
FIG_SIZE = (10, 5)


def plot_sentiment_by_category(df):
    categories = df["category"].unique()
    pos_counts = []
    neu_counts = []
    neg_counts = []

    for cat in categories:
        cat_df = df[df["category"] == cat]
        pos_counts.append(len(cat_df[cat_df["sentiment"] == "Positive"]))
        neu_counts.append(len(cat_df[cat_df["sentiment"] == "Neutral"]))
        neg_counts.append(len(cat_df[cat_df["sentiment"] == "Negative"]))

    x = np.arange(len(categories))
    width = 0.25

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor("#0d0d0d")

    ax.bar(x - width, pos_counts, width, label="Positive",
           color=POSITIVE_COLOR, edgecolor="none", alpha=0.85)
    ax.bar(x, neu_counts, width, label="Neutral",
           color=NEUTRAL_COLOR, edgecolor="none", alpha=0.85)
    ax.bar(x + width, neg_counts, width, label="Negative",
           color=NEGATIVE_COLOR, edgecolor="none", alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels([c.title() for c in categories], fontsize=10)
    ax.set_ylabel("Number of Articles", fontsize=10)
    ax.set_title("Sentiment Distribution by Category",
                 fontsize=14, fontweight="bold", color=ACCENT, pad=15)
    ax.legend(fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)

    plt.tight_layout()
    plt.savefig("charts/sentiment_by_category.png", dpi=150,
                bbox_inches="tight", facecolor="#0d0d0d")
    print("  Saved: charts/sentiment_by_category.png")
    plt.show()


def plot_avg_polarity(df):
    avg_polarity = df.groupby("category")["polarity"].mean().sort_values()

    colors = [POSITIVE_COLOR if v > 0 else NEGATIVE_COLOR
              for v in avg_polarity.values]

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor("#0d0d0d")

    bars = ax.barh(
        [c.title() for c in avg_polarity.index],
        avg_polarity.values,
        color=colors,
        edgecolor="none",
        height=0.5,
        alpha=0.85,
    )

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.002 if width >= 0 else width - 0.002,
            bar.get_y() + bar.get_height() / 2,
            f"{width:+.3f}",
            va="center",
            ha="left" if width >= 0 else "right",
            fontsize=9, color="#888888",
        )

    ax.axvline(0, color="#444444", linewidth=1)
    ax.set_xlabel("Average Polarity Score", fontsize=10)
    ax.set_title("Average Sentiment Score by Category",
                 fontsize=14, fontweight="bold", color=ACCENT, pad=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_axisbelow(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig("charts/avg_polarity.png", dpi=150,
                bbox_inches="tight", facecolor="#0d0d0d")
    print("  Saved: charts/avg_polarity.png")
    plt.show()


def plot_sentiment_pie(df):
    sentiment_counts = df["sentiment"].value_counts()

    colors = {
        "Positive": POSITIVE_COLOR,
        "Neutral": NEUTRAL_COLOR,
        "Negative": NEGATIVE_COLOR,
    }
    pie_colors = [colors[s] for s in sentiment_counts.index]

    fig, ax = plt.subplots(figsize=(7, 5))
    fig.patch.set_facecolor("#0d0d0d")

    wedges, texts, autotexts = ax.pie(
        sentiment_counts.values,
        labels=sentiment_counts.index,
        autopct="%1.1f%%",
        colors=pie_colors,
        startangle=90,
        pctdistance=0.82,
    )

    for text in texts:
        text.set_fontsize(11)
        text.set_color("#cccccc")
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    ax.set_title("Overall Sentiment Distribution",
                 fontsize=14, fontweight="bold", color=ACCENT, pad=20)

    plt.tight_layout()
    plt.savefig("charts/sentiment_pie.png", dpi=150,
                bbox_inches="tight", facecolor="#0d0d0d")
    print("  Saved: charts/sentiment_pie.png")
    plt.show()


def plot_polarity_distribution(df):
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor("#0d0d0d")

    ax.hist(df["polarity"], bins=20, color="#4ECDC4",
            edgecolor="none", alpha=0.85)
    ax.axvline(df["polarity"].mean(), color="#FFE66D",
               linestyle="--", linewidth=1.5,
               label=f"Mean: {df['polarity'].mean():+.3f}")
    ax.axvline(0, color="#444444", linewidth=1, label="Neutral (0)")

    ax.set_xlabel("Polarity Score", fontsize=10)
    ax.set_ylabel("Number of Headlines", fontsize=10)
    ax.set_title("Polarity Score Distribution",
                 fontsize=14, fontweight="bold", color=ACCENT, pad=15)
    ax.legend(fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)

    plt.tight_layout()
    plt.savefig("charts/polarity_distribution.png", dpi=150,
                bbox_inches="tight", facecolor="#0d0d0d")
    print("  Saved: charts/polarity_distribution.png")
    plt.show()


if __name__ == "__main__":
    from fetch_news import fetch_all_headlines
    from sentiment import add_sentiment_scores, print_sentiment_summary

    print()
    print("  NEWS SENTIMENT ANALYSIS")
    print("  ========================")
    print()

    df = fetch_all_headlines()
    df = add_sentiment_scores(df)
    print_sentiment_summary(df)

    print("  Generating charts...")
    print()

    plot_sentiment_by_category(df)
    plot_avg_polarity(df)
    plot_sentiment_pie(df)
    plot_polarity_distribution(df)

    print()
    print("  Done. Charts saved to /charts")
    