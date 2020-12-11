#!/bin/bash

ROS_TYPE="none"

while getopts 'bg' flag
do
	case "${flag}" in
		b)
			ROS_TYPE=ros-noetic-ros-base
			;;
		g)
			ROS_TYPE=ros-noetic-desktop
			;;
	esac
done

if [[ $ROS_TYPE == "none" ]]
then
	echo "please specify if installation for bone or gcs"
	exit 1
fi

# Upgrade system packages to the latest version and install essential packages

# Upgrade existing packages
sudo apt update
sudo apt upgrade -y

# Install ROS

# Add the repos and keys
# ROS 
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# Syncthing
echo "deb https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
curl -s https://syncthing.net/release-key.txt | sudo apt-key add -

# Install ROS packages
sudo apt update
sudo apt install $ROS_TYPE python3-rosdep -y

# Configure rosdep
sudo rosdep init
rosdep update

# Add ros bash setup to user bashrc
# Note that a "source" command after compiling each ROS pacakge is neccessary, so that
# the next ROS node can be overlaid over the previous one

echo "source /opt/ros/noetic/setup.bash" >> ~/.ros_bashrc
source /opt/ros/noetic/setup.bash

# Install and configure MAVROS
sudo apt install ros-noetic-mavros ros-noetic-mavros-extras -y
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
chmod a+x install_geographiclib_datasets.sh
sudo bash install_geographiclib_datasets.sh

# Install remaining packages required for OGC
sudo apt install python3-pip python3-yaml htop tmux nmap screen python3-paramiko syncthing -y

# Install pip modules
pip3 install --user rospkg catkin_pkg defusedxml netifaces pyserial