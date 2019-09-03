#!/bin/bash

# Initialise a ROS node downloaded from Yonah's Github
# The workspace and package name is specified as the 1st and 2nd arguments
# The script is not run if:
#   1. Either of the arguments are not provided
#   2. The workspace and package directories don't exist
if [ -z "$1" -o -z "$2" ]; then
    echo "Usage: bash 02_addROSpackages.sh <workspace name> <package name>.
        Make sure your workspace and package folders exist!"
elif [ ! -d "$HOME/Yonah_ROS_packages/$1" ]; then
    echo "$HOME/Yonah_ROS_packages/$1 directory not found, exiting!"
elif [ ! -d "$HOME/Yonah_ROS_packages/$1/src/$2" ]; then
    echo "$HOME/Yonah_ROS_packages/$1/src/$2 directory not found, exiting!"
else
    cd ~/Yonah_ROS_packages/$1
    catkin_make
    echo "source ~/Yonah_ROS_packages/$1/devel/setup.bash" >> ~/.bashrc
    cd src
    # Note that the below set of commands (moving air_data folder) are a "hack" to get past the "file exists" error
    # when running catkin_create_pkg. It's a very ugly method, but it works...
    mv $2 ~/
    catkin_create_pkg $2 std_msgs rospy
    mv ~/$2/* ./$2/
    rm -r ~/$2
    cd ~/Yonah_ROS_packages/$1
    catkin_make
fi