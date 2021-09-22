set "curpath=%cd%"

cd ..\template_project\

python manage.py makemigrations 

python manage.py migrate 

pause 
