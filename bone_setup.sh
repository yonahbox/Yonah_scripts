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
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
ssh-keygen -p -m PEM -N "" -f ~/.ssh/id_rsa

if ! $CLONEMODE
then
	# Install common common packages
	# These are already installed in the clone method
	sudo apt install vim nano wget bash-completion tcpdump
fi

# source ~/.ros_bashrc file from ~/.bashrc
echo "source ~/.ros_bashrc" >> ~/.bashrc

# Step 1: update system and install essential packages
bash common/install_packages.sh -b
source ~/.ros_bashrc

# Step 2: setup yonahs ROS packages
git clone https://github.com/yonahbox/Yonah_ROS_packages.git ~/Yonah_ROS_packages

bash common/setup_ros_ws.sh -b bonedata_ws bonesms_ws ogc_ws
source ~/.ros_bashrc

# Step 3: install systemd service
cd common
bash systemd_setup.sh
cd ..
sleep 5


# Step 4: setup telegram account
if ! $CLONEMODE
then
	bash common/telegram_build.sh -b
fi

echo "The setup is almost complete! the only thing left is telegram"
echo "You will need access to another device running telegram with the account you want to add"
./common/telegram_auth

echo "Setup complete, restart the system to continue"
echo "If the systemd service should be enabled, run \"sudo systemctl enable ros_boot.service\""
