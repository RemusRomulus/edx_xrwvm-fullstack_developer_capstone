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

## Update Settings.py
* Check URL of application
* Make sure it's added to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in `settings.py`

## Populate Data
* in new shell
* from root directory: `cd edx_xrwvm-fullstack_developer_capstone/server`
* `source djangoenv/bin/activate`
* `python3 manage.py shell`
* `from djanagoapp import populate`
* `populate.initiate()`

# Building Frontend
* from root dir: `cd frontend`
* `npm install`
* `npm run build`

# Running Database Service
* from root dir: `cd database`
* `docker build . -t nodeapp`
* `docker-compose up`

# Sentiment Analyzer Service
## Cloud Engine Setup
* Setup Cloud "Code Engine" Application
  * In "Cloud" tab, select "Code Engine"
  * Select the "Create Project" button
    * Code Engine will take time in "Preparing"
    * Once prepared, press "Code Engine CLI"

## Microservice Setup
* from root directory: `cd edx_xrwvm-fullstack_developer_capstone/server/djangoapp/microservices`
* `docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer`
* `docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer`
* `ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000`
* Connect to the URL that is generated to access the microservices and check if the deployment is successful.
* If the application deployment verification was successful, attach /analyze/Fantastic services to the URL in the browser to see if it returns positive
* Open djangoapp/.env and replace your code engine deployment url with the deployment URL you obtained above.
  * It is essential to include the / at the end of the URL. Please ensure that it is copied
  * `sentiment_analyzer_url=your code engine deployment url`
* Get the URL for the sentiment analyzer app: `ibmcloud ce application list`

# Setting a Cleaner Prompt
* `export PS1="\e[1;34m\$ \e[1;31m\! \e[4;32m\W>\e[0m"`
  * Reference: https://phoenixnap.com/kb/change-bash-prompt-linux