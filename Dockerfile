FROM python:3.12-alpine

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .


