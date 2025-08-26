import pandas as pd
from pathlib import Path

PROCESSED_DATA_DIR = Path("data/processed")

def main():
    orders = pd.read_csv(PROCESSED_DATA_DIR / "orders.csv")

    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    orders["order_year"] = orders["order_purchase_timestamp"].dt.year
    orders["order_month"] = orders["order_purchase_timestamp"].dt.month
    orders["order_day"] = orders["order_purchase_timestamp"].dt.day

    orders["delivered_late"] = (
        pd.to_datetime(orders["order_delivered_customer_date"]) >
        pd.to_datetime(orders["order_estimated_delivery_date"])
    ).astype(int)

    orders.to_csv(PROCESSED_DATA_DIR / "orders_features.csv", index=False)
    print("✅ Arquivo salvo em data/processed/orders_features.csv")

if __name__ == "__main__":
    main()

