#!/bin/bash

git clone https://github.com/yonahbox/Yonah_ROS_packages.git ~/Yonah_ROS_packages

cp systemd/ogc.service /etc/systemd/system/ogc.service
cp systemd/ogc_systemd systemd/ogc_tmux systemd/ogc_admin /usr/local/bin/

./admin_auth

sudo systemctl enable --now ogc.service
