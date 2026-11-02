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

## Quick start

1. Install the listed dependencies with `pip install -r requirements.txt`.
2. Start Jupyter from the `notebooks/` directory so relative data paths resolve.
3. Open `00_reduce_raw.ipynb`, then continue with `01_data_quality.ipynb` and the following numbered notebooks.

The reduction notebook writes `data/processed/games_reduced.csv`; running it again replaces that processed output.
