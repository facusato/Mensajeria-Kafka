start firefox.exe http://localhost:8000/  

set "curpath=%cd%"

cd ..\template_project\

python manage.py runserver 

pause 
