#!/usr/bin/env python3

# Copyright (C) 2019 Lau Yan Han and Yonah (yonahbox@gmail.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''
sendSMS.py: Simple script to send SMS messages to aircraft from a terminal command.
To run this script, please specify the aircraft phone number
'''

import sys
import subprocess

class sms_send():
    
    def __init__(self, phone_no):
        self.msg = ""
        self.phone_no = phone_no # Phone number of Ground Router

    def usage(self):
        """Print help message"""
        helpmsg = """
        Message format:
        - Arm the aircraft: "arm"
        - Disarm the aircraft: "disarm"
        - Mode change: "mode <flight mode in lowercase letters>"
        - Activate regular SMS sending from aircraft (defaults to one SMS every 5 mins): "sms true"
        - Deactivate regular SMS sending from aircraft: "sms false"
        - Request for one SMS from the aircraft (useful for testing link status): "ping"
        - Request regular SMS sending in short intervals (once every 10 sec): "sms short"
        - Request regular SMS sending in long intervals (once every 5 mins): "sms long"
        - Set a specific waypoint number in an already-loaded mission file: "wp set <wp number>"
        - Load a waypoint file that is stored in the companion computer: "wp load <absolute path to waypoint file>"
        Commands are not case sensitive
        """
        print (helpmsg)
        return

    def sendcmd(self):
        """Send SMS to Ground Router, which will forward it to aircraft"""
        if not self.msg:
            return
        subprocess.call(["ssh", "root@192.168.1.1", "gsmctl -S -s '%s %s'"%(self.phone_no, self.msg)], shell=False)
        print (self.msg)
    
    def run(self):
        """Main Function. Waits for input by user, checks what type of command
        is it, then processes it to be sent as an SMS"""
        while True:
            try:
                self.msg = input("Waiting for command: ")
                if self.msg == "help":
                    self.usage()
                    continue
                self.sendcmd()
                self.msg = "" # Reset for next loop
            except (KeyboardInterrupt, SystemExit):
                print ("Shutting down")
                break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Usage: python3 sendSMS.py <phone number of Air Router>")
    else:
        sms_instance = sms_send(sys.argv[1])
        sms_instance.run()