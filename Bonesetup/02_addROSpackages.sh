#!/bin/bash

# Initialise a ROS node downloaded from Yonah's Github
# The workspace and package name is specified as the 1st and 2nd arguments
# Note that the last 6 set of commands (moving air_data folder) are a "hack" to get past the "file exists" error
# when running catkin_create_pkg. It's a very ugly method, but it works...
cd ~/Yonah_ROS_packages/$1
catkin_make
echo "source ~/Yonah_ROS_packages/$1/devel/setup.bash" >> ~/.bashrc
cd src
mv $2 ~/
catkin_create_pkg $2 std_msgs rospy
mv ~/$2/* ./$2/
rm -r ~/$2
cd ~/Yonah_ROS_packages/$1
catkin_make