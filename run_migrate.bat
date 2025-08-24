@echo off

python -m pip install --upgrade pip
pip install -r requirements.txt
cls

cd src
python manage.py migrate
