"""Functions related to data quality checks."""

from __future__ import annotations

import pandas as pd


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return the missing-value summary for each column."""
    return df.isna().sum().rename("missing_count").to_frame()


def duplicate_count(df: pd.DataFrame) -> int:
    """Return the number of duplicate rows in the DataFrame."""
    return int(df.duplicated().sum())
