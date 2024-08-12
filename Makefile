install:
	pip install --upgrade pip

	pip install -U scikit-learn
	pip install pydantic
	pip install fastapi
	pip install lightgbm
	pip install pandas

train:
	python src/train_model.py