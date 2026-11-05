# Games Data Science

A Python and Jupyter project that studies which characteristics of Steam games are related to their popularity, player ratings, and playtime. It covers data cleaning, exploratory analysis, statistical inference, modeling, and bias review.

## Research questions

- RQ1: Which factors are related to the popularity of a game?
- RQ2: Which factors are related to positive player ratings?
- RQ3: Which characteristics are related to playtime?
- RQ4: How do popularity and ratings change with release time?
- RQ5: How is price related to popularity and ratings?

The results are in `reports/final_report.md`. See `docs/project_charter.md` for the project scope.

## Project structure

- `data/raw/`: source datasets; keep `games.csv` unchanged.
- `data/processed/`: reduced and processed datasets.
- `notebooks/`: ordered analysis notebooks; `notebooks/archive/` keeps alternate and historical versions.
- `src/`: reusable code. `01_data_quality` uses `data_quality.py` and `cleaning.py`, `03_ml_readiness` uses `features.py`.
- `scripts/`: scripts that run the notebooks in order.
- `tests/`: unit tests for `src/` and the notebook list.
- `docs/`: data dictionary and project documentation.
- `reports/`: reports, figures, and tables.
- `models/`: trained models, created by `04_modeling` and not committed.
- `dashboard/`: placeholder, not implemented yet.

## Data

- Source: [Steam Games Dataset on Kaggle](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) (`games.csv`, about 400 MB, 125,855 games).
- The `data/raw/games.csv` file in this repository is only an **8-row sample**, because GitHub rejects files over 100 MB. Running `00_reduce_raw` on it gives wrong results.
- To run `00_reduce_raw`, download the full `games.csv` from Kaggle and place it at `data/raw/games.csv`. To stop Git from showing it as modified, run `git update-index --skip-worktree data/raw/games.csv`.
- `data/processed/games_reduced.csv` (full data, 21 columns) is committed, so `01_data_quality` and later notebooks can run without the raw file.
- `data/processed/games_cleaned.csv` and `data/processed/games_features.csv` are not committed; run `01_data_quality` and `03_ml_readiness` to create them.

## Quick start

1. Install the listed dependencies with `pip install -r requirements.txt`.
2. Run all notebooks with `python scripts/run_pipeline.py`, or start from one notebook with `python scripts/run_pipeline.py 03`. `python scripts/run_data_quality.py` runs only `00` and `01`. The scripts skip `00_reduce_raw` when the full `games.csv` is not available.
3. To work in Jupyter instead, start it from the `notebooks/` directory so relative data paths resolve, and open the notebooks in order.
4. Run the tests with `pytest`.

The reduction notebook writes `data/processed/games_reduced.csv`; running it again replaces that processed output.

## Data flow rules

Run the notebooks in order: `00_reduce_raw` → `01_data_quality` → `02_eda` → `02b_eda_rq3_rq4` → `03_ml_readiness` → `04_modeling` → `05_model_evaluation` → `06_statistical_inference` → `07_big_data_ethics_bias`.

- Only `00_reduce_raw` reads the raw file: it checks the raw structure, explains why columns are dropped, and writes `data/raw/games.csv` → `data/processed/games_reduced.csv` (21 columns kept for the research questions, all rows kept).
- `01_data_quality` audits and cleans `games_reduced.csv`, then writes `data/processed/games_cleaned.csv` plus `reports/games_data_quality_audit.xlsx` and `reports/cleaning_log.csv`.
- `02_eda` and `02b_eda_rq3_rq4` read `games_cleaned.csv`. `03_ml_readiness` also reads it and writes `data/processed/games_features.csv`, which has the train/test split in the `split` column.
- The later part of `04_modeling` and notebooks `05`, `06`, `07` read `games_features.csv`. `04_modeling` saves the models to `models/mo_hinh.joblib`, which `05` and `07` load. No notebook other than `00_reduce_raw` reads `games.csv`.
- Rows with `Estimated owners` = "0 - 0" stay in `games_cleaned.csv` but are treated as missing data and removed from all popularity analysis and models, because this group includes very large games such as Call of Duty: Warzone.
- No notebook overwrites `data/raw/games.csv`.
- The raw header `DiscountDLC count` is two columns (`Discount`, `DLC count`) merged into one; always split it when reading the raw file, otherwise every column from there on is shifted by one.
- `notebooks/archive/` holds old versions and is not part of the pipeline.
