"""Model-building helpers and training wrappers."""

from __future__ import annotations

from sklearn.model_selection import train_test_split


def train_test_split_data(X, y, test_size=0.2, random_state=42):
    """Simple wrapper around scikit-learn train/test split."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
