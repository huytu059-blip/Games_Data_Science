"""Tests for the project layout."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from run_pipeline import NOTEBOOKS  # noqa: E402


def test_pipeline_notebooks_exist():
    for name in NOTEBOOKS:
        assert (PROJECT_ROOT / "notebooks" / (name + ".ipynb")).exists(), name


def test_every_notebook_is_in_the_pipeline():
    found = sorted(path.stem for path in (PROJECT_ROOT / "notebooks").glob("*.ipynb"))
    assert found == sorted(NOTEBOOKS)
