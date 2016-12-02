FROM    base/archlinux
COPY	["lshell", "/root/lshell/"]
RUN	pacman --noconfirm -Rsc nano vi && pacman --noconfirm -Sy archlinux-keyring && pacman --noconfirm -Syu python2 && useradd -N -m -u 1001 -s /usr/bin/lshell nope && rm /home/nope/.bash*
COPY	["hint.txt", "/home/nope/hint.txt"]
RUN	chown nope /home/nope/hint.txt && chmod -R 777 /home/nope/ && useradd -N -m -u 1000 noruas && echo "nn6ed{RSA_w0rks_Gr34t_1f_You_Us3_It_Pr0perly}" > /home/noruas/flag.txt && echo "cat flag.txt" > /home/noruas/.your_history && chown noruas /home/noruas/flag.txt /usr/bin/more /home/noruas/.your_history && chmod -R 500 /home/noruas/ && chmod u+s /usr/bin/more

WORKDIR /root/lshell
RUN	python2 setup.py install --no-compile --install-scripts=/usr/bin/ && rm /etc/lshell.conf && export TERM=xterm
COPY	["lshell.conf", "/etc/lshell.conf"]
RUN	chmod 444 /etc/lshell.conf
USER	nope
CMD     ["/usr/bin/lshell"]
