FROM python:3.8.20
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

ADD pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi


COPY . /app


# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]