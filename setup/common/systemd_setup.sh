#!/bin/bash

# Set up ogc systemd service on the aircraft, so that ogc can autostart when aircraft boots up

chmod +x systemd/ogc_systemd
chmod +x systemd/ogc_tmux

sudo cp systemd/ogc_tmux systemd/ogc_systemd /usr/local/bin/
sudo cp systemd/ogc.service /etc/systemd/system/ogc.service

sudo systemctl enable ogc.service

# start and enable syncthing 
sudo systemctl enable --now syncthing@$(whoami)