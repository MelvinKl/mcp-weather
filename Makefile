lint:
	uv run flake8 .

test:
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html --cov-report=xml && uv run flake8 . && uv run black .

black:
	uv run black .