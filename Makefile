install:
	pip3 install -r requirements.txt

lint:
	flake8 src tests

format:
	black src tests

test:
	pytest
