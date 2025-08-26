.ONESHELL:

process:
	. venv/bin/activate && python src/data/make_dataset.py

features:
	. venv/bin/activate && python src/features/build_features.py

train:
	. venv/bin/activate && python src/models/train_model.py

predict:
	. venv/bin/activate && python src/models/predict_model.py --order-id 00010242fe8c5a6d1ba2dd792cb16214

visualize:
	. venv/bin/activate && python src/visualization/visualize.py
