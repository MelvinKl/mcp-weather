lint:
	uv run flake8 .

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf coverage.xml
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html --cov-report=xml && uv run flake8 . && uv run black .

black:
	uv run black .
