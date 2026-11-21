CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                                           NAMES
f2d7a380090b   docker:dind   "dockerd-entrypoint.…"   4 minutes ago   Up 4 minutes   2376/tcp, 127.0.0.1:23750->2375/tcp, 127.0.0.1:9080->8080/tcp   pretend-host


CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                     NAMES
02ac5809a014   mysite-web       "/docker-entrypoint.…"   4 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mysite-web-1
9a45f8740907   traefik/whoami   "/whoami"                4 seconds ago   Up 4 seconds   80/tcp                                    mysite-whoami-1

HTTP/1.1 200 OK
Server: nginx/1.31.8
Date: Mon, 16 Nov 2026 21:13:45 GMT
Content-Type: text/html
Content-Length: 461
Last-Modified: Mon, 16 Nov 2026 13:50:43 GMT
Connection: keep-alive
ETag: "6afb0a33-1cd"
Accept-Ranges: bytes

Hostname: 9a45f8740907

In this lab, 'deploy' meant that compose sent the site and dockerfile to the host, and the host in turn built the image.

