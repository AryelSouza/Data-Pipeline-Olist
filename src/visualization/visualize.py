import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROCESSED_DATA_DIR = Path("data/processed")
REPORTS_DIR = Path("reports")

def main():
    orders = pd.read_csv(PROCESSED_DATA_DIR / "orders_features.csv")

    counts = orders["delivered_late"].value_counts()
    counts.plot(kind="bar")
    plt.title("Distribuição de Pedidos Atrasados")
    plt.xticks([0, 1], ["No prazo", "Atrasado"], rotation=0)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(REPORTS_DIR / "delays_distribution.png")
    print("✅ Gráfico salvo em reports/delays_distribution.png")

if __name__ == "__main__":
    main()

