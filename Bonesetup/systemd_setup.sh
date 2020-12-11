#!/bin/bash

chmod +x systemd/ogc_systemd
chmod +x systemd/ogc_tmux

sudo cp systemd/ogc_tmux systemd/ogc_systemd /usr/local/bin/
sudo cp systemd/ogc.service /etc/systemd/system/ogc.service

sudo systemctl enable ogc.service

# start and enable syncthing 
sudo systemctl enable syncthing@$(whoami)
sudo systemctl start syncthing@$(whoami)