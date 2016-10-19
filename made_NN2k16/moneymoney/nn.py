#!/usr/bin/env python

import SocketServer as ss
import os
from binascii import hexlify
from random import randint
from datetime import datetime
import miblake2
import urllib2
import json
import random
import base58
import uu
import StringIO
import string
import base64
import urllib2
import re

#Flag: 8===D{Enc0ders_D0_N0t_G1v3_R34l_Secur1ty_But_S3cret_Shar1ng_M4ybe_D03s}

FLAG = "YEAH! 8===D{Shamir(2-00124TdmxdOWx6fO3Ju/OPaW1kutWmNKsWrhLxH2W+T7R4QfQ/+NzDebCfTltfTKbgukGlR4yweJn3UW1qw2s5TBCnSQUw=)}"
btc_addr = []
tips = [
        "I saw Dr. Utonium reading Phrack many times.",
        "Last week Dr. Utonium bought this to clean his lab -> https://www.logismarket.com.ar/maxtel-mazzoni/lustradora-rotativa/2767179405-1247658963-p.html",
        "Dr. Utonium thinks that Craig Wright is not who claims to be. What do you think about that?",
        "Dr. Utonium does not like b64. Too mainstream, he says :/",
	"\n 0 | 0 |  0 \n 0 | 1 |  1 \n 1 | 0 |  1 \n 1 | 1 |  0 \nIn many cases, that\'s more an obfuscation than an encryption...",
        "Secret sharing is undervalued :(",
	"Normally, Dr. Utonium uses always the same hint for himself, as he can\'t remember when it\'s right or not.",
	"I stole that for you <3 buttercup{D1D_Y0U_KNOW_BL4KE2?_ME_NEITHER}",
	"As you saw, Dr. Utonium is a big fan of The Lord of the Rings."
]

def rot43(s):
    rot_43 = string.maketrans(
        " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        "KLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJ")
    return string.translate(s, rot_43)

def call_mojo():
    msg = '\n\nAuto-attaching to session 2...\nirssi | MojoJojo@CP3kc2.F5htj.virtual (Ka0chat)\n<+MojoJojo> Hi my little minion! I have info that can be useful for you. I don\'t know when, but I\'m sure you are going to need what I found last month sniffing Utonium\'s communications: 1-000O4LkoDev88CEhevvRqbVSc/Fbh+BS47N0NL0jUoQneR9/Ah+yoYr3qDxzlHJ3EI0MITTz4kCwmxHdKye02rjZIMmduk=. I don\'t know what it means...:_S'
    f = open('freq.txt','r')
    freq = int(f.read())
    f.close()
    if randint(0,100) < freq+1:
        msg += "\nYou\'re lucky! I have got more data for you! " + tips[randint(0,len(tips)-1)]
    msg += "\nDetaching...\n"
    return msg

def peticion(arg):
    try:
        r = urllib2.urlopen('http://blockchain.info/address/' +arg + '?format=json&limit=0')
        return r.read()
    except:
        print "Error detected"
        return "500"

def balance(s):
    r = peticion(s)
    while r == "500":
        time.sleep(1)
        r = peticion(s)
    parse = json.loads(r)
    return parse["final_balance"]

class Handler(ss.StreamRequestHandler):

    def handle(self):
        put = self.wfile.write

        challenge = hexlify(os.urandom(3))######[:5]
        put('\nWelcome to the Dr. Utonium computer! As he usually says, passwords are out-of-style nowadays. So I\'m going to test if you\'re my lovely boss through crypto challenges that only him can solve <3\n\nFirst of all, let\'s fight fire with fire. BLAKE2B(X) = %s. Let me know X. Hint: my $X =~ ^[0-9a-f]{6}$\nSolution: ' % miblake2.BLAKE2b(challenge).hexdigest().strip())
	print "input: " + challenge
        response = self.rfile.readline()[:-1]
        if response != challenge:
            put('You\'re a cheater! Get out of here, now.\n')
            return
        random.seed(datetime.now())
	o_challenge = btc_addr[randint(0,len(btc_addr)-1)]
	challenge = hexlify(base58.b58decode(o_challenge))
        challenge = "Iep! Next! FINAL! " + challenge[::-1]
        key = "ANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZANDYRLZ"
        x_challenge = ''
        for x in range (0,len(challenge)):
            x_challenge += str(ord(challenge[x])^ord(key[x])) + ','
        challenge = "Iep! Next! " + x_challenge.rstrip(',')
	outf = StringIO.StringIO()
        inf = StringIO.StringIO(challenge)
        uu.encode(inf, outf)
        challenge = "Iep! Next! " + outf.getvalue()
        challenge = "Iep! Next! " + rot43(challenge)
        challenge = base64.b16encode(challenge)
        put(call_mojo())
        put('\nHmmm...ok, here is your challenge. Hint: !yenom eht em wohS\n\n' + challenge + "\n\nSolution: ")
	
        challenge = balance(o_challenge)
        print " --- " + str(challenge*0.00000001)
        sol = self.rfile.readline().strip()
        if (len(sol)>15) or (not re.match('^[0-9]+\.[0-9]+$', sol)):
            put('You\'re a cheater! Get out of here, now.\nHint: ^[0-9]+\\.[0-9]+$\n')
            return
        if float(sol) != float(challenge*0.00000001):
            put('You\'re a cheater! Get out of here, now.\n')
            return
        put('%s\n' % FLAG)
        print " ^^^ Right!"


class ReusableTCPServer(ss.ForkingMixIn, ss.TCPServer):
    allow_reuse_address = True


if __name__ == '__main__':
    HOST, PORT = ('0.0.0.0', 1337)
    with open('ad_money.txt') as fp:
        for line in fp:
            btc_addr.append(line.rstrip())
    ss.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer((HOST, PORT), Handler)
    server.serve_forever()
