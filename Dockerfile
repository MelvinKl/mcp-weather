FROM python:3.13

WORKDIR /app
RUN pip install poetry

COPY . .
RUN poetry install --no-root

CMD [ "poetry", "run", "python", "src/main.py"]