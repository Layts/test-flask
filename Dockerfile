FROM python:3.8

# System deps:
RUN pip install poetry

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
# Project initialization:
RUN poetry install

EXPOSE 5000

COPY ./ /app