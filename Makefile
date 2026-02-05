.PHONY: setup test spec-check

setup:
	python -m pip install --upgrade pip
	python -m pip install -e .

test:
	docker build -t chimera-tests .
	docker run --rm chimera-tests

spec-check:
	python scripts/spec_check.py
