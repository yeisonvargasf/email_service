FROM python:3.9.4-slim

WORKDIR /usr/src/app

RUN apt update \
    && apt install build-essential libpq-dev --no-install-recommends --quiet --yes \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/prod.txt .

RUN pip install --requirement prod.txt

COPY . .

CMD scripts/entrypoint.sh
