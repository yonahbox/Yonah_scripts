#!/usr/bin/env python3

"""
File Name: ground_data.py
Date Modified: 26/07/2019
Required Scripts: ground_ssh_connection.sh, ground_netcat_init.sh

Launched by python2.7 under ground_data.launch, which performs the initialisation of a SSH connection from the ground control station (GCS) to a web server.

Includes SSH connection, NETCAT initialisation and periodic tests of connection with the web server.
"""

#Imports critical python modules
import time
import socket
import subprocess
from subprocess import PIPE

#Defines the SSH Class that handles the network connection between the ground control station and the remote web server
class SSH:

	#Initialises SSH states and attempts connection
	def __init__(self):

		self.ssh_link = False
		self.netcat_link = False
		self.ssh_linkage = ''
		self.netcat_linkage = ''

		self.ssh_attempt_connection()

	#Attempts one SSH connection. Waits for 5 seconds before any tests to allow OpenSSH to thoroughly finish the connection process
	def ssh_attempt_connection(self):	
		
		print "Attempting connection...\r\n"

		#Usage of python subprocessing to maintain an open SSH connection
		self.ssh_linkage = subprocess.Popen(['bash', '$(find', '-name', '*ground_ssh_connection.sh)'], stdout=PIPE, stderr=PIPE)
		
		time.sleep(5)	
		
		return self.ssh_link
	
	#Tests for a valid SSH connection with the web server using sockets
	def ssh_test_connection(self):

		#Attempts to connect to the running socket server on the web server
		try:			
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.connect(('localhost', 4001))
			#Send the Ground NETCAT Status			
			if self.netcat_link == True:			
				self.client.send("GROUNDNETCAT")
			else:
				self.client.send("GROUND")
			#Receives a status message from the web server
			self.from_server = self.client.recv(4096)
			self.client.close()
	
			if ("GROUND" in self.from_server) and ("AIR" in self.from_server):	
				print "Air-Server-Ground Established\r"	
				self.ssh_link = True	
			elif ("GROUND" in self.from_server) and not ("AIR" in self.from_server):
				print "Server-Ground Established, Air-Server Connection Down, Please Reconnect\r"
				self.ssh_link = True				

		except:
			print "Server-Ground Disconnected\r"
			self.ssh_link = False
			self.netcat_link = False

		self.from_server = ''

	#Initialises the NETCAT process
	def netcat_init(self):

		#Kills any existing NETCAT processes prior to opening a new one, to prevent the hogging of critical ports		
		self.netcat_list = subprocess.Popen(['pidof', 'netcat'], stdout=PIPE).stdout.read()
		self.arg = 'kill -9 ' + self.netcat_list
		subprocess.Popen([self.arg], shell=True, stdout=PIPE, stderr=PIPE)
		print "NETCAT Reset\r"	
		#Usage of python subprocessing to open a NETCAT process	
		self.netcat_linkage = subprocess.Popen(['bash', '$(find', '-name', '*ground_netcat_init.sh)'], stdout=PIPE)
		self.netcat_link = True
		print "NETCAT Initialised\r"	

	def ssh_terminate(self):
	
		self.ssh_link = False
		self.netcat_link = False
		self.ssh_linkage.kill()
		self.netcat_linkage.kill()


if __name__ == "__main__":
	
	#Creates an instance of SSH
	ssh = SSH()

	try:
		#Loops to ensure that the connection is established, otherwise, the program will continue to attempt connections with the web server until successful
		while True:

			if (ssh.ssh_link == True) and (ssh.netcat_link == False):
				ssh.netcat_init()
	
			if ssh.ssh_test_connection() == False:
				ssh.ssh_attempt_connection()

			time.sleep(1)

	except KeyboardInterrupt:
		ssh.ssh_terminate()
		print "Terminating program...\r"


