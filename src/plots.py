"""Visualization helpers for EDA and reporting."""

from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(series, title: str = "Distribution"):
    """Create a simple histogram for a pandas Series."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(series, ax=ax)
    ax.set_title(title)
    return fig, ax


#34
def plot_correlation_heatmap(correlation_matrix):
    """Ve bieu do nhiet tuong quan giua cac bien so."""

    import matplotlib.pyplot as plt
    import seaborn as sns

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


#35
def plot_top_peak_ccu(df, top_n=10):
    """Ve bieu do cac game co Peak CCU cao nhat."""
    import matplotlib.pyplot as plt
    import pandas as pd

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
    """So sanh so luot danh gia tich cuc va tieu cuc."""
    import matplotlib.pyplot as plt
    import pandas as pd

    data = df[["Positive", "Negative"]].copy()

    for column in ["Positive", "Negative"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna()
    data = data[(data["Positive"] >= 0) & (data["Negative"] >= 0)]

    # Lay mau toi da 5000 dong de bieu do de quan sat hon.
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
