FROM python:3.12.10-slim

ARG APPDIR=/code
WORKDIR ${APPDIR}
ENV PYTHONPATH=${APPDIR}

RUN pip install poetry==2.1.3
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app/ app/

CMD ["hypercorn", "--bind", "0.0.0.0:80", "--worker-class", "uvloop", "--workers", "5", "asgi:app.main:app"]
