.PHONY: dev test lint

dev:
	flask --app runner.py --debug run

test:
	pytest -v

lint:
	flake8 --config=.flake8