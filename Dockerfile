FROM python:3.10-alpine

ENV DOCKER_DEFAULT_PLATFORM=linux/amd64
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /app

ADD app/ /app
