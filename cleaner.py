import pandas as pd

def clean_data(df):

    df.columns = df.columns.str.lower().str.strip()

    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"])

    if "revenue" in df.columns:
        df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")

    if "rating" in df.columns:
        df["rating"] = df["rating"].fillna(df["rating"].mean())

    df = df.dropna()

    return df