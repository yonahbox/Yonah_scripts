#!/bin/bash

CLONEMODE=false

while getopts 'hc' flag
do
	case "${flag}" in
		h) 
			echo "This script simplifies the inital setup of the beaglebone"
			echo "It installs ROS and builds all the packages from the Yonah_ROS_packages repository"
			echo "Usage:"
			echo -e "\t-h: Show this help screen"
			echo -e "\t-c: Clone mode, use this flag if the system was installed by cloning the master image"
			exit
			;;
		c)
			CLONEMODE=true
			;;
	esac
done

echo "Congratulations on your new install, Please wait while the system is being setup"
echo "You may be asked to enter the password several times in this process"

# Create new SSH Keys and convert them to a type that can be used by paramiko
if $CLONEMODE
then
	ssh-keygen -t rsa -N ""
	ssh-keygen -p -m PEM =f ~/.ssh/id_rsa
else
	sudo apt install vim nano wget bash-completion tcpdump
fi

# Step 1: update system and install essential packages
bash 01_install_packages.sh

# Step 2: setup yonahs ROS packages
git clone https://github.com/yonahbox/Yonah_ROS_packages.git ~/Yonah_ROS_packages

bash 02_setup_ros_ws.sh bonedata_ws bonesms_ws ogc_ws

# Step 3: install systemd service
bash 03_systemd_setup.sh

# Step 4: setup telegram account
if ! $CLONEMODE
then
	bash 04_telegram_build.sh
fi

echo "The setup is almost complete! the only thing left is telegram"
echo "You will need access to another device running telegram with the account you want to add"
./telegram/tele_auth

echo "Setup complete, restart the system to continue"
echo "If the systemd service should be enabled, run \"sudo systemctl enable ros_boot.service\""
