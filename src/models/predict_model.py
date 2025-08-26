import pandas as pd
import joblib
import json
import argparse
from pathlib import Path

PROCESSED_DATA_DIR = Path("data/processed")
MODELS_DIR = Path("models")

def load_model():
    model = joblib.load(MODELS_DIR / "model.pkl")
    with open(MODELS_DIR / "feature_columns.json", "r") as f:
        feature_cols = json.load(f)
    return model, feature_cols

def predict(order_id: str):
    model, feature_cols = load_model()

    orders = pd.read_csv(PROCESSED_DATA_DIR / "orders_features.csv")
    order = orders[orders["order_id"] == order_id]

    if order.empty:
        print(f"❌ Pedido {order_id} não encontrado!")
        return

    X = order[feature_cols]
    y_pred = model.predict(X)[0]
    print(f"🔮 Previsão para o pedido {order_id}: {'Entrega atrasada' if y_pred == 1 else 'Entrega no prazo'}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order-id", type=str, default=None, help="ID do pedido a ser previsto")
    args = parser.parse_args()

    if args.order_id is None:
        orders = pd.read_csv(PROCESSED_DATA_DIR / "orders_features.csv")
        args.order_id = orders["order_id"].iloc[0]  # pega o primeiro como default
        print(f"⚠️ Nenhum order_id informado, usando {args.order_id}")

    predict(args.order_id)

if __name__ == "__main__":
    main()

