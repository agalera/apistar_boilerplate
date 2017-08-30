FROM nginx:latest
MAINTAINER Alberto Galera "galerajimenez@gmail.com"
#RUN mkdir /w
COPY nginx.conf /etc/nginx/nginx.conf
COPY api.conf /etc/nginx/sites-enabled/api.conf
COPY files.conf /etc/nginx/sites-enabled/files.conf
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
