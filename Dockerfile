FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN apt-get update && \
    apt-get install -y libpq-dev python3-dev gcc libjpeg-dev zlib1g-dev
RUN python -m pip install --upgrade pip && \
    pip install pipenv && \
    pip install psycopg2-binary && \
    pip install Pillow
RUN pipenv install --system --deploy

COPY . /code