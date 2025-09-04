# Common developer tasks
.PHONY: install lint format type test cov precommit all

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt -r requirements-dev.txt
	pre-commit install

lint:
	ruff check src tests

format:
	ruff format src tests

type:
	mypy src

test:
	pytest --maxfail=1 --disable-warnings

cov:
	pytest --cov=src/textstat_mini --cov-report=term --cov-report=xml

precommit:
	pre-commit run --all-files

all: install lint type test cov
