install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 main.py

test:
	python -m pytest -vv test_main.py

all: install lint test
