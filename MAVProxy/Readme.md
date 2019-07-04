# MAVProxy

Main folder where MAVProxy will be run during flight tests/SITL testing
Note that all these instructions are for Ubuntu 16.04

## List of files and folders:

* **Alias Scripts**: Scripts for launching graphs/other modules in MAVProxy

The following are temporary holding folders for: Dataflash logs, Parameters, Telemetry Logs, and Waypoint files respectively. They are designed to allow quick access during flight testing

* **BinLogs**
* **Params**
* **Tlogs**
* **Waypoints**

## Quick Launch Files

These are complicated commands used for starting MAVProxy/SITL, abstracted into shell files to make them easy to launch. All commands are recorded in **QuickCommands.txt**.

**Running SITL on custom binary:**

* **run_quadplane_CMAC.sh**: Start quadplane SITL in CMAC
* **run_quadplane_Kompiam.sh**: Start quadplane SITL in Kompiam
* **run_quadplaneRF8_CMAC.sh**: Start quadplane SITL with Realflight8 in CMAC

Note: Please create your symbolic link to the custom arduplane binary, e.g. `ln -s <path_to_ardupilot_codebase>/build/sitl/bin/arduplane`

To learn how to create custom binary, see the following [link](https://github.com/yonahbox/ardupilot/pull/10)

**Launching MAVProxy:**

* **start_mavproxy_airwifi.sh**: Start MAVProxy over Air Wifi
* **start_mavproxy_AWS.sh**: Start MAVProxy over AWS instance
* **start_mavproxy_Nemo.sh**: Start MAVProxy over RFD connection
* **start_mavproxy_playback.sh**: Start MAVProxy over MAVPlayback
* **start_mavproxy_sitl.sh***: Start MAVProxy over custom SITL binary (see above)
* **start_mavproxy_USB.sh**: Start MAVProxy over USB connection