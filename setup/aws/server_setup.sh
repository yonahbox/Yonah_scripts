#!/bin/bash

# Main setup file for a new web server

echo "Extracting Data Link (Tech) file"
cp socket_server.py ~/ #@TODO: Run socket_server directly from the original folder

echo "Copying sbd files to cgi-bin"
sudo cp sbd_from_server.py sbd_to_gcs.py /usr/lib/cgi-bin

echo "Setting up OGC Systemd service"

# We need Yonah_ROS_packages repo for the Td and Syncthing python modules
git clone https://github.com/yonahbox/Yonah_ROS_packages.git ~/Yonah_ROS_packages

sudo cp systemd/ogc.service /etc/systemd/system/ogc.service
sudo cp systemd/ogc_systemd systemd/ogc_tmux systemd/ogc_admin /usr/local/bin/

./admin_auth

sudo systemctl enable --now ogc.service

echo "Server auto setup is almost done! To finish config, you need to do the following manual configurations:

1. Give your devices ssh authorisation to the server
2. Setup Apache2 service
3. Configure socket_server.py with cron

See https://github.com/yonahbox/Yonah_ROS_packages/wiki/Software-Installation for more info
"
