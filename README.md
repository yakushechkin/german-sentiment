[![Build Status](https://github.com/yakushechkin/german-sentiment/actions/workflows/main.yml/badge.svg)](https://github.com/yakushechkin/german-sentiment/actions/workflows/main.yml)

[![Build Status](https://github.com/yakushechkin/german-sentiment/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yakushechkin/german-sentiment/actions/workflows/docker-image.yml)


# german-sentiment
Micro service for german sentiment classification


This REST API was built with Python 3.8, [Germansentiment](https://huggingface.co/oliverguhr/german-sentiment-bert), FastAPI, Uvicorn and Python standard library.


## Run in docker container:

1. Clone repository

2. Build the container
```
make build
```

3. Run container on http://0.0.0.0:8000/: 
```
make run
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

or Run pylint (code analysis)
```
make lint
```

or Run black (uncompromising code formatter)
```
make black
```

Run the app:
```
python3 run.py
```

