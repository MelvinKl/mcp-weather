lint:
	poetry run flake8 .

test:
	poetry run pytest

black:
	poetry run black .