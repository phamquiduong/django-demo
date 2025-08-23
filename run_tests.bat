@echo off

call run_pip_install.bat
cls

pytest -v src
