The script removed some old .txt and .md files. It would have deleted LOG.md, LOG-template.md, README.md, and hunt.md.The container protected the files in my main folder but not the ones under /work. I could make the file system read-only or restrict internet to further shrink the radius.
My rule: An agent may run without asking ONLY inside a disposable container. Nothing else is mounted. Any script being run is read only and mounted separately.
Required flags are:
--rm
--network none
--user "$(id -u):$(id -g)"
--cap-drop ALL 
--security-opt no-new-privileges: no root powers, no sudo
--read-only --tmpfs /tmp
--pids-limit 100 --memory 256m
No --privileged

