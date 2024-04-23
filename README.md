
### Тестовое задание для компании Anverali:


### Задача:
#### `Необходимо создать сайт с админ панелью и 2-мя кабинетами на Flask или Django. Сайт может быть не оформлен красиво. Структура на выбор. Можно взять за основу сайт kwork.ru. На сайте помимо админки должны быть два кабинета заказчика и исполнителя. Минимальный набор полей в профилях (имя, контактные данные, опыт). БД PostgreSQL`




### Стэк технологий:
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

- Django - 5.0.4
- Djangorestframework - 3.15.1
- Python - 3.11
- Docker

  

### Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
git clone git@github.com:ipoderator/anvilari_sites.git
```
```
python3.11 -m venv venv 
```
```
. ./venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3.11 -m pip install --upgrade pip
```
Создаем Суперпользователя:
```
python manage.py createsuperuser
```
Устанавливаем зависимости:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3.11 manage.py migrate
```
Запустить проект:
```
python3.11 manage.py runserver
```

### Так жe можно собрать из Docker:

- Собираем базу данных:
```
docker-compose up -d
```
- Собираем образ:
```
docker build -t anverali_sites .
```
- Запускаем контейнер:
```
docker run -p 8000:8000 anverali_sites
```

Команды для проверки:

```
api-core/registration/ 

api-core/customer_profile/slug/ 

api-core/performer_pofile/slug/

api-core/search_vacancies/

api-auth/login/

api-auth/logout/
```


### Автор:
<div id="header" align="center">  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>  </div>


- [Чуркин Глеб](https://github.com/ipoderator)