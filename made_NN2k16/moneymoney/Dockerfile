FROM    base/archlinux
COPY    ["ad_money.txt", "/root/"]
COPY    ["nn.py", "/root/"]
COPY	["miblake2.py", "/root/"]
COPY	["freq.txt", "/root/"]
RUN     pacman --noconfirm -Sy openssl python2 python2-pip ca-certificates
RUN	pip2 install base58
WORKDIR /root
CMD     ["python2", "-u", "nn.py"]
