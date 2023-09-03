# Платформа блога

✅ CRUD, pagination, filtering, sorting and searching

✅ Relationship: one-to-one, one-to-many, many-to-many

✅ Unit tests

✅ Docker and docker compose

✅ Production

✅ Nginx and gunicorn

✅ Static and Media

✅ Unit tests


## Быстрый старт

**ПРИМЕЧАНИЕ**: Проект использует Python 3.11, поэтому перед началом установки его необходимо установить. Рекомендуется использовать [`pyenv`](https://github.com/pyenv/pyenv) для установки.

**ПРИМЕЧАНИЕ**: Корень проекта Django находится в папке `src`.

### Вот краткая инструкция по быстрой настройке проекта для разработки:

1. Установите poetry.

2. Склонируйте репозиторий:
```bash
$ git clone https://github.com/azizjon-aliev/blog_platform.git
```

3. Установите зависимости:
```bash
$ poetry install
$ poetry shell
```

4. Добавьте и настройте файл `.env`: `$ cp .env.example .env` -> отредактируйте `.env`.
5. Выполните `make collectstatic`
6. Выполните `make migrate`
7. Выполните `make test`
8. Вручную создайте суперпользователя: `$ make initadmin`.
9. Выполните `make loaddata`
10. Запустите сервер: $ make runserver.

### Использование с Docker

Для локальной разработки:

`$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.local.yml --env-file ./.env up -d --build`

Подробнее о [docker-compose extends](https://docs.docker.com/compose/extends/)

### Использование Postgres с Docker

В проекте используется Postgres в качестве базы данных. Чтобы использовать Postgres с Docker:

1. Добавьте `POSTGRES_DB=blog_patform, POSTGRES_USER=blog_patform_user, POSTGRES_PASSWORD=blog_patform_password` в файл `.env`
2. Из корня проекта выполните команду: `$ docker run --rm --volume pgdata:/var/lib/postgresql/data --name pg --env-file ./.env -d -p 5432:5432 postgres:14-alpine`


### URL
1. `http://127.0.0.1:8000/admin`
2. `http://127.0.0.1:8000/docs`

### Default user
1. username - `admin`
2. email - `admin@example.com`
3. password - `admin`


