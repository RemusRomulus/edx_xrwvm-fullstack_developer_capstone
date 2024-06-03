# Running Django Service
* `git clone https://github.com/RemusRomulus/edx_xrwvm-fullstack_developer_capstone.git`
* `cd edx_xrwvm-fullstack_developer_capstone/server`

## Setup Django Env
* `pip install virtualenv`
* `virtualenv djangoenv`
* `source djangoenv/bin/activate`

## Install Requirements
* `python3 -m pip install -Ur requirements.txt`

## Migrations
* `python3 manage.py makemigrations`
* `python3 manage.py migrate`
* `python3 manage.py migrate --run-syncdb`

## Run Server
* `python3 manage.py runserver`

## Populate Data
* in new shell
* from root directory: `cd edx_xrwvm-fullstack_developer_capstone/server`
* `source djangoenv/bin/activate`
* `python3 manage.py shell`
* `from dhangoproj import populate`
* `populate.initiate()`

# Building Frontend
* from root dir: `cd frontend`
* `npm install`
* `npm run build`

# Running Database Service
* from root dir: `cd database`
* `docker build . -t nodeapp`
* `docker-compose up`