"""Feature engineering functionality."""

from __future__ import annotations

import pandas as pd


def add_missing_flag(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Create a binary indicator for missing values in a column."""
    df = df.copy()
    df[f"{column}_missing"] = df[column].isna().astype(int)
    return df
