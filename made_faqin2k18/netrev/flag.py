import sys
import hashlib

# Dado un USERID, calcula la flag. El USERID es lo que se escribe en el binario

if len(sys.argv) != 2:
   print "Syntax: python2 flag.py <USERID>"
   sys.exit(0)

flag = sys.argv[1]
k = "8===D"

while (len(k) < len(flag)):
   k += k

flag2 = ""
j = 0
for i in flag:
   flag2 += chr(ord(i) ^ ord(k[j]))
   j += 1

m = hashlib.md5()
m.update(flag2)
print m.hexdigest()
