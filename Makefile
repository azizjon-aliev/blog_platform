runserver:
	python -m src.manage runserver

runserver-prod:
	python -m src.manage runserver 0.0.0.0:8000

collectstatic:
	python -m src.manage collectstatic --noinput


migrate:
	python -m src.manage migrate


collect:
	python -m src.manage migrate
	python -m src.manage initadmin


migrations:
	python -m src.manage makemigrations

initadmin:
	python -m src.manage initadmin


refresh-db:
	python -m src.manage flush
	python -m src.manage migrate
	python -m src.manage initadmin

fakedata:
	python -m src.manage fakedata
