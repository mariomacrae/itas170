**ssh.md — week 2**  
**The key**  
Paste ls -l ~/.ssh (the permissions column matters):  
total 32  
drwx------ 2 mario.macrae mario.macrae 4096 Sep 21 17:35  agent  
-rw-rw-r-- 1 mario.macrae mario.macrae   89 Sep 10 13:31  authorized_keys  
-rw------- 1 mario.macrae mario.macrae   81 Sep 26 16:57  config  
-rw-rw-r-- 1 mario.macrae mario.macrae   81 Sep 26 17:07 'config M-M'  
-rw------- 1 mario.macrae mario.macrae  464 Sep 22 09:04  id_ed25519  
-rw-r--r-- 1 mario.macrae mario.macrae  102 Sep 22 09:04  id_ed25519.pub  
-rw------- 1 mario.macrae mario.macrae  978 Sep 21 17:00  known_hosts  
-rw-r--r-- 1 mario.macrae mario.macrae  142 Sep 21 14:28  known_hosts.old  
Which of the two files is allowed to leave this machine, and why?  
The public key file may leave your machine so the server can check if it is legitimate.  
   
**The fingerprint**  
The fingerprint ssh showed you the first time you connected to GitHub:  
256 SHA256:vT1SoBJ4ADen406r5nYwqwhknd/AWAmDaQIZeWJu3Hc mario.macrae@itas.ca (ED25519)  
I checked it with curl -s [https://api.github.com/meta](https://api.github.com/meta "https://api.github.com/meta") and it matched.  
   
**The proof**  
Paste the line GitHub answered ssh -T git@github.com with:  
Hi mariomacrae! You;ve successfully authenticated, but GitHub does not provide shell access.  
Host gh     HostName github.com     User git     IdentityFile ~/.ss  
   
   
Host gh  
HostName github.com  
User git  
IdentityFile ~/.ssh/id_ed25519  
You might want two keys on a machine in case you have separate GitHub accounts.  
