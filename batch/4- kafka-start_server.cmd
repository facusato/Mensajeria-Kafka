set "curpath=%cd%"

cd %curpath%

cd ..\kafka\bin\windows

kafka-server-start.bat ..\..\config\server.properties

pause