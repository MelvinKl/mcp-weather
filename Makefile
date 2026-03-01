lint:
	poetry run flake8 .

test:
	poetry run pytest && poetry run flake8 . && poetry run black .

black:
	poetry run black .