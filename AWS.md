AWS
===

### Push to Staging

CHANGE ENV VARIABLES

1. ECS
2. Task Definitions
3. click on <container>
4. click on <newest>
5. Create new Revision
5. Container Definitions -> Container Image
6. in popup -> scroll to Env variables -> change -> update
7. scroll to bottom -> Create
8. ECS

If (Container doesnt hotswap )
9. Clusters
11. click on <container>
12. Tasks -> stop task
12. carry on

Else
1. Clusters -> click on service
2. update
3. Revision -> latest
4. next next next update

CLOUD API

- read docs and add env to places specified
- git push to master
- BUILD -> app 1
- edit environment
- untick [Allow AWS .......]
- Add envs to additional configuration
- Goto code, sh deploy-flask-docker-image
- BUILD
- EC2 -> CerberusLivelinkApi-staging get public IP
- lastpass shared folder -> priv key
- nano livelink_staging.pem
- copy priv key
- chmod 0600 livelink_staging.pem 
- ssh -i livelink_staging.pem ec2-user@[EC2-Instance-Public-IP]

C_ENV

- ECS 
- Task Definitions
- scroll to Containers
- Cloud API
- Edit Keys

- Build from form in frontent
- Builds from DEVELOPMENT


#### GET PEM Keys

- AWS
- System Manager
- Parameter Store

#### USERS

Agents -> centos

API -> ec2-user