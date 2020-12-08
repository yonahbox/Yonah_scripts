#!/bin/bash

# sudo cp systemd/ros_boot_start /usr/local/bin/ros_boot_start
# sudo cp systemd/ros_boot_stop /usr/local/bin/ros_boot_stop
# sudo cp systemd/ros_boot.service /etc/systemd/system/ros_boot.service

# sudo chmod +x /usr/local/bin/ros_boot_start
# sudo chmod +x /usr/local/bin/ros_boot_stop

#sudo systemctl enable ros_boot.service

chmod +x systemd/ogc_systemd
chmod +x systemd/ogc_tmux

sudo cp systemd/ogc_tmux systemd/ogc_systemd /usr/local/bin/
sudo cp systemd/ogc.service /etc/systemd/system/ogc.service

#sudo systemctl enable ogc.service