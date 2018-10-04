#! /bin/bash

# A script that automates the reconstruction of the entire database.
rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell < init.py

# Create a superuser account.
USER='admin'
PASS='admin'
EMAIL='admin@326.edu'
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$USER', '$EMAIL', '$PASS')" | python3 manage.py shell
echo "===================================================================="
echo "The database has been setup with the following credentials:

username: $USER
password: $PASS
email: $EMAIL

You will need to use the username '$USER' and password '$PASS' to
login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

$ python3 manage.py runserver 0.0.0.0:8080"
echo "===================================================================="

