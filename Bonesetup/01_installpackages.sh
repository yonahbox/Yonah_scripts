#!/bin/bash

# Set up ROS and other relevant packages on Beaglebone Black
# See https://subscription.packtpub.com/book/hardware_and_creative/9781786463654/1/ch01lvl1sec12/installing-ros-in-beaglebone-black

# Step 1: Set up the local machine and the source.list file
sudo apt-get update
sudo update-locale LANG=C LANGUAGE=C LC_ALL=C LC_MESSAGES=POSIX
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros-latest.list'

# Step 2: Set up your keys
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116

# Step 3: Install ROS packages, rosdep, and add setup.bash to bashrc
sudo apt-get update
sudo apt-get install ros-kinetic-ros-base
sudo apt-get install python-rosdep
sudo rosdep init
rosdep update
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

# Step 4: Install MAVROS packages
# See http://ardupilot.org/dev/docs/ros-install.html
sudo apt-get install ros-kinetic-mavros ros-kinetic-mavros-extras
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
chmod a+x install_geographiclib_datasets.sh
bash install_geographiclib_datasets.sh
sudo apt-get install python-catkin-tools

# Step 5: Install packages to make MAVROS/ROS compatible with python3
# See https://medium.com/@beta_b0t/how-to-setup-ros-with-python-3-44a69ca36674
sudo apt-get install python3-pip python3-yaml
sudo pip3 install rospkg catkin_pkg defusedxml

# Step 6: Install non-ROS packages: htop, git, tmux and nmap (netcat)
sudo apt-get install htop git tmux nmap

# Step 7: Configure timezone to Singapore time
# See https://www.tecmint.com/set-time-timezone-and-synchronize-time-using-timedatectl-command/
timedatectl set-timezone "Asia/Singapore"