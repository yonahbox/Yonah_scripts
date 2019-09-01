# Bonesetup

Contains scripts that will automate the initial setup of the Beaglebone Black Companion Computer. The installation steps are found [in this guide](https://subscription.packtpub.com/book/hardware_and_creative/9781786463654/1/ch01lvl1sec12/installing-ros-in-beaglebone-black)

There are four main tasks to be performed during the initial setup (minus the hardware setup component):

1. Flashing the SD card and inserting it into the Beaglebone
2. Installing ROS, MAVROS and other neccessary packages
3. Adding ROS packages from [Yonah_ROS_Packages](https://github.com/yonahbox/Yonah_ROS_packages.git)
4. Removing unnecessary packages

Steps 2 - 4 can be automated using scripts in this folder

## Bone setup procedure

* Follow the installation steps mentioned in [in the above guide](https://subscription.packtpub.com/book/hardware_and_creative/9781786463654/1/ch01lvl1sec12/installing-ros-in-beaglebone-black)
* Note that When booting up for the first time in SD card (and pressing F2 button), you need to wait for a few minutes before you can ssh into the bone
    * To learn how to ssh into the Bone over USB, refer to the following [link](https://www.dummies.com/computers/beaglebone/how-to-connect-your-beaglebone-via-ssh-over-usb/).
* Make sure the Bone is connected to the Internet (through a LAN cable connected to a router) before installing packages
* Follow the steps in the guide up to and including the part where you add "restricted" to sources.list (i.e. `sudo vi /etc/apt/sources.list` followed by `deb http://ports.ubuntu.com/ubuntu-ports/ xenial main restricted universe multiverse`, etc)
    * Note: There is no need to do the memory re-partitioning step mentioned in the guide
* Afterwards, use the scripts in this folder to automate the rest of the setup process. Download the Bonesetup folder, copy it into the Bone's root folder (using `scp` command), and run the 00_Bonesetup script with `bash 00_Bonesetup.sh`
    * Note: Make sure all the scripts in this folder are copied to the same location in the Beaglebone (e.g. all located in the Bone's root folder)
* Respond "Yes" or enter password whenever the system prompts you to do so
* After the script is complete, carry out the following:
    * Reload the .bashrc with `source ~/.bashrc` so that the ROS packages can be recognised
    * Add a whitelist file (with the title `whitelist.txt`) into `~/Yonah_ROS_Packages/bonesms_ws/src/air_sms/src/` location in the Beaglebone, so that air_sms can use it to recognise whitelisted phone numbers. Refer to the air_sms [Readme](https://github.com/yonahbox/Yonah_ROS_packages/tree/master/bonesms_ws) on instructions on how to setup `whitelist.txt`
    * Add the AWS Private Keys into `~/Yonah_ROS_Packages/bonedata_ws/src/air_data/src/` location in the Beaglebone, so that air_data can use it to connect to the AWS instance
* Note that all of Yonah's ROS packages will be located in the `~/Yonah_ROS_Packages` folder