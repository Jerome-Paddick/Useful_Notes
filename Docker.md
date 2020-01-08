Docker
======

1. [Run](#run)
2. [Containers](#containers)
3. [Compose](#docker-compose)
4. [Explanation](#explanation)

---

### Run

cd to dir with dockerfile  
docker build .  
---> 0e8b79b08cc9

ACCESS SHELL  
docker run -it 0e8b79b08cc9 sh

---

### Containers

List Containsers -> `docker ps`
- size `-s`
- latest `-l`
- all (even stopped) `-a`
- Logs Container -> `docker logs -f [ID]`
- Kill Container -> `docker kill [ID]`
- Start Container -> `docker start [ID]`
- Stop Container -> `docker stop [ID]`
- Remove Container -> `docker rm [ID]`


Containers can exist in following states, during which the container name can't be used for another container:

- created
- restarting
- running
- paused
- exited
- dead


---

### Docker Compose

- Tool for defining and running multi-container apps
- YAML configured

---

### Explanation


     Virtual Machines    
    ¦Infrastructure(Hardware) -> Host OS -> Hypervisor -> Guest OS -> Apps/Bins/Libs¦



Hypervisor Types
1. Interfaces directly with Infrastructure's hardware (more efficient)
2. Runs as application on top of host OS (hyper-V)

Docker  
    ¦ Infrastructure(Hardware) -> Host OS -> Docker Daemon -> Apps/Bins ¦hines  
    ¦ Infrastructure(Hardware) -> Host OS -> Hypervisor -> Guest OS -> Apps/Bins¦

    Docker  
    ¦Infrastructure(Hardware) -> Host OS -> Docker Daemon -> Apps/Bins/Libs¦

DAEMON - Shares resources with host os