# Bikezon

Django based website that will allow users to participate in an online bicycle and parts marketplace. Users will be able to create accounts, postings, browse categories and book items to buy. The marketplace will specifically focus on bikes and parts for them.

## Getting started

In order to setup the project on your local machine:

Open a terminal and change into the directory that you wish to work in (for the example this will be workspace).

Using anaconda to create virtual-env and clone repo:

```shell
(base)workspace$:conda create -n bikezon python=3.6.5
(base)workspace$:conda activate bikezon
(bikezon)workspace$:conda install pip
(bikezon)workspace$:git clone https://github.com/bikezon/bikezon.git
```

You can use any other virtual environment if you would prefer to.

## Installing dependencies and initialising the project

Dependencies for the project can be found in requirements.txt.

In order to setup the project on windows:

```shell
(bikezon)workspace$:start init.bat
```

And let the batch file run. After it is done you can close it. This will install all dependencies, initialise the database and populate the database.
This also creates a super user:

```shell
username: admin
password: admin
```

In order to setup the project on linux:

```shell
(bikezon)workspace$: ./init.sh
```

The script will do the same thing as on the windows version.

All dependencies are installed **inside of your virtual environment** - so there is no need to use the --user flag unless you are setting up the project outside of a virtual environment (not reccommended).

To run the project locally use:

```shell
python manage.py runserver
```

And go to [Local host](127.0.0.1:8000 "127.0.0.1:8000") in your browser.

## Hosting and access to website

Coming soon: pythonanywhere hosting

## Running tests

Coming soon: unit tests guide

## Built with

[Django](https://www.djangoproject.com/ "Django's Homepage") - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

[Django Boostrap 4](https://pypi.org/project/django-bootstrap4/ "Bootstrap support for Django projects") - Bootstrap support for Django projects.
