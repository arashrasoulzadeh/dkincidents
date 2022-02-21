# syntax=docker/dockerfile:1
FROM python:3
RUN apt-get update 
RUN apt-get install libpcap-dev libpq-dev -y
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt install build-essential python-dev gcc libxslt-dev libffi-dev libssl-dev -y
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/
