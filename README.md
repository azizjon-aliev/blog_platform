- 1 Clone
- 2 poetry install --no-root
- 3 make collectstatic
- 4 make migrate
- 5 make initadmin
- 6 make loaddata
- 7 make runserver


username - admin
email - admin@example.com
password - admin

run with docker 

docker-compose -f docker/docker-compose.yml -f docker/docker-compose.local.yml --env-file ./.env up -d --build