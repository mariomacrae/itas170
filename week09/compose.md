NAME              IMAGE            COMMAND                  SERVICE   CREATED             STATUS             PORTS
week09-web-1      week09-web       "/docker-entrypoint.…"   web       8 seconds ago       Up 8 seconds       0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
week09-whoami-1   traefik/whoami   "/whoami"                whoami    About an hour ago   Up About an hour   80/tcp

/api/ output:
Hostname: 948ad318b9d8
IP: 127.0.0.1
IP: ::1
IP: 172.18.0.2
RemoteAddr: 172.18.0.3:43944
GET / HTTP/1.1
Host: localhost
User-Agent: curl/8.18.0
Accept: */*

Whoami resolves inside compose because it automatically creates a bridge network with an embedded DNS server. It does not resolve inside standalone because docker containers attach to the default bridge network.

The compose file builds an image instead of mounting the site folder because building an image creates a self contained and unchangeable container, whereas mounting the folder is better for live editing.

