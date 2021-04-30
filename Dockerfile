FROM python:3.9.4-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --requirement requirements.txt

COPY . .

CMD gunicorn --config python:config.gunicorn
