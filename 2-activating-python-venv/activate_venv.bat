@echo off
:: Define the path to your virtual environment folder
set venvPath="C:\path\to\venv"

:: Check if the venv folder exists and the activate.bat script is present
if exist "%venvPath%\Scripts\activate.bat" (
    echo Activating virtual environment...
    call %venvPath%\Scripts\activate.bat
    cd /d %venvPath%\..
    cmd.exe
) else (
    echo Virtual environment not found at %venvPath%
    pause
)
