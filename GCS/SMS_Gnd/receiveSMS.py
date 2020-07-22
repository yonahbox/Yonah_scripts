#!/usr/bin/env python3

# Copyright (C) 2019, Lau Yan Han and Yonah (yonahbox@gmail.com)

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
Simple script to read SMS messages from aircraft and display them on console

Lau Yan Han and Yonah, July 2019
'''

import subprocess
import datetime
import logging

class sms_receive():

    def readSMS(self):
        '''
        Takes in SMS from Ground RUT955 and display it on the terminal
        '''
        
        # Set up a logger that logs all messages (including debug msgs) to a file called receivedSMS.log
        logging.basicConfig(filename="receivedSMS.log", level=logging.DEBUG)
        
        # Set up a second logger to print directly to the terminal. Ignore debug msgs
        printtoterminal = logging.StreamHandler()
        printtoterminal.setLevel(logging.INFO)
        logging.getLogger('').addHandler(printtoterminal)

        logging.info("Waiting for SMS")
        
        while True:
            try:
                received_raw = subprocess.check_output(["ssh", "root@192.168.1.1", "gsmctl -S -r 1"], shell=False)
                received = received_raw.decode()

                if 'no message' in received:
                    continue

                self.msg = (received.splitlines()[4]).split(' ',1)[1] #Extract message (5th line, excluding 1st word)
                logging.info(datetime.datetime.now())
                logging.info(self.msg)

                subprocess.call(["ssh", "root@192.168.1.1", "gsmctl -S -d 1"], shell=False) # Delete message in RUT

            except (IndexError):
                logging.warn("I received a junk message")
            
            except (subprocess.CalledProcessError):
                logging.warn("SSH process into router has been killed")
            
            except (KeyboardInterrupt, SystemExit):
                logging.info("Shutting down")
                logging.shutdown()
                break

if __name__ == "__main__":
    sms_instance = sms_receive()
    sms_instance.readSMS()