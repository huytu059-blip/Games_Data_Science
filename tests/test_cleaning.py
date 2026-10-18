"""Tests for cleaning utilities."""

import pandas as pd

from src.cleaning import drop_duplicates


def test_drop_duplicates_removes_repeated_rows():
    df = pd.DataFrame({"a": [1, 1, 2]})
    result = drop_duplicates(df)
    assert len(result) == 2
