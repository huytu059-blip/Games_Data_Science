"""Evaluation utilities for model performance."""

from __future__ import annotations

from sklearn.metrics import accuracy_score, classification_report


def evaluate_model(y_true, y_pred):
    """Return a simple evaluation summary for a classification task."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "report": classification_report(y_true, y_pred, output_dict=True),
    }
