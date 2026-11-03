"""Functions related to data quality checks."""

from __future__ import annotations

import pandas as pd


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return the missing-value summary for each column."""
    return df.isna().sum().rename("missing_count").to_frame()


def duplicate_count(df: pd.DataFrame) -> int:
    """Return the number of duplicate rows in the DataFrame."""
    return int(df.duplicated().sum())


def detect_outliers_iqr(
    df: pd.DataFrame,
    columns=None
) -> pd.DataFrame:
    """Detect potential outliers using the IQR method."""

    if columns is None:
        columns = df.select_dtypes(include="number").columns.tolist()

    results = []

    for column in columns:
        series = df[column].dropna()

        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outlier_mask = (
            (series < lower_bound) |
            (series > upper_bound)
        )

        results.append({
            "column": column,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "outlier_count": int(outlier_mask.sum()),
            "outlier_percent": round(
                outlier_mask.mean() * 100, 2
            ),
        })

    return pd.DataFrame(results)
