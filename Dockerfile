FROM python:3.10-slim-buster as builder

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80