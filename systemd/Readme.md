#Systemd integration

##ros_boot_start:

    this script is run when the service is started
    creates a new tmux session titled "roslaunch_session" and runs the required roslaunch command in that session
    should be placed in `/usr/local/bin/`


##ros_boot_stop:

    runs when the service is to be stopped 
    kills the tmux session created by ros_boot_start
    should be placed in `/usr/local/bin/`


##ros_boot.service:

    unit file required by systemd 
    this file tells systemd what scripts to run when we start the service
    should be placed in `/etc/systemd/system/`


##install.sh:

    places the files in the correct locations mentioned above
    I also included a line that would enable the unit to run when the bone boots up but it is currently commented out as this is still considered testing


##Results of my tests:

    we can establish link to AWS when the bone starts up, verified this by connecting the GCS peace as well. Peace was able to receive data from Nemo4 without any interaction with nemo4


##General info:

    We can attach to the created tmux session by running `tmux attach -t roslaunch_session`
        suggest that we add this as an alias to make it easier to attach in the future
    to enable the script to run on boot run `sudo systemctl enable ros_boot.service`
        the script does not currently run on boot
    to stop the script from running on boot run `sudo systemctl disable ros_boot.service`
    to start the service manually run `sudo systemctl start ros_boot.service`
    to stop the service run `sudo systemctl stop ros_boot.service`
    to restart the service run `sudo systemctl restart ros_boot.service`