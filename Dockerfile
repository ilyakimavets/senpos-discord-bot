FROM python:3.7.0-alpine3.8

COPY requirements.txt ./
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev git && pip install --no-cache-dir -r requirements.txt


COPY . /app

WORKDIR /app

CMD python3 app.py
