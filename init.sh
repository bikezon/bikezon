#!/bin/bash

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations app
python manage.py migrate app

exit 0
