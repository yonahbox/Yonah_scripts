#!/usr/bin/env python3

# Copyright (C) 2019 Seah Shao Xuan, Lau Yan Han, and Yonah (yonahbox@gmail.com)

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

"""
File Name: ground_data.py
Required Scripts: ground_ssh_connection.sh, ground_netcat_init.sh

Launched by python3, which performs the initialisation of a SSH connection from the ground control station (GCS) to a web server.
Includes SSH connection, NETCAT initialisation and periodic tests of connection with the web server.
"""

#Imports critical python modules
import time
import socket
import subprocess
from subprocess import PIPE
import sys

#Defines the SSH Class that handles the network connection between the ground control station and the remote web server
class SSH:

	#Initialises SSH states and attempts connection
	def __init__(self):

		self.air_link = False
		self.ground_link = False
		self.netcat_link = False
		self.ssh_linkage = ''
		self.netcat_linkage = ''

		self.ssh_attempt_connection()

	#Attempts one SSH connection. Waits for 5 seconds before any tests to allow OpenSSH to thoroughly finish the connection process
	def ssh_attempt_connection(self):	
		
		print ("Attempting connection...\r\n")

		port_1 = (10 * int(sys.argv[1])) + 4000
		port_2 = port_1 + 1
		port_3 = port_1 + 2

		#Usage of python subprocessing to maintain an open SSH connection
		self.ssh_linkage = subprocess.Popen(['bash $(find -name *ground_ssh_connection.sh) '+str(port_1)+' '+str(port_2)+' '+str(port_3)], shell=True, stdout=PIPE, stderr=PIPE)
		
		time.sleep(5)	

		while self.ssh_test_connection() == False:			
			None			
	
	#Tests for a valid SSH connection with the web server using sockets
	def ssh_test_connection(self):

		#Attempts to connect to the running socket server on the web server
		try:			
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.connect(('localhost', 4001))
			if self.netcat_link == True:			
				self.client.send("GROUNDNETCAT".encode())
			else:
				self.client.send("GROUND".encode())
			#Send the Ground NETCAT Status
			self.from_server = self.client.recv(4096)
			self.client.close()

			cur_time = "[" + str(time.time()) + "]"
	
			if ("GROUND".encode() in self.from_server) and ("AIR".encode() in self.from_server):	
				print (cur_time + " Air-Server-Ground Established\r")
				self.air_link = True
				self.ground_link = True	
			elif ("GROUND".encode() in self.from_server) and not ("AIR".encode() in self.from_server):
				print (cur_time + " Server-Ground Established, Air-Server Connection Down, Please Reconnect\r")
				self.air_link = False
				self.ground_link = True				

		except:
			# @TODO: Catch specific exceptions
			cur_time = "[" + str(time.time()) + "]"
			print (cur_time + " Server-Ground Disconnected\r")
			self.air_link = False
			self.ground_link = False
			self.netcat_link = False
			time.sleep(2)
			return False

		self.from_server = ''

	#Initialises the NETCAT process
	def netcat_init(self):

		#Kills any existing NETCAT processes prior to opening a new one, to prevent the hogging of critical ports	
		self.netcat_list = subprocess.Popen(['pidof', 'netcat'], stdout=PIPE).stdout.read()
		self.arg = 'kill -9 ' + self.netcat_list.decode()
		#Usage of python subprocessing to open a NETCAT process
		subprocess.Popen([self.arg], shell=True, stdout=PIPE, stderr=PIPE)
		print ("NETCAT Reset\r")
		self.netcat_linkage = subprocess.Popen(['bash $(find -name *ground_netcat_init.sh)'], shell=True, stdout=PIPE)
		self.netcat_link = True
		print ("NETCAT Initialised\r")

	def ssh_terminate(self):
	
		self.air_link = False
		self.ground_link = False
		self.netcat_link = False
		self.ssh_linkage.kill()
		self.netcat_linkage.kill()

if __name__ == "__main__":

	#Creates an instance of SSH
	ssh = SSH()

	#Launches mavProxy. To-do: This feature currently is broken as we can't input commands into MavP
	#subprocess.Popen(['mavproxy.py', '--master=udp:localhost:5001'], stdout=PIPE, stderr=PIPE)

	try:
		#Loops to ensure that the connection is established, otherwise, the program will continue to attempt connections with the web server until successful
		while True:

			
			if ssh.ssh_test_connection() == False:
				ssh.ssh_attempt_connection()

			if (ssh.ground_link == True) and (ssh.netcat_link == False):
				ssh.netcat_init()
				
			time.sleep(1)

	except KeyboardInterrupt:
		ssh.ssh_terminate()
		print ("Terminating program...\r")


