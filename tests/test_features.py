"""Tests for feature engineering utilities."""

import pandas as pd
import pytest

from src.features import (
    add_missing_flag,
    add_owners_mid,
    add_review_columns,
    price_group,
    release_period,
    remove_missing_owners,
)


def test_add_missing_flag_creates_indicator_column():
    df = pd.DataFrame({"x": [1.0, None, 3.0]})
    result = add_missing_flag(df, "x")
    assert "x_missing" in result.columns
    assert result["x_missing"].tolist() == [0, 1, 0]


def test_remove_missing_owners_keeps_real_ranges():
    df = pd.DataFrame({"Estimated owners": ["0 - 0", "0 - 20000", "20000 - 50000"]})
    result = remove_missing_owners(df)
    assert result["Estimated owners"].tolist() == ["0 - 20000", "20000 - 50000"]


def test_add_owners_mid_uses_midpoint():
    df = pd.DataFrame({"Estimated owners": ["20000 - 50000", "0 - 20000"]})
    assert add_owners_mid(df)["Owners_mid"].tolist() == [35000, 10000]


def test_add_review_columns_needs_ten_reviews():
    df = pd.DataFrame({"Positive": [9, 8, 0], "Negative": [0, 2, 0]})
    result = add_review_columns(df)
    assert result["Total reviews"].tolist() == [9, 10, 0]
    assert result["Positive ratio"].isna().tolist() == [True, False, True]
    assert result.loc[1, "Positive ratio"] == 80


@pytest.mark.parametrize("price, group", [
    (0, "Miễn phí"),
    (0.99, "Thấp"),
    (4.99, "Thấp"),
    (5, "Trung bình"),
    (14.99, "Trung bình"),
    (15, "Cao"),
    (999.98, "Cao"),
])
def test_price_group_boundaries(price, group):
    assert price_group(price) == group


@pytest.mark.parametrize("year, period", [
    (2013, "Trước 2014"),
    (2014, "2014-2017"),
    (2017, "2014-2017"),
    (2018, "2018-2020"),
    (2020, "2018-2020"),
    (2021, "2021-2023"),
    (2023, "2021-2023"),
    (2024, "2024-2025"),
    (2025, "2024-2025"),
])
def test_release_period_boundaries(year, period):
    assert release_period(year) == period
