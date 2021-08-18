# OSCP Cheatsheet


## Network Discovery

- **nmap**

```bash
nmap -sC -sV -p- -v 192.168.1.1
```

- **responder**

```bash
responder -I eth0 -A
responder.py -I eth0 -wrf
```



