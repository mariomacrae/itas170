Volumes.md

1. File does not exist inside the plain container. In the named volume, the file has landed in docker's storage at the mountpoint. In a bind mount, the file is in my folder. 
In the plain container, the file does not show because the container is built from scratch. It writes the file inside one container, reads it, and deletes it because of the --rm flag.
2. In the named volume scenario, naming the volume tells docker to manage the storage area internally so you don't have to worry about where your project files are located.
3. For the bind mount scenario, the file is in the folder because the directory was created before telling docker to create the file. The note is owned by root (default user) because the container shares my linux kernel. This tells me that docker shares my linux kernel and i need sudo permissions to delete the file.
