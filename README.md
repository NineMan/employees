<a href="https://github.com/psf/black">
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Описание
----------
Это приложение - реализация тестового задания на позицию python разработчика.

Задание
---------
Реализовать веб-приложение которое предоставляет один API метод 
для получения списка определенных сотрудников. 
Приложение должно быть реализовано с использованием FastAPI и MongoDB.
Список данных прикреплен в json файле.
Плюсом будет использование Docker, покрытие тестами.


#### Быстрый старт

1 Установить виртуальное окружение и запустить его

2 Скопировать себе репозитарий

```python
https://github.com/NineMan/employees.git
```

3 Установить зависимости

```python
pip install -r requirements.txt
```

4 Создать и заполнить БД данными из employees.json

```python
python load_db.py
```

5 Запуск тестов (не реализовано):

```python
pass
```

6 Запустить приложение:

```python
python app/main.py
```

#### Запуск через Docker (не реализовано)

Необходимо иметь установленные ``docker`` и ``docker-compose``

#### Маршруты

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.
Все маршруты можно посмотреть: ``/docs`` или ``/redoc``.

http://127.0.0.1:8000/docs
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
http://127.0.0.1:8000/docs

#### Вспомогательные команды для разработки:

   # Форматирование кода инструментом black (не забывать про ручной перенос строк)
   python -m black --line-length 79 app/

#### ToDo

1) Указывать файл для загрузки
2) Добавить тесты
