## Network Discovery

- [**nmap**](https://nmap.org/book/)

```bash
nmap -sC -sV -p- -v <target IP>
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

- [**Netdiscover**](https://github.com/alexxy/netdiscover)

```bash
netdiscover -i eth0 -r <target IP>
```
