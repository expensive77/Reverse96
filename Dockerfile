FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /project
WORKDIR /app
COPY project /app