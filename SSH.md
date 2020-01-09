SSH
===

### OPEN SSH TUNNEL

`-L` local port forwarding - open as local user on remote system

    ssh -L [local_port]:[remote_address]:[remote_port] [username@server.com]


---
### Basic Use

    ssh [USER] -p [port]
    graphical
    ssh -X 

to find ip of machine 
ap a
over internet
https://ifconfig.co/ip

access this machine
    
    sudo systemctl stop ssh
    sudo systemctl start ssh

diable/enable on start 

    sudo systemctl disable ssh
    sudo systemctl enable ssh
