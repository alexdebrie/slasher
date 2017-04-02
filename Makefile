check: test lint

test:
	python -m unittest discover

lint:
	flake8 .
