"""Tests for model helpers."""

import pandas as pd

from src.evaluation import evaluate_model
from src.models import train_test_split_data


def test_evaluate_model_accuracy():
    result = evaluate_model([0, 1, 1, 0], [0, 1, 0, 0])
    assert result["accuracy"] == 0.75


def test_evaluate_model_when_one_class_is_never_predicted():
    # Baseline luon doan nhan 0 van phai tinh duoc
    result = evaluate_model([0, 1], [0, 0])
    assert result["report"]["1"]["precision"] == 0


def test_split_keeps_class_ratio_with_stratify():
    X = pd.DataFrame({"a": range(100)})
    y = pd.Series([1] * 20 + [0] * 80)
    X_train, X_test, y_train, y_test = train_test_split_data(X, y, stratify=y)
    assert len(X_test) == 20
    assert y_test.mean() == 0.2
