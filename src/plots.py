"""Visualization helpers for EDA and reporting."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_histogram(series, title: str = "Distribution"):
    """Create a simple histogram for a pandas Series."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(series, ax=ax)
    ax.set_title(title)
    return fig, ax


def plot_correlation_heatmap(correlation_matrix):
    """Plot a correlation heatmap."""
    plt.figure(figsize=(10, 8))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0
    )

    plt.title("Correlation Matrix of Steam Games")
    plt.tight_layout()
    plt.show()


def plot_top_peak_ccu(df, top_n=10):
    """Plot the games with the highest Peak CCU."""
    data = df[["Name", "Peak CCU"]].copy()
    data["Peak CCU"] = pd.to_numeric(data["Peak CCU"], errors="coerce")
    data = data.dropna(subset=["Name", "Peak CCU"])
    data = data.nlargest(top_n, "Peak CCU")
    data = data.sort_values("Peak CCU")

    plt.figure(figsize=(10, 6))
    plt.barh(data["Name"].astype(str), data["Peak CCU"])
    plt.xlabel("Peak Concurrent Users")
    plt.ylabel("Game")
    plt.title(f"Top {top_n} Games by Peak CCU")
    plt.tight_layout()
    plt.show()


def plot_positive_negative_reviews(df):
    """Compare positive and negative review counts."""
    data = df[["Positive", "Negative"]].copy()

    for column in ["Positive", "Negative"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna()
    data = data[(data["Positive"] >= 0) & (data["Negative"] >= 0)]

    # Sample at most 5000 rows so the chart stays readable.
    if len(data) > 5000:
        data = data.sample(n=5000, random_state=42)

    plt.figure(figsize=(9, 6))
    plt.scatter(
        data["Positive"],
        data["Negative"],
        alpha=0.35,
        s=15
    )
    plt.xscale("symlog")
    plt.yscale("symlog")
    plt.xlabel("Positive Reviews")
    plt.ylabel("Negative Reviews")
    plt.title("Positive vs Negative Reviews")
    plt.tight_layout()
    plt.show()
