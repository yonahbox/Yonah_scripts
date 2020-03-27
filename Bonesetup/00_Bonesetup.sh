#!/bin/bash

# Full process for the initial setup of a brand new Beaglebone

##########################################

# Step 1: Install initial packages (e.g. ROS, MAVROS)

# Note that a "source" command after compiling each ROS pacakge is neccessary, so that
# the next ROS node can be overlaid over the previous one

bash 01_installpackages.sh
source /opt/ros/kinetic/setup.bash

##########################################

# Step 2: Download Yonah's ROS packages and compile them one by one

# For each ROS package, "addROSpackages.sh" is called, with the workspace and package names
# passed into the shellfile as arguments

# Again, note that the "source" command is required after each compilation,
# so as to to overlay the next ROS node over the previous one
# Failing to do so will result in some of the packages not being detected by ROS 

git clone https://github.com/yonahbox/Yonah_ROS_packages.git ~/Yonah_ROS_packages

# air_data
bash 02_addROSpackages.sh bonedata_ws air_data
source ~/Yonah_ROS_packages/bonedata_ws/devel/setup.bash

# air_sms
bash 02_addROSpackages.sh bonesms_ws air_sms
source ~/Yonah_ROS_packages/bonesms_ws/devel/setup.bash

# To add new packages, just copy the lines above and specify the workspace and package name accordingly

##########################################

#Step 3: Remove unncessary packages

bash 03_removepackages.sh

##########################################

#Step 4: setup the systemd service

bash 04_systemd_setup.sh

##########################################

echo "
Setup complete, please do the following:

1. Reload the bashrc using source ~/.bashrc
2. Add a whitelist.txt into ~/Yonah_ROS_Packages/bonesms_ws/src/air_sms/src/
3. Add the AWS Private Keys into ~/Yonah_ROS_Packages/bonedata_ws/src/air_data/src/
4. If systemd service should be enabled, run sudo systemctl enabled ros_boot.service
"