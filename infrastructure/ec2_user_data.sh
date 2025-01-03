#!/bin/bash
yum update -y
yum install -y docker nginx
systemctl start docker
sudo usermod -aG docker ec2-user
systemctl enable docker
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
systemctl start nginx
systemctl enable nginx

cat <<EOT > /etc/nginx/nginx.conf
events {}

http {
    upstream grpc_backend {
        server 127.0.0.1:50051;
    }

    server {
        listen 80 http2;

        location / {
            grpc_pass grpc://grpc_backend;
            error_page 502 = /error502grpc;
        }

        location = /error502grpc {
            internal;
            default_type application/grpc;
            add_header grpc-status 14;
            add_header content-length 0;
            return 204;
        }
    }
}
EOT
systemctl restart nginx

docker run -d -p 50051:50051 medical-act-image
