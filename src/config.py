from pathlib import Path

RANDOM_STATE = 42

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
FIGURES_DIR = ROOT_DIR / "figures"

RAW_CSV = DATA_DIR / "diabetes_binary_health_indicators_BRFSS2015.csv"
SAMPLED_CSV = DATA_DIR / "diabetes_sampled.csv"
SAMPLED_ENGINEERED_CSV = DATA_DIR / "diabetes_sampled_final.csv"
DROPPED_FEATURES_JSON = DATA_DIR / "dropped_features.json"
TARGET_COL = "Diabetes_binary"

SAMPLE_SIZE = 40000
TEST_SIZE = 0.2

# Controls which sample 02_preprocessing.ipynb reads. True = use the output of
# 01b_feature_engineering.ipynb (engineered features added, weak raw features
# dropped per its ablation analysis). False = use the untouched 01_eda.ipynb
# sample (all 21 raw features, no engineered columns).
USE_ENGINEERED_FEATURES = True

FIGURES_DIR.mkdir(parents=True, exist_ok=True)
