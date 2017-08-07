import base64
import re

fname = 'out.txt'

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

with open(fname) as f:
    content = f.readlines()
    res = []
    strings = []
    content = [i for i in content if i.find('php') > 0]
    caca = ""
    for i in content:
        s1 = find_between(i, 'php?', '&L4bry1nth')
        s2 = find_between_r(i, '?', '-')
        concat = s1 + s2
        concat_reverse = concat[::-1]
        b64_concat = base64.b64decode(concat_reverse)
	i = b64_concat.count('317')
        b64_concat = b64_concat.replace('317', '')
	strings.append(b64_concat)
    for i in range(0, len(strings[0])):
	for j in range (0,len(strings)):
		regexp = re.compile('[a-zPADN{}0-9]')
		if regexp.search(strings[j][i]) is not None:
			print strings[j][:-1]
