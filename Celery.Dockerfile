# syntax=docker/dockerfile:1
FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY api/requirements.txt /code/

RUN pip install -r requirements.txt

COPY api /code/
