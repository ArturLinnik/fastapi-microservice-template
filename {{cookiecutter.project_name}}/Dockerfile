FROM python:3.10

WORKDIR /ms

RUN pip install poetry

COPY ./ /ms/ 

RUN poetry config virtualenvs.create false && poetry install

EXPOSE 8000

CMD uvicorn run:app --host 0.0.0.0 --port 8000
