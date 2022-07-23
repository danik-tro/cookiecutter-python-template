.PHONY: setup \
		run \
		test \

setup:
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest -v

lint:
	poetry run flake8

mypy:
	poetry run mypy ./dem

black:
	poetry run isort .; poetry run black .

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
