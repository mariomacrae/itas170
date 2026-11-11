Hello from Docker!  
   
 This message shows that your installation appears to be working correctly.  
NAME="Alpine Linux"  
   
 ID=alpine  
   
 VERSION_ID=3.20.10  
   
 PRETTY_NAME="Alpine Linux v3.20"  
   
 HOME_URL="https://alpinelinux.org/"  
   
 BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"  
7.0.0-38-generic  
   
 ac304f71ed1e893e7cb4cc50ed02263666203d916f5c8f851b22f775edef7a56  
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                     NAMES  
   
 ac304f71ed1e   nginx:alpine   "/docker-entrypoint.…"   43 seconds ago   Up 42 seconds   0.0.0.0:8080->80/tcp, \[::\]:8080->80/tcp   web  
curl -I http://localhost:8080  
   
 HTTP/1.1 200 OK  
   
 Server: nginx/1.31.8  
   
 Date: Mon, 02 Nov 2026 18:26:22 GMT  
   
 Content-Type: text/html  
   
 Content-Length: 896  
   
 Last-Modified: Wed, 21 Oct 2026 17:54:44 GMT  
   
 Connection: keep-alive  
   
 ETag: "6ad8fc64-380"  
   
 Accept-Ranges: bytes  
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES  
50x.html  
   
 index.html  
Server: nginx/1.31.8  
   
 Date: Mon, 02 Nov 2026 18:26:22 GMT  
   
 Content-Type: text/html  
   
 Content-Length: 896  
   
 Last-Modified: Wed, 21 Oct 2026 17:54:44 GMT  
   
 Connection: keep-alive  
   
 ETag: "6ad8fc64-380"  
   
 Accept-Ranges: bytes  
The two uname-r command proved what version of linux the computer was running. The difference between --rm and stop/rm is that —rm automatically cleans up the container’s file system and works better for smaller tasks, and stop/rm manually halts the container before deleting it.  
