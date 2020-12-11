#!/usr/bin/env python3

from pathlib import Path
import xml.etree.ElementTree as xml
import requests as req

class Syncthing:
	def __init__(self):
		self._host = "http://localhost:8384"

		self.parse_config()

	def parse_config(self):
		home_dir = str(Path.home())
		config_path = home_dir + '/.config/syncthing/config.xml'

		if not Path(config_path).is_file():
			print("Syncthing config not found")
			print("Please rerun this file after installing syncthing")
			exit()

		root = xml.parse(config_path)
		for elem in root.iter('apikey'):
			self.api_key = elem.text

	def _post(self, url, data):
		try:
			req.post(self.host + url, headers= {
				"X-API-Key": self.api_key
			}, data=json.dumps(data))
		except req.exceptions.RequestException:
			print("syncthing post error")

	def _get(self, url):
		try:
			result = req.get(self.host + url, headers = {
				"X-API-Key": self.api_key
			})
		except req.exceptions.RequestException:
			print("synchting get error")
			return None

		return result.json()

	def add_device(self, id_n, label):
		self._post("/rest/config/devices", {
			"deviceID": id_n,
			"name": label
		})

		folder = self._get("/rest/config/folders/default")
		folder["devices"].append({
			"deviceID": id_n
		})

		self._post("/rest/config/folders", folder)