@echo off
python -m pip install --upgrade pip
pip install -r requirements.txt
cls

set /p PORT="> Server port (default 80): "
if "%PORT%"=="" set PORT=80
cls

cd src
python manage.py runserver 0.0.0.0:%PORT%
