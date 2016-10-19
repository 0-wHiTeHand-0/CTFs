#!/bin/bash
if [ $(docker ps -a|wc -l) -gt 50 ]; then
	echo "It's a party hard! Too much people at home! Try again in 30 seconds plz..."
	else
docker run -it --rm --network=none --log-driver=syslog --log-opt labels=ctfRSA --log-opt syslog-address=udp://127.0.0.1:55778 crypto2_img
	fi
exit
