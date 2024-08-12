install:
	pip install --upgrade pip

	pip install pandas
	pip install -U scikit-learn
	pip install lightgbm
	pip install pydantic
	pip install fastapi uvicorn

train:
	python train_model.py

serve:
	uvicorn serve_model:app --reload --port 8010