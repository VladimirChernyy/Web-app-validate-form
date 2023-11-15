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



 Настраиваем Docker
``` 
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin;
``` 
Клонируйте с GitHub проект и перейдите в директорию проекта.
``` 
git@github.com:VladimirChernyy/taski-docker.git

cd taski-docker
``` 

Создаем файл .env, в котором нужно указать данные

``` 
sudo nano .env
```
Добавьте в файл .env код  

```
POSTGRES_DB=<Желаемое_имя_базы_данных>
POSTGRES_USER=<Желаемое_имя_пользователя_базы_данных>
POSTGRES_PASSWORD=<Желаемый_пароль_пользователя_базы_данных>
DB_HOST=db
DB_PORT=5432
```

Соберите и запустите контейнеры в фоновом режиме
```
sudo docker compose -f docker-compose.yml up -d
```
Примените миграции
```
sudo docker compose -f docker-compose.yml exec backend python manage.py migrate
```
Соберите статику
```
sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic
```

Создайте суперпользователся
```
sudo docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```

![main.yml](https://github.com/VladimirChernyy/foodgram-project-react/actions/workflows/main.yml/badge.svg)

## Над проектом работал:
[Vladimir Chernyy](https://github.com/VladimirChernyy)