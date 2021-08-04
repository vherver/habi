# Habi Backend test
## Stack used in the project
- Python 3.8
- Django
- Docker
- Mysql

## Development planning

As the first steps for the development is to adapt the project in Django to be able to use the existing tables in the database, ideally the models should be built in Django and through migrations

The entpoints will be created that will make up the API that will allow users to obtain the information from the database

[Related documentation](https://www.google.com)

##Strategy to solve the problem:

Since there is a restriction that the records in the database should not be modified, it is decided to use two databases, one that provides the information provided by Habi and the other for the Django configuration.

The models.py file was populated using the command 

```
python manage.py inspectdb
```

## Installation

The project will be wrapped in docker so it will be necessary to have docker installed and it will only be necessary to run

```
docker-compose build
docker-compose up
```
