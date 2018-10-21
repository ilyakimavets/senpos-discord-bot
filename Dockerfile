FROM python:3.7.0-alpine3.8

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

CMD python3 app.py