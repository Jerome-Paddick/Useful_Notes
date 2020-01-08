Code Commit Repos
===
#### Contents

1. [ctp-switch-agent-1](#ctp-switch-agent-1)
2. [ctp-switch-app-2](#ctp-switch-app-2)
3. [ctp-switch-app-1](#ctp-switch-app-1)
4. [ctp-mts-dd]()
5. [ctp-sts-vtiger-1](#ctp-sts-vtiger-1)
6. [ctp-livelink-recordingapp-2](#ctp-livelink-recordingapp-2)
7. [ctp-livelink-iosapp1](#ctp-livelink-iosapp1)
8. [ctp-livelink-integration-zixi-2](#ctp-livelink-integration-zixi-2)
9. [ctp-livelink-integration-zixi-1](#ctp-livelink-integration-zixi-1)
10. [ctp-livelink-recordingapp-1](#ctp-livelink-recordingapp-1)

---
#### ctp-switch-agent-1

Python Modules
* [pika](#pika) = “~=1.1.0”
* requests = “*”
* [pytz](#pytz) = “*”
* [influxdb](#pytz) = “*”
* [boto3](#boto3) = “*”
* [python-dotenv](#dotenv) = “*”

---

#### ctp-switch-app-2
Frontend application -> Paired with    [ctp-switch-app-1](#ctp-switch-app-1)
* Vue
* [Ansible](#Ansible)

#### Run
1. cd to root dir
2. `npm install`
3. create local env called `.env.development.local`


---

#### ctp-switch-app-1
   Dockerised Backend application, paired with [ctp-switch-app-2](#ctp-switch-app-2)

ECR  
Dockerised Backend -> Nginx Server -> Django Framework  
Ansible -> Deploy AWS

* Docker
* [Ansible](#Ansible)
* Django

### Quickstart
1. docker-compose up
2. 

Run

- docker build .
- docker run -it [ImageName] sh
- To activate this project's virtualenv, run `pipenv shell`.
Alternatively, run a command inside the virtualenv with `pipenv run`.
- RUN `pipenv run python manage.py collectstatic --no-input`
 ---> Running in d87570dd9cdb
- `python manage.py migrate`
- `python manage.py runserver`
- `python manage.py runserver 0.0.0.0:8000`

Compose

- docker-compose up

---


### Glossary

<a name="Ansible"></a>
### 	 ~ANSIBLE~
* App deployment automation


#### pika
- py implementation of AMQP0-9-1 protocol
- [docs](https://pika.readthedocs.io/en/stable/https://pika.readthedocs.io/en/stable/)
- [AMQP 0-9-1 Model Explained — RabbitMQ](https://www.rabbitmq.com/tutorials/amqp-concepts.html)
- *Advanced Message Queuing Protocol*
- message published to "exchanges” which distributes it to queues, using rules (bindings), with predefined metadata
Broker delivers messages to consumers subscribed to queues or consumer can fetch messages directly, exchange is opaque to broker

#### pytz
- timezone database
- [homepage](https://pythonhosted.org/pytz/https://pythonhosted.org/pytz/)

#### influxdb 
- Time seris database
[Getting Started with Python and InfluxDB | InfluxData](https://www.influxdata.com/blog/getting-started-python-influxdb/)


#### boto3
 - AWS SDK (Amazon Web Services Software Development Kit)
- [Boto 3 Documentation — Boto 3 Docs 1.10.46 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- can make requests and process responses from AWS Services


#### dotenv 
- reads key-val pair from .env file and adds to environment variable
- [python-dotenv · PyPI](https://pypi.org/project/python-dotenv/)

#### ECR
- *ELASTIC CONTAINER REGISTRY*
- Docker container registry
- Store, Manage and deploy docker containter images
- Used to run containers in [ECS](#ecs) and [EKS](#eks)

#### ECS
- *ELASTIC CONTAINER SERVICE*
- Select Container Images
  - -> launch [EC2](#ec2) instances
  - -> manage containers

#### EKS
- *ELASTIC KUBERNETES SERVICE*
- Kubernetes manages clusters of [EC2](#ec2) instances and runs containers on those instances
- 

#### EC2
- *ELASTIC CLOUD COMPUTE*
- resizable capacity computing instance
