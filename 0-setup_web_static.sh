#!/usr/bin/env bash
# bash script which sets up web servers for deployment of web static work

# Check if user and group ubuntu exist
if ! id -u "ubuntu" > /dev/null 2>&1; then
    echo "User ubuntu does not exist"
    exit 1
fi

if ! getent group "ubuntu" > /dev/null 2>&1; then
    echo "Group ubuntu does not exist"
    exit 1
fi

# Install Nginx if it is not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create required directories if they do not already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content of /data/web_static/current/ to hbnb_static
sudo sed -i "/server_name _;/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx after updating configuration
sudo service nginx restart

