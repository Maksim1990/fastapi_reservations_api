FROM python:3.10

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.3.2

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY pyproject.toml poetry.lock*  /code/
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./app /code/app
ENTRYPOINT ["tail", "-f", "/dev/null"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

#uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
