install:
	pip install --upgrade pip
	pip install -r requirements.txt

train:
	cd app && python train_model.py

serve:
	cd app && uvicorn serve_model:app --reload --port 8010

build-image:
	docker build -t ml-service-image .

run-container:
	docker run -d --name ml-service-container -p 80:80 ml-service-image && echo "Container is running at: http://0.0.0.0/docs"

stop-container:
	docker stop ml-service-container
	docker rm ml-service-container