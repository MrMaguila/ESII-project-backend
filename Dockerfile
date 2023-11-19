FROM python:3.12.0

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install

CMD "./start.sh"
