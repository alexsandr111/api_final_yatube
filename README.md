# Проект «API для Yatube»

# Описание проекта

API Yatube позволяет публиковать пользователям блоги.
Функционал проекта включает в себя создание групп для блогов,
пользователи могут оставлять комментарии к блогам,
пользователи имеют возможность подписываться друг на друга.
Для создания постов, комментариев и подписки необходима аутентификация пользователя.

## Используемые технологии и утилиты

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-ff1709?style=flat&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=json-web-tokens)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)

## Библиотеки и версии

```
Django==3.2.16
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0
isort==5.12.0
```

## Запуск проекта

### Клонировать репозиторий:

```
git clone git@github.com:
```

### Cоздать виртуальное окружение:

```
python -m venv venv
```

### Активировать виртуальное окружение:

```
Если у вас Windows
source venv/scripts/activate
    
Если у вас Linux/macOS
source env/bin/activate
```

### Обновить менеджер пакетов pip:

```
python -m pip install --upgrade pip
```

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python manage.py migrate
```

### Дополнительная документация проекта:

```
http://127.0.0.1:8000/redoc/
```

### Запустить проект:

```
python manage.py runserver
```

### Примеры запросов

Получить список всех постов:
```
GET /api/v1/posts/
```

Добавление нового поста:
```
POST /api/v1/posts/
```

Получить список всех групп:
```
GET /api/v1/groups/
```

Добавление нового комментария:
```
POST /api/v1/posts/{post_id}/comments/
```
Удаление комментария по id:
```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```

Получение списока подписок:
```
GET /api/v1/follow/
```

Подписка пользователя на пользователя переданного в запросе:
```
POST /api/v1/follow/
```
