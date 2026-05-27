# Movie API

API для онлайн-кинотеатра на Django REST Framework

## Установка и запуск

```bash
# Клонировать репозиторий
git clone <ссылка на ваш репозиторий>

# Перейти в папку
cd my_movie_api

# Создать виртуальное окружение
python -m venv venv

# Активировать окружение
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Выполнить миграции
python manage.py migrate

# Создать суперпользователя (опционально)
python manage.py createsuperuser

# Запустить сервер
python manage.py runserver


python manage.py makemigrations
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/admin/
python manage.py createsuperuser
http://127.0.0.1:8000/api/v1/movies/
source venv/Scripts/activate

# Запросы

http://127.0.0.1:8000/api/v1/movies/        # Список фильмов	
http://127.0.0.1:8000/api/v1/movies/1/      # Один фильм (id=1)
http://127.0.0.1:8000/api/v1/directors/     # Список режиссёров	
http://127.0.0.1:8000/api/v1/genres/        # Список жанров	
http://127.0.0.1:8000/api/v1/actors/        # Список актёров	
http://127.0.0.1:8000/api/v1/movies/?title=Начало    # Фильтр по названию	