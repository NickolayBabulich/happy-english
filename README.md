# Happy English - Английский для всех!

### О проекте:

Happy English - Английский для всех! - сервис дистанционного обучения с возможностью создавать разделы и модули для обучения,
а также итоговое тестирование знаний ученика.

Данный проект представляет собой универсальную платформу для создания курсов обучения любой другой области отличной от английского,
английский язык дан как тестовый проект в качестве демонстрации.

## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/-OOP-FF5733?style=flat)](https://en.wikipedia.org/wiki/Object-oriented_programming) [![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
 [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

### Что реализовано
- Регистрация пользователя
- Активация пользователя через email
- Редактирование профиля пользователя
- Авторизация уже зарегистрированного пользователя
- Создание и редактирование разделов курса
- Создание и редактирование модулей разделов
- Создание и редактирование тестов для проверки знаний под конкретный раздел курса
- Создание и редактирование вопросов на тесты с вариантами ответов


### Настройка сервиса:

- Установлены Python версии не ниже 3.11, база данных PostgreSQL
- В директории проекта создано виртуальное окружение:
    - ```python -m venv venv```
- Установлены зависимости:
    - ```pip install -r requirements.txt```
- Создана пустая БД в PostgreSQL
- Заполнен файл .env.sample (по умолчанию некоторые настройки заполнены, но изменяются в зависимости от ваших нужд) вашими настройками и после переименован в .env
- Созданы и применены миграции:
    - ```python manage.py makemigrations```
    - ```python manage.py migrate```
- Загружены тестовые данные для сервиса Happy English в качестве демонстрации:
    - ```python manage.py loaddata app_data.json```
- Запущен локальный сервер:
    - ```python manage.py runserver```

### Дополнительные настройки:

- Суперпользователь создается командой:
    - ```python manage.py csu``` и имеет следующие настройки:
        - логин: admin@mailing.com
        - пароль: 1

### Начало работы:

- Для начала работы пользователю необходимо создать либо авторизоваться под существующим аккаунтом в сервисе
- Если пользователь проходит процедуру регистрации, после заполнения формы на электронную почту пользователя поступит
  письмо со ссылкой для активации аккаунта
- Для редактирования разделов и всех данных рекомендуется создать суперпользователя по инструкции из Дополнительных настроек
- Весь CRUD осуществляется через стандартную админку Django http://localhost:8000/admin

### Логика работы системы:

- Администратором создается тематический раздел с учебными модулями
- Для каждого тематического раздела создается контрольный тест
- Пользователю доступны разделы и тесты для обучения
