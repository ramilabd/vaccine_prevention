dev-start:
	python core/manage.py runserver

lint:
	poetry run flake8 core

install:
	poetry install

selfcheck:
	poetry check

.PHONY: install test tests lint selfcheck check