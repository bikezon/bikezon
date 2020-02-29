# Bikezon

Django based website that will allow users to participate in an online bicycle and parts marketplace. Users will be able to create accounts, postings, browse categories and book items to buy. The marketplace will specifically focus on bikes and parts for them.

# Getting started

In order to setup the project on your local machine:

Open a terminal and change into the directory that you wish to work in (for the example this will be workspace).

Using anaconda to create virtual-env and clone repo:
```
(base)workspace$:conda create -n bikezon python=3.6.5
(base)workspace$:conda activate bikezon
(bikezon)workspace$:git clone https://github.com/bikezon/bikezon.git 
```
Using mkenv:
```
workspace$:mkvirtualenv bikezon -p python3
workspace$:workon bikezon
(bikezon)workspace$:git clone https://github.com/bikezon/bikezon.git
```

# Installing dependencies

Pip is required to install dependencies. For more information on pip and installation see:\
https://pip.pypa.io/en/stable/quickstart/

Dependencies for the project can be found in requirements.txt. To install all dependencies:
```
(bikezon)workspace$: pip install -r requirements.txt
```

# Hosting and access to website

Coming soon: pythonanywhere hosting

# Running tests

Coming soon: unit tests guide

# Built with

[Django](https://www.djangoproject.com/ "Django's Homepage") - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
