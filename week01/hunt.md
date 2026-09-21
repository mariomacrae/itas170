
   
6. Cmd: grep '" 404 ' access.log | cut -d' ' -f7 | sort | uniq -c | sort -nr  
   
82 /wp-login.php  
   
 Wp-login.php produced 82 404s.  
   
 The php files are paths exclusive to wordpress, and the automatic scanning traffic is redirecting the users to them.  
   
7. Cmd: sort -t' ' -k10,10nr access.log | head -1  
   
Path: 112.106.51.88 - - [10/Sep/2026:08:08:01 -0700] "GET /downloads/itas170-lab1.pdf HTTP/1.1" 200 2097152 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) AppleWebKit/605.1.15 Safari/17.6"  
   
2097152  bytes  
   
8. Cmd: grep -c "Googlebot" access.log  
   
335 from Googlebot, 374 when 'bot' is searched. These numbers differ  because   
of the file robots.txt.  
   
9. Cmd: grep -c "12/Sep/2026" access.log  
   
744 requests happened on September 12th.  
   
     10.  Cmd: grep -c '"POST /wp-login.php ' access.log  
132 in total, 45 containing login  
   
   
