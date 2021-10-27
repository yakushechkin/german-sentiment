.PHONY: all test clean

install:
	pip install --upgrade pip &&\
		pip install -r requirements-dev.txt
		
format:
	black ./ --exclude=.env/
	
lint:
	pylint --disable=R,C app/

test:
	python -m pytest -vv --cov=app/ test/test_api.py

build:
	docker build -t sentiment-app .

run:
	docker run -d -p 8000:8000 --name sentiment-app sentiment-app



