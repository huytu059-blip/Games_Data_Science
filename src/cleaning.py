"""Data cleaning utilities."""

from __future__ import annotations

import pandas as pd


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate records from a DataFrame."""
    return df.drop_duplicates().reset_index(drop=True)


def fill_missing_numeric(df: pd.DataFrame, columns=None, value=0):
    """Fill missing numeric values for selected columns."""
    cols = df.columns if columns is None else columns
    return df[cols].fillna(value)
