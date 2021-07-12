FROM python:3.6.0

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD python3 main.py
