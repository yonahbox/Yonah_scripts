#!/bin/bash

echo "Preparing to install"

# Create new SSH Keys and convert them to a type that can be used by paramiko
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
ssh-keygen -p -m PEM -N "" -f ~/.ssh/id_rsa

# add user to dialout group for SBD serial to work
sudo usermod -a -G $(whoami)

# source ~/.ros_bashrc file from ~/.bashrc
echo "source ~/.ros_bashrc" >> ~/.bashrc

echo "Installing required packages"
bash common/install_packages.sh -g
source ~/.ros_bashrc

echo "setting up ROS workspaces"
git clone https://github.com/yonahbox/Yonah_ROS_packages.git ~/Yonah_ROS_packages

bash common/setup_ros_ws.sh -g bonedata_ws bonesms_ws ogc_ws
source ~/.ros_bashrc

echo "Installing telegram"
bash common/telegram_build.sh -g

echo "The setup is almost complete! the only thing left is telegram"
echo "You will need access to another device running telegram with the account you want to add"
./common/telegram_auth

echo "Setup complete, restart the system to continue"