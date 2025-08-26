import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")

def main():
    orders = pd.read_csv(RAW_DATA_DIR / "olist_orders_dataset.csv")
    customers = pd.read_csv(RAW_DATA_DIR / "olist_customers_dataset.csv")

    df = orders.merge(customers, on="customer_id", how="left")
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_DIR / "orders.csv", index=False)
    print("✅ Arquivo salvo em data/processed/orders.csv")

if __name__ == "__main__":
    main()

