<h1 align="center">✨ TEST 21VEK ✨</h1>


## ***Навигация***
- [Описание](#описание)
- [Технологии](#технологии)
- [Установка](#установка)

<a name="описание"></a> 
## ***Описание***

Тестовое задание для компании 21vek

Важно:
  Файл .env был залит на git c ознакомительной целью.

API
Реализованные задачи:

- База данных выбранна PostgreSQL
- Миграции Alembic накатываются автоматически при запуске docker-compose
- Создана полнаценная CRUD новостей, на базе SQLAlchemy и шаблона репозиторий
- Выполнено кеширование на базе Redis
- Выполнено логирование на уровне Middleware
- Все эндпоинты асинхронны
- Выполнена контарезация
- Использовались environment variables 

Workflow
Реализованные задачи:

- Запускается периодическое выполнение задачи (каждые 10 секунд) на базе Cerary
- Периодическая задача отправляет requests на https://jsonplaceholder.com
- Использовались environment variables 
- Запуск переодической задачи реализован на базе Celery beat 
- Реализован web интерфейс Celery на базе Flower

<a name="технологии"></a> 
## ***Технологии***

- [FastApi](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryq.dev/en/stable/#)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)

<a name="установка"></a> 
## ***Установка***

- Метод (Подходит для разворачивания с помощью Docker):
  - Клонировать репозиторий
  - Перейти в папку где находится файл docker-compose.yml
  - Выполнить команду docker compose up -d
  - Пререйти по адресу 127.0.0.1:8000/docs 
  - Пререйти по адресу 127.0.0.1:5556 чтобы посмотреть выполнение
    переодической задачи
  - Выполнить запрос
