import sys

#Se le pasa la flag deseada, y devuelve lo que hay que escribir en el binario. CUIDADO CON LAS BACKSLASHES; hay que escaparlas

if len(sys.argv) != 2:
   print "Syntax: python2 flag.py <FLAG>"
   sys.exit(0)

flag = sys.argv[1]
i = 0
j = len(flag)-1
l = j

flag2 = ""

while (i<l+1):
   if i <= l/2:
      c = 7
   else:
      c = 10
   flag2 += chr(ord(flag[j])+c)
   i = i+1
   j = j-1

print flag2
