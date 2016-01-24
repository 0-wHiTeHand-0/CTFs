import struct
import os
import hashlib
from binascii import hexlify
import socket
import itertools

serv='bringthenoise.insomnihack.ch'
port=1111
buffer2=1024
POWLEN=5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serv, port))
sock.send('')
data = sock.recv(buffer2)[12:17]
print "Hash to process: %s" % data
rdata=0
while (hashlib.md5(str(rdata).encode('ascii')).hexdigest().strip()[:5] != data):
	rdata=rdata+1
print "Success! %s" % str(rdata).encode('ascii')
sock.send(str(rdata).encode('ascii')+'\n')
data = sock.recv(buffer2)
data = data + sock.recv(buffer2)

coefs = data.split('\n')
coefs = coefs[0:-2]

eq = [map(lambda x: int(x), e.split(', ')) for e in coefs]
print "eq:"
print eq

for s in itertools.product(range(8), repeat=6):
    allok = True
    for e in eq:
        result = sum(s[i]*e[i] for i in range(6)) % 8
        thisok=False
        for v in [-1,0,1]:
            thisok = thisok or (e[6] == (result + 8 + v) % 8)
        allok = allok and thisok
    if allok:
        print "PWNZ"
        print s
	sock.send(str(s)[1:-1]+'\n')
	data = sock.recv(buffer2)
	print data
	break
sock.close()
