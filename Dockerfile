
FROM python:3.9-slim

COPY ./auth /app/auth
COPY ./config /app/config
COPY ./database /app/database
COPY ./ml /app/ml

COPY ./requirements.txt /app
COPY ./.env /app
COPY ./test.db /app
COPY ./routers /app/routers
COPY ./SchemaModels /app/SchemaModels
COPY ./main.py /app
WORKDIR /app 

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]

