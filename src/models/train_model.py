import pandas as pd
import joblib
import json
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

PROCESSED_DATA_DIR = Path("data/processed")
MODELS_DIR = Path("models")
REPORTS_DIR = Path("reports")

def main():
    orders = pd.read_csv(PROCESSED_DATA_DIR / "orders_features.csv")

    feature_cols = ["order_year", "order_month", "order_day"]
    target_col = "delivered_late"

    X = orders[feature_cols]
    y = orders[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Acurácia: {acc:.4f}")
    print("\nRelatório de classificação:\n")
    print(classification_report(y_test, y_pred))

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODELS_DIR / "model.pkl")

    with open(MODELS_DIR / "feature_columns.json", "w") as f:
        json.dump(feature_cols, f)

    with open(REPORTS_DIR / "metrics.txt", "w") as f:
        f.write(f"Acurácia: {acc:.4f}\n")
        f.write(classification_report(y_test, y_pred))

    print("✅ Modelo salvo em models/model.pkl")
    print("✅ Colunas salvas em models/feature_columns.json")
    print("✅ Métricas em reports/metrics.txt")

if __name__ == "__main__":
    main()

