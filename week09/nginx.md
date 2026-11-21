nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

nginx: [emerg] unexpected "}" in /etc/nginx/conf.d/default.conf:21
nginx: configuration file /etc/nginx/nginx.conf test failed

**curl -sI -H 'Accept-Encoding: gzip' http://localhost:8080:**
HTTP/1.1 200 OK
Server: nginx/1.31.8
Date: Mon, 16 Nov 2026 17:33:26 GMT
Content-Type: text/html
Content-Length: 461
Last-Modified: Mon, 16 Nov 2026 13:50:43 GMT
Connection: keep-alive
ETag: "6afb0a33-1cd"
Accept-Ranges: bytes

**curl -s http://localhost:8080/nothere:**
<!doctype html>
<.html lang="en">
<.head><.meta charset="utf-8"><.title>Not here<./title><./head>
<.body>
  <.h1>404 — not here<./h1>
  <.p>My own error page, served by my own server block.</.p>
<./body>
<./html>

**curl -s http://localhost:8080/docs/**
<!doctype html>
<.html lang="en"><.head><.meta charset="utf-8"><.title>Docs<./title><./head>
<.body><.h1>Docs<./h1><.p>Runbooks will live here.<./p><./body><./html>
 
 try_files $uri $uri/ =404; tells ngnix to do a left-to-right search until it finds the correct file or folder named docs.
