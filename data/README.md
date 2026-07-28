# Data

This project uses the **Diabetes Health Indicators Dataset** (CDC BRFSS 2015),
available on Kaggle:

https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

## Automatic download (recommended)

Run `src/00_data_load.ipynb` first. It uses `kagglehub` to download the dataset
and copies the CSV into this folder at the path the rest of the pipeline expects:

```
data/diabetes_binary_health_indicators_BRFSS2015.csv
```

You need a free Kaggle account and API credentials the first time you run it:

1. Go to https://www.kaggle.com/settings → **API** → **Create New Token**. This
   downloads a `kaggle.json` file.
2. Place it at `~/.kaggle/kaggle.json` (Linux/Mac) or
   `C:\Users\<you>\.kaggle\kaggle.json` (Windows), or set the `KAGGLE_USERNAME`
   and `KAGGLE_KEY` environment variables. `kagglehub` will also prompt for
   these interactively if it can't find them.

## Manual download (alternative)

If you'd rather not use the Kaggle API, download the CSV manually from the
link above and place it at `data/diabetes_binary_health_indicators_BRFSS2015.csv`,
or via the Kaggle CLI:

```
kaggle datasets download -d alexteboul/diabetes-health-indicators-dataset -p data --unzip
```

Then continue with the notebooks in `src/` in order (see project README.md).

The raw CSV is not committed to this repository — download it yourself following
one of the steps above.
