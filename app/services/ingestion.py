import pandas as pd
from pathlib import Path

def load_transactions(path: str = "data/raw/transactions.csv"):
    p = Path(path)
    if not p.exists():
        return pd.DataFrame()
    if p.suffix == ".parquet":
        return pd.read_parquet(p)
    return pd.read_csv(p)

def save_processed(df: pd.DataFrame, path: str = "data/processed/transactions.parquet"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    return path