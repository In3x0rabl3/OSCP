# OSCP Cheatsheet


## Network Discovery

- [**nmap**](https://nmap.org/book/)

```bash
nmap -sC -sV -p- -v 192.168.1.1
```

- [**responder**](https://github.com/SpiderLabs/Responder)

```bash
responder -I eth0 -A
responder.py -I eth0 -wrf
```

- [**Bettercap**](https://www.bettercap.org/)

```bash
bettercap -X --proxy --proxy-https -T <target IP>
```



