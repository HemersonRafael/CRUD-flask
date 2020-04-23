# CRUD-flask
## Begin by using pip to install Pipenv and its dependencies:

    pip install pipenv

## Create the directory with the name of the project:

    mkdir CRUD-flask && cd CRUD-flask

## Init project with pipenv:

    pipenv install

##### Normally it is created two files  Pipfile and Pipfile.lock, in the directory of the project. If need specific version of the python  is necessary to use the flags --two or --three.

### Activate the project virtual environment with the following command

    pipenv shell

### Installing Project Dependencies

    pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt

### Installing Development Dependencies
    
    pipenv install pylint --dev
### Acess the postgreSQL
    sudo -u postgre psql
### Create the database
    CREATE DATABASE blog_api_db;
### Create user 
    CREATE USER apiflask WITH PASSWORD '123456';
### Grant privileges on database to user
    GRANT ALL PRIVILEGES ON DATABASE "blog_api_db" to apiflask;
### Set the environment variable
    bash setEnvVariables.sh
    In my case: zsh setEnvVariables.sh
### Running the project
    python run.py
check the execution in the browser through the link http://127.0.0.1:5000/ 

### Run migrations initialization
    python manage.py db init

### Populate our migrations files and generate tables 
    python manage.py db migrate

### Apply the changes to the db
    python manage.py db upgrade
    