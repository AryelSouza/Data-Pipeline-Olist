⚙️ Instalação

Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Data-Pipeline-Olist.git
cd Data-Pipeline-Olist
```

Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```
🛠️ Uso com Makefile

O projeto é totalmente automatizado via Makefile.
A ordem correta de execução é:

Pré-processamento dos dados
```bash
make process
```

➡️ Gera data/processed/orders.csv

Construção das features
```bash
make features
```

➡️ Gera data/processed/orders_features.csv

Treinamento do modelo
```bash
make train
```

➡️ Salva:

Modelo treinado em models/model.pkl

Colunas usadas em models/feature_columns.json

Métricas em reports/metrics.txt

Predição
```bash
make predict


#Por padrão, o script usa o pedido:

00010242fe8c5a6d1ba2dd792cb16214
```

Para escolher outro pedido, rode diretamente o script:
```bash
. venv/bin/activate && python src/models/predict_model.py --order-id <ORDER_ID>
```
📊 Exemplo de Saída

Treinamento:
```bash
Acurácia: 0.9214

Relatório de classificação:
              precision    recall  f1-score   support

           0       0.92      1.00      0.96     18325
           1       0.00      0.00      0.00      1564

    accuracy                           0.92     19889
   macro avg       0.46      0.50      0.48     19889
weighted avg       0.85      0.92      0.88     19889
```

Predição:
```bash
🔮 Previsão para o pedido 00010242fe8c5a6d1ba2dd792cb16214: Entrega no prazo
```
