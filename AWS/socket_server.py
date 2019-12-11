#!/usr/bin/env python2.7

import time
import socket
import multiprocessing
import subprocess
import sys

class aircraft:
	
	def __init__(self):		
	
		self.air_conn = ''
		self.air_addr = ''
		self.ground_conn = ''
		self.ground_addr = ''
		self.air_ack = multiprocessing.Queue()
		self.ground_ack = multiprocessing.Queue()
		self.status = []

	def aircraft_name(self, name):
		self.name = name

	def socket_init(self, a, b):
		self.s_air = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s_air.bind(('localhost', a))
		self.s_ground = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s_ground.bind(('localhost', b))	

	def air_sock_ping(self):
		
		self.s_air.listen(1)	
		self.air_conn, self.air_addr = self.s_air.accept()
		self.air_ack.put(self.air_conn.recv(4096))
		self.air_conn.send(str(self.status))

	def ground_sock_ping(self):

		self.s_ground.listen(1)		
		self.ground_conn, self.ground_addr = self.s_ground.accept()
		self.ground_ack.put(self.ground_conn.recv(4096))
		self.ground_conn.send(str(self.status))

	def per_second(self):		

		self.air_ack = multiprocessing.Queue()
		self.ground_ack = multiprocessing.Queue()

		self.processes = [multiprocessing.Process(target=self.air_sock_ping), multiprocessing.Process(target=self.ground_sock_ping)]

		for p in self.processes:
			p.start()

		for p in self.processes:
			p.join(1)

		for p in self.processes:
			p.terminate()	

		self.status = []

		try:		
			self.status.append(self.air_ack.get(timeout=0.1))			
		except:
			self.status.append('')
			
		try:		
			self.status.append(self.ground_ack.get(timeout=0.1)) 		
		except:
			self.status.append('')		


def log_status(live_aircraft, aircraft_status):

	for a in live_aircraft:

		if ("AIR" in a.status) and (("GROUND" in a.status) or ("GROUNDNETCAT" in a.status)):	
			aircraft_status.append([a.name, "A---S---G"])
		elif ("AIR" in a.status) and not (("GROUND" in a.status) or ("GROUNDNETCAT" in a.status)):
			aircraft_status.append([a.name, "A---S-x-G"])			
		elif not ("AIR" in a.status) and (("GROUND" in a.status) or ("GROUNDNETCAT" in a.status)):
			aircraft_status.append([a.name, "A-x-S---G"])
		else:
			aircraft_status.append([a.name, "A-x-S-x-G"])

	print (aircraft_status)

	log_file = open("DL_log.txt", "a")
	log_file.write("["+str(time.asctime(time.localtime()))+"] ")
	for s in aircraft_status:
		log_file.write("NEMO"+str(s[0])+": "+str(s[1])+", ")
	log_file.write("\n")
	log_file.close()

live_aircraft = []

for arg in sys.argv[1:]:
	a = aircraft()
	a.aircraft_name(arg)
	a.socket_init(4000+(10*int(arg)), 4001+(10*int(arg)))
	live_aircraft.append(a)

while True:
	
	aircraft_processes = []
	aircraft_status = []
	
	for a in live_aircraft:
		aircraft_processes.append(multiprocessing.Process(target=a.per_second()))

	for a in aircraft_processes:
		a.start()
	
	for a in aircraft_processes:
		a.join(2)

	for a in aircraft_processes:
		a.terminate()
	
	log_status(live_aircraft, aircraft_status)
	

