#!/bin/bash

# This script is designed to be run on the first boot after cloning the install image onto the bone
# It should be automatically downloaded and run

# clone the repo
git clone https://github.com/yonahbox/Yonah_scripts.git ~/Yonah_scripts

# run the main installation script
cd Yonah_scripts/Bonesetup
./00_bone_setup.sh -c