@echo off

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations app
python manage.py migrate app
python populate_app.py

pause
