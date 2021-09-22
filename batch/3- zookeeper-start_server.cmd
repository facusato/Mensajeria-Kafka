set "curpath=%cd%"

cd %curpath%

cd ..\kafka\bin\windows

zookeeper-server-start.bat ..\..\config\zookeeper.properties

pause


