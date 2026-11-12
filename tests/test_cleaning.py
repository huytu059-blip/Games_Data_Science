"""Tests for cleaning utilities."""

import pandas as pd

from src.cleaning import (
    correct_text_whitespace,
    detect_invalid_ranges,
    drop_duplicates,
    fill_missing_numeric,
)


def test_drop_duplicates_removes_repeated_rows():
    df = pd.DataFrame({"a": [1, 1, 2]})
    result = drop_duplicates(df)
    assert len(result) == 2


def test_fill_missing_numeric_keeps_other_columns():
    df = pd.DataFrame({"a": [1.0, None], "b": ["x", "y"]})
    result = fill_missing_numeric(df, columns=["a"])
    assert result.columns.tolist() == ["a", "b"]
    assert result["a"].tolist() == [1.0, 0.0]


def test_fill_missing_numeric_does_not_change_input():
    df = pd.DataFrame({"a": [None]})
    fill_missing_numeric(df)
    assert df["a"].isna().all()


def test_detect_invalid_ranges_finds_only_bad_values():
    df = pd.DataFrame({"Price": [1.0, -2.0], "Metacritic score": [50, 120]})
    result = detect_invalid_ranges(df)
    assert sorted(result["column"]) == ["Metacritic score", "Price"]
    assert len(result) == 2


def test_detect_invalid_ranges_ignores_missing_columns():
    df = pd.DataFrame({"Other": [-1]})
    assert detect_invalid_ranges(df).empty


def test_correct_text_whitespace_only_strips_text():
    df = pd.DataFrame({"name": ["  Portal 2 "], "price": [1]})
    result = correct_text_whitespace(df, columns=["name"])
    assert result.loc[0, "name"] == "Portal 2"
    assert result.loc[0, "price"] == 1
