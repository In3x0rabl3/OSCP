from pwn import *

offset = cyclic_find(0x61637561)
print(offset)
