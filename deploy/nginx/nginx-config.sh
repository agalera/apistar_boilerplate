#!/usr/bin/env bash

SERVICE_USER=${SERVICE_USER:-"root"}

cat << EOF > ${SERVICE_HOME}/conf/nginx.conf
user  ${SERVICE_USER};
worker_processes  8;

error_log  ${SERVICE_HOME}/log/error.log warn;
pid        ${SERVICE_HOME}/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       ${SERVICE_HOME}/conf/mime.types;
    default_type  application/octet-stream;

    log_format  main  '\$remote_addr - \$remote_user [\$time_local] "\$request" '
                      '\$status \$body_bytes_sent "\$http_referer" '
                      '"\$http_user_agent" "\$http_x_forwarded_for"';

    access_log  ${SERVICE_HOME}/log/access.log  main;

    sendfile        off;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include ${SERVICE_HOME}/sites/*.conf;
}
EOF
