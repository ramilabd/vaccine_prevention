dev-start:
	python core/manage.py runserver

lint:
	poetry run flake8 core

install:
	poetry install

selfcheck:
	poetry check

makemigrations:
	poetry run python core/manage.py makemigrations

migrate:
	poetry run python core/manage.py migrate

.PHONY: install test tests lint selfcheck check