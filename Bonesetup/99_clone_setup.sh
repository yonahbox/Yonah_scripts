#!/bin/bash

# This script is designed to be run on the first boot after cloning the install image onto the bone
# It should be automatically downloaded and run

# clone the repo
git clone https://github.com/yonahbox/Yonah_scripts.git ~/Yonah_scripts

# temporary requirements while scripts are not in master
cd Yonah_scripts
git checkout clone

# run the main installation script
cd Bonesetup
./00_bone_setup.sh -c