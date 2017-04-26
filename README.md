# djcasemg ; 
#author:@wq4121@126.com
A python django project
this project implements the following functions:
interface information recode,
send interface request,
interface cases recode,
associate cases and interface,
the recodes may contain  add/delete/update/query/clone operations

 
before you running this project ,you should reference mysql configuration information in the file setting.py ,make sure the database is accessible. 
and run these command in the project root path:  "python manage makemigrations" ; "python manage migrate"
at last run this command to start django server: "python manage.py runserver 0.0.0.0:8080" ,open browser to access the address:localhost:8080/interfapp/intfcf