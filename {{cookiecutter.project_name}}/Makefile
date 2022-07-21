.PHONY: setup \
		run \
		test \

all:

virtual_env:
	poetry shell

setup: virtual_env
	. poetry install
	. poetry run pre-commit install

test:
	. ve/bin/activate; poetry run pytest -v

lint:
	. ve/bin/activate; flake8

mypy:
	. ve/bin/activate; mypy ./dem

black:
	. ve/bin/activate; isort .; black .

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f .coverage
	rm -fr htmlcov/
