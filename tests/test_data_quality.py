"""Tests for data quality checks."""

import pandas as pd

from src.data_quality import detect_outliers_iqr, duplicate_count, missing_summary


def test_missing_summary_counts_each_column():
    df = pd.DataFrame({"a": [1, None, None], "b": [1, 2, 3]})
    result = missing_summary(df)
    assert result.loc["a", "missing_count"] == 2
    assert result.loc["b", "missing_count"] == 0


def test_duplicate_count():
    df = pd.DataFrame({"a": [1, 1, 2]})
    assert duplicate_count(df) == 1


def test_detect_outliers_iqr_finds_large_value():
    df = pd.DataFrame({"x": [1, 2, 3, 4, 100]})
    result = detect_outliers_iqr(df)
    assert result.loc[0, "outlier_count"] == 1


def test_detect_outliers_iqr_flags_everything_when_mostly_zero():
    # Day la ly do bao cao khong dung IQR cho cac cot co nhieu so 0
    df = pd.DataFrame({"x": [0, 0, 0, 0, 0, 0, 0, 0, 5, 9]})
    result = detect_outliers_iqr(df)
    assert result.loc[0, "IQR"] == 0
    assert result.loc[0, "outlier_count"] == 2


def test_detect_outliers_iqr_skips_empty_column():
    df = pd.DataFrame({"x": [None, None]})
    assert detect_outliers_iqr(df, columns=["x"]).empty
