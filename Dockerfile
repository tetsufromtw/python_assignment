FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

COPY . /app
ENV env_file .env
CMD ["uvicorn", "financial.main:app", "--host", "0.0.0.0", "--port", "8000"]

