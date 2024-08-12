# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
COPY ./app/model.pkl /code/

# 
CMD ["fastapi", "run", "app/serve_model.py", "--proxy-headers", "--port", "80"]