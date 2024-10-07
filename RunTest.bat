cd "%~dp0"
call .\.venv\Scripts\activate.bat
pytest .\Tests -n auto 
pause