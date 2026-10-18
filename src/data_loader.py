"""Utilities for loading project datasets."""

from __future__ import annotations

import pandas as pd


def load_csv(path: str):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)
