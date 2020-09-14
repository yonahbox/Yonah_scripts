#!/bin/bash

# Initialize ROS workspace from Yonahs git repository
# Expects a list of workspace names seperated by a space

# Keep track of original directory to return there after script completes
origin=$(pwd)

# Note that a "source" command after compiling each ROS pacakge is neccessary, so that
# the next ROS node can be overlaid over the previous one

for ws in "$@"
do
	# Ensure the directory exists
	if [ ! -d  ~/Yonah_ROS_packages/$ws ]
	then
		echo "Workspace not found, exiting"
	else
		cd ~/Yonah_ROS_packages/$ws
		catkin_make -DCATKIN_BLACKLIST_PACKAGES="rqt_mypkg"
		echo "source ~/Yonah_ROS_packages/$ws/devel/setup.bash" >> ~/.bashrc
		source ~/Yonah_ROS_packages/$ws/devel/setup.bash
	fi
done

# Return to original working directory
cd $origin
