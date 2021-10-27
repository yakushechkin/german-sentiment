.PHONY: all test clean

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black ./ --exclude=.env/
	
lint:
	pylint --disable=R,C app/

test:
	python -m pytest -vv --cov=app/ test/test_api.py
