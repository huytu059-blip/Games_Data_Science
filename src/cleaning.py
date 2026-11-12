"""Data cleaning utilities."""

from __future__ import annotations

import pandas as pd


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate records from a DataFrame."""
    return df.drop_duplicates().reset_index(drop=True)


def fill_missing_numeric(df: pd.DataFrame, columns=None, value=0):
    """Fill missing numeric values for selected columns and keep the other columns."""
    df = df.copy()
    cols = df.columns if columns is None else columns
    df[cols] = df[cols].fillna(value)
    return df


def detect_invalid_ranges(df: pd.DataFrame) -> pd.DataFrame:
    """Report values outside basic valid ranges without changing data."""

    rules = {
        "Price": (0, None),
        "Required age": (0, None),
        "Metacritic score": (0, 100),
        "Positive": (0, None),
        "Negative": (0, None),
        "Achievements": (0, None),
        "Recommendations": (0, None),
        "Peak CCU": (0, None),
        "Average playtime forever": (0, None),
        "Average playtime two weeks": (0, None),
        "Median playtime forever": (0, None),
        "Median playtime two weeks": (0, None),
    }

    results = []

    for column, (lower, upper) in rules.items():
        if column not in df.columns:
            continue

        values = pd.to_numeric(df[column], errors="coerce")
        invalid = values.notna() & (values < lower)

        if upper is not None:
            invalid |= values.notna() & (values > upper)

        for index in df.index[invalid]:
            results.append({
                "row_index": index,
                "column": column,
                "value": df.loc[index, column],
                "reason": "Outside configured valid range",
            })

    return pd.DataFrame(
        results,
        columns=["row_index", "column", "value", "reason"]
    )


def correct_text_whitespace(df, columns=None):
    """Remove leading and trailing whitespace from text columns."""
    df = df.copy()

    if columns is None:
        columns = df.select_dtypes(
            include=["object", "string"]
        ).columns

    for column in columns:
        df[column] = df[column].map(
            lambda value: value.strip()
            if isinstance(value, str)
            else value
        )

    return df
