# Games Data Science

A Python and Jupyter project for data quality review, exploratory analysis, and model evaluation.

## Project structure

- `data/raw/`: source datasets; keep `games.csv` unchanged.
- `data/processed/`: reduced and processed datasets.
- `notebooks/`: ordered analysis notebooks; `notebooks/archive/` keeps alternate and historical versions.
- `src/`: reusable data, feature, model, evaluation, and visualization code.
- `scripts/`: script entry points.
- `tests/`: unit tests.
- `docs/`: data dictionary and project documentation.
- `reports/`: reports, figures, and tables.
- `models/`: trained model artifacts when available.
- `dashboard/`: dashboard application.
- `presentation/`: presentation outline.

## Data

- Source: [Steam Games Dataset on Kaggle](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) (`games.csv`, about 400 MB, 125,855 games).
- The `data/raw/games.csv` file in this repository is only an **8-row sample**, because GitHub rejects files over 100 MB. Running `00_reduce_raw` on it gives wrong results.
- To run `00_reduce_raw`, download the full `games.csv` from Kaggle and place it at `data/raw/games.csv`. To stop Git from showing it as modified, run `git update-index --skip-worktree data/raw/games.csv`.
- `data/processed/games_reduced.csv` (full data, 21 columns) is committed, so `01_data_quality` and later notebooks can run without the raw file.
- `data/processed/games_cleaned.csv` is not committed; run `01_data_quality` to create it.

## Quick start

1. Install the listed dependencies with `pip install -r requirements.txt`.
2. Start Jupyter from the `notebooks/` directory so relative data paths resolve.
3. Open `00_reduce_raw.ipynb`, then continue with `01_data_quality.ipynb` and the following numbered notebooks.

The reduction notebook writes `data/processed/games_reduced.csv`; running it again replaces that processed output.

## Data flow rules

Run the notebooks in order: `00_reduce_raw` → `01_data_quality` → `02_eda` → `04_modeling`.

- Only `00_reduce_raw` reads the raw file: it checks the raw structure, explains why columns are dropped, and writes `data/raw/games.csv` → `data/processed/games_reduced.csv` (21 columns kept for the research questions, all rows kept).
- `01_data_quality` audits and cleans `games_reduced.csv`, then writes `data/processed/games_cleaned.csv` plus `reports/games_data_quality_audit.xlsx` and `reports/cleaning_log.csv`.
- All analysis notebooks after that (`02_eda`, `04_modeling`, ...) read only `games_cleaned.csv`. No notebook other than `00_reduce_raw` reads `games.csv`.
- No notebook overwrites `data/raw/games.csv`.
- The raw header `DiscountDLC count` is two columns (`Discount`, `DLC count`) merged into one; always split it when reading the raw file, otherwise every column from there on is shifted by one.
- `notebooks/archive/` holds old versions and is not part of the pipeline.
