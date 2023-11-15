#  Проект «Web-приложение для определения заполненных форм.»

## Описание проекта:

Проект позволяет определить заполненую форму и вернуть ее название.

## В проекте были использованы технологии:
Django REST
Python 3.9
Gunicorn
MnogoDB
Docker

## Как запустить проект:


Клонируйте с GitHub проект и перейдите в директорию проекта.
``` 
git@github.com:VladimirChernyy/Web-app-validate-form.git

cd Web-app-validate-form
``` 

Создаем файл .env по примеру .env.example

``` 
sudo nano .env
```

Соберите и запустите контейнеры в фоновом режиме
```
sudo docker compose -f docker-compose.yaml up --build -d
```
Примените миграции
```
sudo docker compose -f docker-compose.yaml exec web python manage.py migrate
```
Загрузите данные в базу данных
```
sudo docker compose -f docker-compose.yaml exec web python manage.py load_data
```

## Примеры запросов:

```
request POST:
$ http://127.0.0.1:8000/api/v1/get_form/?phone=+7 888 882 22 22&email=jane.doe@example.com

response: "Шаблон формы 14"

request POST:
$ http://127.0.0.1:8000/api/v1/get_form/?phone=+7 888 882 12 22&email=jane.doe@example.com

response:
            {
                "field_name1": "phone",
                "field_name2": "email"
            }
```

## Над проектом работал:
[Vladimir Chernyy](https://github.com/VladimirChernyy)
