FROM    base/archlinux:latest
RUN     pacman --noconfirm -Syu && pacman --noconfirm -S php gnu-netcat && mkdir /tmp/www /tmp/faqin && chmod 777 /tmp/faqin
COPY    ["index.html", "/tmp/www"]
COPY    ["lel.php", "/tmp/www"]
COPY    ["lel.php.back", "/tmp/www"]
COPY    ["robots.txt", "/tmp/www"]
WORKDIR /tmp/www
USER	nobody
CMD     ["php","-S", "0.0.0.0:4646", "-t", "."]
