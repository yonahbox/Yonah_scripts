# AWS

Contains files that will be run on Yonah's Amazon Web Server EC2 Instance

## Overall setup

The setup of AWS is managed by the `server_setup.sh` file. Copy this folder into the AWS instance (either through scp or git clone) and run the file. See the [documentation](https://github.com/yonahbox/Yonah_ROS_packages/wiki/Software-Installation#server-side-installation) for more details.

> **Note**: The server setup script has not been tested on an actual server yet. We welcome feedback and bug reports

The next sections give an overview of the files and folders in this section:

## Systemd

Contains files to configure OGC service in systemd on the server.

* **ogc.service**: Main service file that will be copied into systemd's working directory. Calls `ogc_systemd`
* **ogc_systemd**: Generate a tmux session and run `ogc_tmux` within it. This file should be in `/usr/local/bin`
* **ogc_tmux**: Export paths of necessary python modules and run the `ogc_admin` python script. This file should be in `/usr/local/bin`
* **ogc_admin**: Main python script that will always run on the server, to perform identifiers handling for the OGC. This file should be in `/usr/local/bin`

## Admin Auth

The **admin_auth** python script authenticates a telegram phone number for usage on the server. 

## SBD Link (Ops)

* **sbd_from_server.py**: Receive Iridium Short-Burst-Data (SBD) messages from Rock Seven server
* **sbd_to_gcs.py**: Forward Iridium Short-Burst-Data (SBD) messages to Ground Control

## Data Link Telemetry (Tech)

Uses the **socket_server.py** file. It should be set to to autorun using cron when the EC2 instance is launched. See the [documentation](https://github.com/yonahbox/Yonah_ROS_packages/wiki/Software-Installation#data-link-tech-script) on how to setup.

Each time a new aircraft is added, the crontab must be modified accordingly (see instructions in the above link)

@TODO: Switch from cron to systemd to standardize with rest of our software.