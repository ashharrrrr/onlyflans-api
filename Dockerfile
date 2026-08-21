FROM python:3.12-slim

WORKDIR /code

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv \
    && uv sync --locked --no-dev

COPY ./app /code/app

CMD ["uv", "run", "--no-sync", "fastapi", "run", "app/main.py", "--port", "8000"]
