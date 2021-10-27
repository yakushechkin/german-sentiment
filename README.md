[![Build Status](https://github.com/yakushechkin/german-sentiment/actions/workflows/main.yml/badge.svg)](https://github.com/yakushechkin/german-sentiment/actions/workflows/main.yml)

[![Build Status](https://github.com/yakushechkin/german-sentiment/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yakushechkin/german-sentiment/actions/workflows/docker-image.yml)


# german-sentiment
Micro service for german sentiment classification


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


