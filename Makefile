lint:
	poetry run flake8 .

test:
	poetry run pytest --cov=src --cov-report=term-missing --cov-report=html --cov-report=xml && poetry run flake8 . && poetry run black .

black:
	poetry run black .
<<<<<<< HEAD
=======

test:
	poetry run pytest
>>>>>>> origin/main
