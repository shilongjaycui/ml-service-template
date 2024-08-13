FROM python:3.9
 
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 80

COPY . /code/
COPY ./model.pkl /code/

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "80"]