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