lint:
	poetry run flake8 .

test:
	poetry run pytest --cov=src --cov-report=term-missing --cov-report=html --cov-report=xml

black:
	poetry run black .