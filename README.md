# qmm_rdbms
Django project for Quantum Matter Mapping using a Relational Database

Setting up the DB

    sudo apt-get update
    sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

    sudo su - postgres
    psql

    CREATE DATABASE qmm;
    CREATE USER qmmuser WITH PASSWORD 'qmm';

    ALTER ROLE qmmuser SET client_encoding TO 'utf8';
    ALTER ROLE qmmuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE qmmuser SET timezone TO 'UTC';

    GRANT ALL PRIVILEGES ON DATABASE qmm TO qmmuser;
    
    \q
    exit
    sudo pip install virtualenv

To use the virtual environment, use: 

     source qmmenv/bin/activate

Start the environment, and install Django with Postgres' adapter to the project directory

    pip install django psycopg2
  
Connect the app to Postgres:

    cd ~/qmm_rdbms
    python manage.py makemigrations
    python manage.py migrate
  
 Then make a superuser for the baked in Django admin:
 
      python manage.py createsuperuser
  
 The app can be started by running:
 
      python manage.py runserver
    
    
 Then visiting localhost:8000 in a browser window.
 The baked in admin can be visited by going to localhost:8000/admin and logging in with the credentials you generated previously.
 



