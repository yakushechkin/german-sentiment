FROM python:3.8

WORKDIR /sentiment-app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY main.py .
COPY ./app ./app

CMD ["python", "./main.py"]

