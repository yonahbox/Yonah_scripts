# Common Setup files

Contains setup files common to both air and ground

## List of files and folders

* **scripts**: Python scripts (syncthing and td) to assist in authenticating new devices
* **systemd**: Systemd files to help autolaunch OGC on the aircraft when it boots up
* **device_auth**: Python script to authenticate a device's telegram phone number and add it to the OGC syncthing/identifiers network
* **install_packages.sh**: Install essential packages (e.g. git, ros, tmux)
* **setup_ros_ws.sh***: Setup Yonah's ROS workspaces and packages
* **telegram_build.sh**: Builds stable version of Tdlib