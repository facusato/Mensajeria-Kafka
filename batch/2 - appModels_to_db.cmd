set "curpath=%cd%"

cd ..\template_project\

python manage.py makemigrations template_app 

python manage.py migrate template_app 

pause 
