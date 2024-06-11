#!/bin/bash

# Make Migrations and Migrate the Database
echo "Making Migrations and Migrating the Database"
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py migrate --run-syncdb --noinput
python manage.py collectstatic --noinput
exec "$@"
