runserver:
	poetry run python -m src.manage runserver

runserver-prod:
	poetry run gunicorn --bind 0.0.0.0:8000 src.config.wsgi:application

collectstatic:
	poetry run python -m src.manage collectstatic --noinput

migrate:
	poetry run python -m src.manage migrate

migrations:
	poetry run python -m src.manage makemigrations

initadmin:
	poetry run python -m src.manage initadmin

loaddata:
	poetry run python -m src.manage loaddata --format yaml data/tag.yaml
	poetry run python -m src.manage loaddata --format yaml data/category.yaml
