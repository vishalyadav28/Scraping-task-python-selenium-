# Transparency in Coverage DataScraping API



## Getting started

Install virtualenv using this

```

pip install virtualenv

```

Or refer to this URL

```

https://pypi.org/project/virtualenv/

```


## Installation

Use requirements.txt to install all dependencies

Command

if you are using LINUX machine

```
pip3 install -r requirements.txt

```

## DB

Postgres

## DB Migrations

as we already have migrations file we need to run

```

python manage.py migrate

```

to apply changes in DB

## Run project

Command

Locate manage.py file and run this command

```

python manage.py runserver

```

## Create Super user and Basic Authentication

To create super user run

```
python manage.py createsuperuser
```
then pass the cred and remember that because it will used to login admin and in Basic Auth

Example :

run 
```
python manage.py createsuperuser
```
then pass
username : admin
email : admin@company.com
password : password

## Run Django-crontab

To add crontab use this command

```
python3 manage.py crontab add

```

To show crontab use this command

```
python3 manage.py crontab show

```

To remove crontab use this command

```
python3 manage.py crontab remove

```

## Swagger url

* please create super user
* pass the basic auth before using api



Visit this url to run the api

```
http://127.0.0.1:8000/swagger/

```

