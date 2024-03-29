#!/usr/bin/env python3

'''
sbd_from_server: Receive MO msg from Rockblock web server and store it in our web server
'''

# Copyright (C) 2020, Lau Yan Han and Yonah (yonahbox@gmail.com)

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


# This script should be placed in our web server, in /usr/lib/cgi-bin

import binascii
import cgi, cgitb
import os

form = cgi.FieldStorage()

# Send respose back to Rock Seven first
print ("Content-Type:text/html\n\n")
print ("OK")

# In the final implementation, should have some form of security checks (e.g. check for whitelisted serial/imei)
rock7_whitelist = {"109.74.196.135", "212.71.235.32"}
try:
    # Get client IP address. See https://stackoverflow.com/questions/7033953/python-cgi-program-wants-to-know-the-ip-address-of-the-calling-web-page
    # Update: The above link fails for Python3.8 and Ubuntu 20.04; see this instead: https://www.tutorialspoint.com/cgi-environment-variables-in-python
    ip = os.environ["REMOTE_ADDR"]
except:
    ip = "127.0.0.1"

# Only Rock 7 IPs can access this script
if ip in rock7_whitelist:
    # Ignore incoming msgs without data feld (e.g. blank SBD msgs)
    if "data" in form.keys():
        # Transfer FieldStorage to a dictionary (for easier manipulation)
        params = {}
        for key in form.keys():
            params[key] = form[key].value
        # Write MO msg to text file. File can only hold 1 msg at a time...
        # Pre-req: Make sure apache server has read-write permissions to the file and its folder
        # See https://www.simplified.guide/apache/change-user-and-group
        # and https://stackoverflow.com/questions/33622113/python-cgi-script-permission-denied-when-writing-file
        with open("/satcomms_server/buffer.txt", 'w+') as fp:
            fp.write(str(params) + "\n")
