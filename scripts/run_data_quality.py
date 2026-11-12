"""Run only the data reduction and data quality notebooks."""

import sys

from run_pipeline import run_notebooks


def main():
    return run_notebooks(["00_reduce_raw", "01_data_quality"])


if __name__ == "__main__":
    sys.exit(main())
