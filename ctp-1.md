Cerberus
==========

# Requirements

## Python

You need python3.5 and python3.5-dev installed on your system. Installing `python3` from your package manager installs either 3.5 or a newer version. If you don't have 3.5 installed and need to compile it from source, you can:

  - download the source from `https://www.python.org/downloads/source/` (the 3.5 tgz archive)

  - update your packages
```
sudo apt-get update
```

  - install the tools needed to build Python
```
# For apt-based systems (like Debian, Ubuntu, and Mint)
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev  libncursesw5-dev xz-utils tk-dev

# For yum-based systems (like CentOS)
sudo yum -y groupinstall development
sudo yum -y install zlib-devel
```

  - build Python
```
tar xvf Python-3.5.6.tgz
cd 
./configure --enable-optimizations --with-ensurepip=install
make -j 8
sudo make altinstall # to make sure you don't overwrite your system Python
``` 

  - check that Python was correctly built using `python3.5 -V`

## Pipenv

We're using `pipenv` to create a python virtual environment and install the required dependencies.

If you don't have `pipenv` installed globally on your local system, you can install it using pip (if you don't have pip and didn't follow the step above, `sudo apt-get install python3-pip`)

```
pip3 install pipenv
```

# Setup

Enter the `switch/switch` directory. (this should be the default unless something different is mentioned below).

```
pipenv install
```

If you don't have postgres installed locally, you can run it through docker
and create the persistent volume in the current folder:


To build the python container run:
```
docker-compose build --no-cache python
```

```
docker-compose up -d postgres
```

## Using pipenv

To start the python env, use:
```
pipenv shell
```

If you want to install other dependencies, use the following command and commit the new
Pipfile and Pipfile.lock files generated:

```
pipenv install <example-dependency>
```

## Running the migrations

Make sure you are in the `switch/switch` directory.

To run the initial migrations, use:
```
python manage.py migrate
```

If you make changes to the models, run the following to generate and migrate the migrations
```
python manage.py makemigrations
python manage.py migrate
```

# Using the app in development

Make sure you are in the `pipenv shell` or prefix the commands below with `pipenv run`.

## Starting the app:
```
python manage.py runserver
```

To start listening on a different ip / port (or all IPs using 0.0.0.0) you can run the following command (and replace the ip/port as you wish)

```
python manage.py runserver 0.0.0.0:8000
```

## Creating a superuser

If you used a fresh postgres install, you might want to create a superuser, you can do this using:
```
python manage.py createsuperuser
```

## Notes
  - The development config has `*` as the `ALLOWED_HOSTS` by default, so you should be able to access it with any host/ip

## Base URLs

  - Swagger docs at `http://ip:port/api/scheduler/schemas`.
  - Django admin at `http://ip:port/admin`.

# Editing configuration files

The configs are located in `switch/switch/config`, `development.py` and `production.py`, and they extend the common `base.py` in the same folder.

By default, manage.py will use `development.py` (overridable through the `DJANGO_SETTINGS_MODULE` environment variable).

The `python-decouple` package makes using configs easier, they can be overridden through a local `.env` or `settings.ini` file, or in the local environment (environment takes precedence).

## Environment Variables

> You can find a full list of environment variables in example.env

`SQL_ENGINE` - Database engine, defaults to `django.db.backends.postgresql_psycopg2`

>Must be one of `django.db.backends.postgresql_psycopg2`, `django.db.backends.postgresql`, `django.db.backends.mysql`, `django.db.backends.sqlite3`, `django.db.backends.oracle`

`SQL_DATABASE` - Database name, defaults to `postgres`

`SQL_USER` - Database username, defaults to `postgres`

`SQL_PASSWORD` - Database password, defaults to `postgres`

`SQL_HOST` - Database host, defaults to `localhost`

`SQL_PORT` - Database port, defaults to `5432`

`SECRET_KEY` - The application secret key

`LOGS_PATH` The application logs path, defaults to `switch/Logs`


# Testing

Tests should be created in a TDD fashion. To facilitate running tests, there is the `pytest` with `pytest-django` package that watches the tests for changes and runs them again.

You can start the tests with this package (in the pipenv shell, in `switch/switch`) using:
```
py.test -f
```

The tests are structured based on this layout:
```
- tests
    - integration
        - test_<integration test 1>.py
        - ...
    - unit
        - test_<unit test 1>.py
        - ...
```

# Deploying the app in production

To run daphne, enter the `switch/switch` directory and run
```
pipenv run daphne -b 0.0.0.0 -p 8080 asgi:application
```

