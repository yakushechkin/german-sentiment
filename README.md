[![Build Status](https://github.com/yakushechkin/german-sentiment/actions/workflows/main.yml/badge.svg)](https://github.com/yakushechkin/german-sentiment/actions/workflows/main.yml)

[![Build Status](https://github.com/yakushechkin/german-sentiment/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yakushechkin/german-sentiment/actions/workflows/docker-image.yml)


# german-sentiment
Micro service for German sentiment classification


This REST API was built with Python 3.8, [Germansentiment](https://huggingface.co/oliverguhr/german-sentiment-bert), FastAPI, Uvicorn and Python standard library.


## Run in docker container:

1. Clone repository

2. Build an image from a Dockerfile
```
make build
```

3. Run the image inside of a container (http://0.0.0.0:8000/): 
```
make run
```

Interactive API docs: http://0.0.0.0:8000/docs

Example of the POST request using cURL:
```
curl -X 'POST' \
  'http://0.0.0.0:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "texts": [
    "Mit keinem guten Ergebniss","Das ist gar nicht mal so gut",
    "Total awesome!","nicht so schlecht wie erwartet",
    "Der Test verlief positiv.","Sie fährt ein grünes Auto."]
}'
```

## Dev setup

Create virtual environment in cloned/downloaded repository and install required packages.

```
python3 -m venv .env
source .env/bin/activate
make install
```

After activating virtual environment, tests can be run:
```
make test
```

Run pylint (code analysis)
```
make lint
```

Run black (uncompromising code formatter)
```
make black
```

Run the app:
```
python3 run.py
```

## Deploying to Google Cloud Platform (GCP)

1. Create a file app.yaml (to configure App Engine app's settings)
2. In the cloud shell run the command to create the app:
``` 
gcloud app create
```
3. Run the following to deploy the app:
``` 
gcloud app deploy
```
Extra: Setup trigger in Google Build (create cloudbuild.yaml to configure this). A simple example of the app structure deployed on GCP can be found here: https://github.com/yakushechkin/gcloud-cd

Also, a good idea is to utilize Cloud Storage (Bucket) for storing the pickled classifier.
