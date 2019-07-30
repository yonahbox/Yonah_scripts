#!/usr/bin/env python3

'''
Simple script to read SMS messages from aircraft and display them on console

Lau Yan Han and Yonah, July 2019
'''

import subprocess
import datetime

class sms_receive():

    def readSMS(self):
        '''
        Takes in SMS from Ground RUT955 and display it on the terminal
        '''
        print("Waiting for SMS")
        while True:
            try:
                received_raw = subprocess.check_output(["ssh", "root@192.168.1.1", "gsmctl -S -r 1"], shell=False)
                received = received_raw.decode()

                if 'no message' in received:
                    continue

                self.msg = (received.splitlines()[4]).split(' ',1)[1] #Extract message (5th line, excluding 1st word)
                print(datetime.datetime.now())
                print(self.msg)

                subprocess.call(["ssh", "root@192.168.1.1", "gsmctl -S -d 1"], shell=False) # Delete message in RUT

            except (IndexError):
                print ("I received a junk message")
            
            except (KeyboardInterrupt, SystemExit):
                print ("Shutting down")
                break

if __name__ == "__main__":
    sms_instance = sms_receive()
    sms_instance.readSMS()