You can use any process manager but pm2 is preferred.
To manage the process using pm2 (npm install -g pm2), run
```
pm2 start --name switch "pipenv run daphne -b 0.0.0.0 -p 8080 asgi:application"
```

Environment variables can be setup using a .env file or by passing them when starting pm2
```
SQL_HOST=12.34.56.78 SQL_USER=postgres SQL_PASSWORD=postgres pm2 start --name switch "pipenv run daphne -b 0.0.0.0 -p 8080 asgi:application"
```

You can view the status of the process by running
```
pm2 show switch
```

You can view the process logs by running
```
pm2 logs switch
```

To stop the process run 
```
pm2 stop switch
```

### Below is an example NGINX configuration:

```
server {
    listen 80;
    server_name ip_or_domain;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/switch/static_dir;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://0.0.0.0:8080;
    }
}
```

# Deploying the app using docker

The docker compose file will run NGINX, Postgres and Python containers.
```
docker-compose up
```

To stop the docker containers run
```
docker-compose down
```

To run in detached mode
```
docker-compose up -d
```

> Once the docker containers are running, the application will be available on the ip of the machine running docker on port 80
> For example, if you are running docker on your local machine you can visit http://127.0.0.1:80
> If you are running docker inside a virtual machine you can visit http://<ip of vm>:80


To run one of the containers, pass the name of the container (nginx, postgres or python)
`docker-compose up postgres`

To remove the postgres container and its data in case of migration issues during development
```
docker rm -f -v  postgres
```

To nuke everything (including volumes!! be careful), run:
```
docker-compose down -v
```

## Migrations and fixtures

To run the migrations inside the docker container:

```
./docker-migrate.sh
```

To load the fixtures run:
```
./docker-load-fixtures.sh
```

## Interacting with python inside the container

To create a superuser inside the container or run management commands,  first enter a shell by running:
```
docker exec -it python /bin/sh
```

Then inside the container:
```
cd /srv/www
pipenv shell
cd switch/switch/
```

You can then run Django management commands:
```
python manage.py createsuperuser
```
You can exit the pipenv shell by typing `exit` then, to exit the container type `exit` again

##Rabbit MQ
Start the RabbitMQ container.
```
docker-compose up rabbitmq
```


Download the rabbitmq_delayed_message_exchange plugin from community plugins:
  -https://www.rabbitmq.com/community-plugins.html
  -Currenly using rabbitmq ver 3.7.x
  -https://www.rabbitmq.com/blog/2015/04/16/scheduling-messages-with-rabbitmq/

Connect to the rabbitMQ container to interact.
```
docker exec -it rabbitmq /bin/sh
cd /opt/rabbitmq/plugins
wget https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
unzip rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
rm rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
```
Enable the management plugin, so that it can be accessed from a web browser
```
rabbitmq-plugins enable rabbitmq_management
```

Go to the rabbitmq management console:
 -http://blah:15672
 -user:guest
 -pass:guest
 
Declare and configure the required queues
```
rabbitmqadmin declare exchange name="switch-zixi" type="x-delayed-message" arguments={/"x-delayed-type/":/"direct/"}
```



Enable the plugins
```
rabbitmq-plugins enable rabbitmq_management
```


# Environment Variables

`SQL_ENGINE` - Database engine, defaults to `django.db.backends.postgresql_psycopg2`

>Must be one of `django.db.backends.postgresql_psycopg2`, `django.db.backends.postgresql`, `django.db.backends.mysql`, `django.db.backends.sqlite3`, `django.db.backends.oracle`

`SQL_DATABASE` - Database name, defaults to `postgres`

`SQL_USER` - Database username, defaults to `postgres`

`SQL_PASSWORD` - Database password, defaults to `postgres`

`SQL_HOST` - Database host, defaults to `localhost`

`SQL_PORT` - Database port, defaults to `5432`

`SECRET_KEY` - The application secret key

`LOGS_PATH` The application logs path, defaults to `switch/Logs`

# Permissions

Information on the permissions system can be found in [switch/switch/permissions/README.md](switch/switch/permissions/README.md)



### Deploying to AWS

Set environment variables outline in example.env

```
pipenv run ./ansible-deploy.sh
```

# Updating Ansible server with latest ansible deploy scripts

rsync -PaXe "ssh -i ~/.ssh/ansible_rsa" --include=ansible-deployment/*** --include=ansible-deploy.sh --exclude="*" ./ ubuntu@<ansible-server-ip>:switch-api