# Data_Gnd
AWS Data Telemetry Scripts to be run on the GCS

## List of files and folders
* ground_data.py: Main script to be run on the GCS for launching AWS data telemetry
* ground_netcat_init.sh: Shellfile for initializing netcat, called by ground_data.py
* ground_ssh_connection.sh: Shellfile for launching an ssh session into AWS server, called by ground_data.py
* launch_GCS.sh: Launch MAVProxy and connect it over AWS Data Telemetry
