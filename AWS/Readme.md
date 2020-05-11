# AWS

Contains files that will be run on Yonah's Amazon Web Server EC2 Instance.

## Files
* **socket_server.py**: Carries out port forwarding for Data (Tech) link
* **sbd_from_server.py**: Receive Iridium Short-Burst-Data (SBD) messages from Rock Seven server
* **sbd_to_gcs.py**: Forward Iridium Short-Burst-Data (SBD) messages to Ground Control

Note that **sbd** based files should be placed in `/usr/lib/cgi-bin` folder of the web server, if apache2 is used