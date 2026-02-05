FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir pytest

COPY . /app

CMD ["pytest", "-q"]
