setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest

lint:
	ruff check .

format:
	black .

run:
	python scripts/run.py
