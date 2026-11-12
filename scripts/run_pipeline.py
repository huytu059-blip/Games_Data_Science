"""Run the project notebooks in order.

Usage:
    python scripts/run_pipeline.py        run all notebooks
    python scripts/run_pipeline.py 03     start from notebook 03
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "games.csv"

NOTEBOOKS = [
    "00_reduce_raw",
    "01_data_quality",
    "02_eda",
    "02b_eda_rq3_rq4",
    "03_ml_readiness",
    "04_modeling",
    "05_model_evaluation",
    "06_statistical_inference",
    "07_big_data_ethics_bias",
]

# File games.csv tren GitHub chi la mau 8 dong, file that khoang 400 MB
MIN_RAW_SIZE = 100 * 1024 * 1024


def has_full_raw_file():
    """Check that the real raw file is available, not the small sample."""
    return RAW_FILE.exists() and RAW_FILE.stat().st_size > MIN_RAW_SIZE


def run_notebook(name):
    """Run one notebook and save its outputs. Return True if it worked."""
    print("Dang chay", name, "...", flush=True)
    command = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook", "--execute", "--inplace",
        "--ExecutePreprocessor.timeout=1800",
        str(NOTEBOOK_DIR / (name + ".ipynb")),
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        print(result.stderr[-2000:])
        return False
    return True


def run_notebooks(names):
    """Run a list of notebooks in order and stop at the first error."""
    for name in names:
        if name == "00_reduce_raw" and not has_full_raw_file():
            print("Bo qua", name, "vi chua co file games.csv day du (xem README)")
            continue
        if not run_notebook(name):
            print("Loi o notebook", name, "- da dung lai")
            return 1
    print("Da chay xong")
    return 0


def main():
    names = NOTEBOOKS
    if len(sys.argv) > 1:
        start = sys.argv[1]
        names = [name for name in NOTEBOOKS if name >= start]
        if not names:
            print("Khong tim thay notebook bat dau tu", start)
            return 1
    return run_notebooks(names)


if __name__ == "__main__":
    sys.exit(main())
