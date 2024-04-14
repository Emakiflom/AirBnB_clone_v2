#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo -e "<html>\n<head>\n</head>\n<body>\n  Holberton School\n</body>\n</html>" > /data/web_static/releases/test/index.html
sudo rm - rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
