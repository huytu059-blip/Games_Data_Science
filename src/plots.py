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
