Code Commit Repos
===
#### Contents

2. [ctp-switch-app-2](#ctp-switch-app-2)
3. [ctp-switch-app-1](#ctp-switch-app-1)

---

### Create new Page

#### ctp-2
1. src/views  
-> create new folder [page]  
-> 2 files:  
    1st file: `[page.vue]`
        
        <style lang="scss" scoped>
            @import '@/assets/auth.scss';
        </style>
        <template>
            [code]
        <template>
            <script lang="ts" src="./[page].ts" />            
    2nd file: `[page.ts]`
        
        import { Component, Vue, Watch } from 'vue-property-decorator';
        import { [MODEL] } from '@store/[MODEL]/model
        
        import { NS_[NAMESPACE] } from '@store/[ASDF]/types
        const AsdfModule = namespace(NS_[NAMESPACE])
        
        const 
        
        export default class [PageView] extends Vue {
            protected [page-const]: [type] = [val];
            
            protected [page-func](){
                return [return]
            }
            
        };    
        
2. /router.ts

        import [PageView] from './views/[Pageview]/[PAGE].vue'
        
        const router = new Router({
          mode: 'history',
          base: process.env.BASE_URL,
          linkActiveClass: 'active',
          routes: [{
              path: '[PAGE]',
              name: [PAGE],
              component: [Pageview],
              meta: { requiresAuth: true }
           },]
        
---

### Create New MODEL

#### ctp-2

1. src/store  
    -> create new dir [model]
    
        |[model]
        |- actions.ts
        |- getters.ts
        |- index.ts
        |- models.ts
        |- mutations.ts
        |- types.ts
    
    


---

#### ctp-switch-app-2
Frontend application -> Paired with    [ctp-switch-app-1](#ctp-switch-app-1)
* Vue
* [Ansible](#Ansible)

---
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

---
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

---
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


===

    class OrganisationSourceInvitation(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        source_organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
        destination_organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
        destination_temporary_name = models.CharField(max_length=30)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        created_on = models.DateTimeField(auto_now_add=True)
        registered = models.BooleanField(default=False)