# inspired by github.com/oliverguhr/german-sentiment-lib/blob/master/germansentiment/tests/test.py

from fastapi.testclient import TestClient

from app.api import app

texts = [
    "Mit keinem guten Ergebniss",
    "Das war unfair",
    "Das ist gar nicht mal so gut",
    "Total awesome!",
    "nicht so schlecht wie erwartet",
    "Das ist gar nicht mal so schlecht",
    "Der Test verlief positiv.",
    "Sie fährt ein grünes Auto.",
    "Der Fall wurde an die Polzei übergeben.",
]


client = TestClient(app)


def test_read_item():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"About": "German Sentiment Classification with Bert"}


def test_multi_document_classification():
    response = client.post("/predict", json={"texts": texts})
    expected = [
        "negative",
        "negative",
        "negative",
        "positive",
        "positive",
        "positive",
        "neutral",
        "neutral",
        "neutral",
    ]
    assert response.status_code == 200
    assert response.json() == {"sentiments": expected}


def test_single_document_classification():
    response = client.post("/predict", json={"texts": [texts[0]]})
    expected = ["negative"]
    assert response.status_code == 200
    assert response.json() == {"sentiments": expected}


def test_long_document_classification():
    response = client.post("/predict", json={"texts": [texts[0] * 100]})
    expected = ["negative"]
    assert response.status_code == 200
    assert response.json() == {"sentiments": expected}


def test_faulty_response():
    response = client.post("/predict", json={"texts": 100})
    expected = ["negative"]
    assert response.status_code == 422
