# AWS

Contains files that will be run on Yonah's Amazon Web Server EC2 Instance.

## Data Link Telemetry (Tech)

Uses the **socket_server.py** file. This file should be placed in the home folder of the AWS instance

The file writes to a DL_log.txt file to monitor the status of the telemetry link. This file can become quite large; remember to delete it every now and then after extracting the logs!

### Setup

The **socket_server.py** script should be set to autorun when the EC2 instance is initialized. This is done using chron:

* ssh into the EC2 instance, and run the command `crontab -e`
* Add the line `python socket_server.py <aircraft numbers>` into the crontab file. For example, if you wish to support Data Telemetry for Nemo4, 5 and 6, add the line `python socket_server.py 4 5 6`
* Note that this is limited to supporting 100 aircraft in total (numbered 0 to 99)

### Usage

As the script is set to autorun on each launch of the AWS EC2 instance, no additional steps are needed apart from launching the EC2.

However, each time a new aircraft is added, the crontab must be modified accordingly (see instructions above)

For instructions on operating the rest of the Data Telemetry (Tech) system, refer to the Yonah ROS packages repository (@TODO: Add more detailed instructions and provide a link)

## SBD Link (Ops)

@TODO