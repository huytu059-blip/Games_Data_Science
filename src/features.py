"""Feature engineering functionality."""

from __future__ import annotations

import numpy as np
import pandas as pd

MISSING_OWNERS = "0 - 0"
MIN_REVIEWS = 10


def add_missing_flag(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Create a binary indicator for missing values in a column."""
    df = df.copy()
    df[f"{column}_missing"] = df[column].isna().astype(int)
    return df


def remove_missing_owners(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where Estimated owners is "0 - 0", which means missing data."""
    return df[df["Estimated owners"] != MISSING_OWNERS].copy()


def add_owners_mid(df: pd.DataFrame) -> pd.DataFrame:
    """Add Owners_mid, the midpoint of the Estimated owners range."""
    df = df.copy()
    low = df["Estimated owners"].str.split(" - ").str[0].astype(float)
    high = df["Estimated owners"].str.split(" - ").str[1].astype(float)
    df["Owners_mid"] = (low + high) / 2
    return df


def add_review_columns(df: pd.DataFrame, min_reviews: int = MIN_REVIEWS) -> pd.DataFrame:
    """Add Total reviews and Positive ratio (%), only for games with enough reviews."""
    df = df.copy()
    df["Total reviews"] = df["Positive"] + df["Negative"]
    df["Positive ratio"] = np.nan
    enough = df["Total reviews"] >= min_reviews
    df.loc[enough, "Positive ratio"] = df.loc[enough, "Positive"] / df.loc[enough, "Total reviews"] * 100
    return df


def price_group(price: float) -> str:
    """Return the price group of one game."""
    if price == 0:
        return "Miễn phí"
    if price < 5:
        return "Thấp"
    if price < 15:
        return "Trung bình"
    return "Cao"


def release_period(year: int) -> str:
    """Return the release period of one game."""
    if year < 2014:
        return "Trước 2014"
    if year <= 2017:
        return "2014-2017"
    if year <= 2020:
        return "2018-2020"
    if year <= 2023:
        return "2021-2023"
    return "2024-2025"
