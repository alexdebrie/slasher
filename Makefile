check: test lint

test:
	python -m unittest discover tests/

lint:
	flake8 .
