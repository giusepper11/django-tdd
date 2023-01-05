build:
	docker compose build

run:
	docker compose up

lint:
	docker compose run --rm app sh -c "flake8"

tests:
	docker compose run --rm app sh -c "python manage.py test"