"""Tests for feature engineering utilities."""

import pandas as pd

from src.features import add_missing_flag


def test_add_missing_flag_creates_indicator_column():
    df = pd.DataFrame({"x": [1.0, None, 3.0]})
    result = add_missing_flag(df, "x")
    assert "x_missing" in result.columns
    assert result["x_missing"].tolist() == [0, 1, 0]
