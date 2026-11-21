# The deployable image: nginx, our configuration, our site — all baked in,
# so the SAME image runs on this laptop and on the Docker host. Nothing is
# bind-mounted at deploy time; a folder on your machine does not exist on
# a machine that is not yours.
FROM nginx:alpine
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/
COPY nginx/.htpasswd /etc/nginx/.htpasswd
EXPOSE 80
