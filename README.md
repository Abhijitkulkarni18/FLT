Swagger Link: https://flt-assignment.herokuapp.com/swagger/


Base Url: https://flt-assignment.herokuapp.com/api/


Git Repository Link: https://github.com/Abhijitkulkarni18/FLT

Postman Collection APIs: https://www.getpostman.com/collections/288bc88f21a83d816d12

Postman Documentation link: https://documenter.getpostman.com/view/7497641/SztEY6Ak?version=latest

Postman Collection link : https://www.getpostman.com/collections/288bc88f21a83d816d12



Django Set-Up:

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver

Django Admin Credentials and URL:

URL: https://flt-assignment.herokuapp.com/admin/

username:abhijit

password:password


Loading Initial data:

python3 manage.py loaddata user_data.json

python3 manage.py loaddata activity_data.json


Loading Initial data in Heroku:

heroku run python3 manage.py loaddata user_data.json

heroku run python3 manage.py loaddata activity_data.json

For more info about me, please visit: https://abhijitkulkarni.herokuapp.com/ 