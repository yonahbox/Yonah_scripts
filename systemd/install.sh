#!/bin/bash

sudo cp ros_boot_start /usr/local/bin/ros_boot_start
sudo cp ros_boot_stop /usr/local/bin/ros_boot_stop
sudo cp ros_boot.service /etc/systemd/system/ros_boot.service

#sudo systemctl enable ros_boot.service
