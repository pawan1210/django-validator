# Validator

A Rest API to validate input request data.

## 🚧 Technology Stack

- **Framework** - Django Rest Framework (GenericAPIView and serializers are used)
- **Python** - version 3.8.3

## ⬇️ Installation and Run with docker

```
# clone the repository to your local machine
$ git clone https://github.com/pawan1210/django-validator.git

# navigate to the project's directory and install all the relevant dependencies
$ cd django-validator

# Run
$ docker-compose up -d --build

# Visit http://localhost:8000/ in your browser
```

## ⬇️ Installation on local host

```
# clone the repository to your local machine
$ git clone https://github.com/pawan1210/django-validator.git

# navigate to the project's directory and install all the relevant dev-dependencies
$ cd django-validator

# install dependencies
$ pip install -r requirements.txt

# Start application
$ python manage.py runserver

# Visit http://127.0.0.1:8000/ in your browser
```

## 🔨 API Endpoints

## [VIEW POSTMAN DOCUMENTATION](https://www.getpostman.com/collections/9da571a80d9840ea82f2)

| REQUEST METHODS |           ENDPOINTS            |     |
| :-------------- | :----------------------------: | --: |
| POST            | /validate/finite-values-entity |
| POST            |    /validate/numeric-entity    |

## Rules/Assumptions

1. Either supported_values or values is empty then filled and partially_filled attributes will be false.
2. Constraint for numeric entity supports [">=","<=",">","<","=="] operators.
3. Constraint can be of 2 types - "x>=5 and x<=6" and "x>=5". Meaning it can contain 1 or 2 statements. The function can be made to support n number of statements also with some tweaks.
