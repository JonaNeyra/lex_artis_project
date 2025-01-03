#!/bin/bash
yum update -y
yum install -y docker nginx git
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

cd /tmp
git clone https://github.com/JonaNeyra/lex_artis_project.git
sudo mkdir /var/opt medical_act
sudo cp -R /tmp/lex_artis_project/medical_act /var/opt/medical_act
sudo chown -R www-data:www-data /var/opt/medical_act

docker build -t medical-act-image /var/opt/medical_act
docker run -d -p 50051:50051 medical-act-image
