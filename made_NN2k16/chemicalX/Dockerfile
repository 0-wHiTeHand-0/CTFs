FROM    base/archlinux
COPY	["lshell", "/root/lshell/"]
RUN	pacman --noconfirm -Rsc nano vi && pacman --noconfirm -Sy archlinux-keyring && pacman --noconfirm -Syu python2

RUN	useradd -N -m -u 1001 -s /usr/bin/lshell nope
RUN	rm /home/nope/.bash*
COPY	["hint.txt", "/home/nope/hint.txt"]
RUN	chown nope /home/nope/hint.txt
RUN	chmod -R 777 /home/nope/

RUN	useradd -N -m -u 1000 noruas
RUN	echo "nn6ed{RSA_w0rks_Gr34t_1f_You_Us3_It_Pr0perly}" > /home/noruas/flag.txt
RUN	echo "cat flag.txt" > /home/noruas/.your_history
RUN	chown noruas /home/noruas/flag.txt /usr/bin/more /home/noruas/.your_history
RUN	chmod -R 500 /home/noruas/
RUN	chmod u+s /usr/bin/more

WORKDIR /root/lshell
RUN	python2 setup.py install --no-compile --install-scripts=/usr/bin/
RUN	rm /etc/lshell.conf && export TERM=xterm
COPY	["lshell.conf", "/etc/lshell.conf"]
RUN	chmod 444 /etc/lshell.conf
USER	nope
CMD     ["/usr/bin/lshell"]
