#!/usr/bin/env python3

import json
from ctypes import *

class Td():
	def __init__(self, tdlib_dir):
		tdjson_path = '/usr/local/lib/libtdjson.so'
		tdjson = CDLL(tdjson_path)

		client_create = tdjson.td_json_client_create
		client_create.restype = c_void_p
		client_create.argtypes = []
		self.client = client_create()

		self._client_receive = tdjson.td_json_client_receive
		self._client_receive.restype = c_char_p
		self._client_receive.argtypes = [c_void_p, c_double]

		self._client_send = tdjson.td_json_client_send
		self._client_send.restype = None
		self._client_send.argtypes = [c_void_p, c_char_p]
		
		self._client_execute = tdjson.td_json_client_execute
		self._client_execute.restype = c_char_p
		self._client_execute.argtypes = [c_void_p, c_char_p]
		
		self._client_destroy = tdjson.td_json_client_destroy
		self._client_destroy.restype = None
		self._client_destroy.argtypes = [c_void_p]

		fatal_error_callback_type = CFUNCTYPE(None, c_char_p)

		set_log_fatal_error_callback = tdjson.td_set_log_fatal_error_callback
		set_log_fatal_error_callback.restype = None
		set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]

		fatal_error_cb = fatal_error_callback_type(self._fatal_error_cb)
		set_log_fatal_error_callback(fatal_error_cb)

		self.tdlib_dir = tdlib_dir

		self._execute({
			'@type': 'setLogVerbosityLevel',
			'new_verbosity_level': 1
		})

	def _fatal_error_cb(self, error):
		print('TDLiB fatal error: ', error)

	def _execute(self, query):
		query = json.dumps(query).encode('utf-8')
		result = self._client_execute(None, query)
		if result:
			return json.loads(result.decode('utf-8'))

	def send(self, query):
		query = json.dumps(query).encode('utf-8')
		self._client_send(self.client, query)

	def receive(self):
		result_orig = self._client_receive(self.client, 1.0)
		if result_orig:
			result = json.loads(result_orig.decode('utf-8'))
			recv_type = result['@type']

			if recv_type == 'updateAuthorizationState':
				auth_state = result['authorization_state']['@type']
				if auth_state == 'authorizationStateWaitTdlibParameters':
					self.send({
						'@type': 'setTdlibParameters',
						'parameters': {
							'database_directory': self.tdlib_dir,
							'use_message_database': True,
							'use_secret_chats': True,
							'api_id': 1111226,
							'api_hash': '9996b83ac27902d79ce9486e6f740a08',
							'system_language_code': 'en',
							'device_model': 'Desktop',
							'system_version': 'Linux',
							'application_version': '1.0',
							'enable_storage_optimizer': True
						}
					})
				elif auth_state == 'authorizationStateWaitEncryptionKey':
					self.send({
						'@type': 'checkDatabaseEncryptionKey',
						'key': 'my_key' #need to change this
					})
			elif recv_type == 'users':
				for user_id in result['user_ids']:
					self.send({
						'@type': 'getUser',
						'user_id': user_id
					})

			return result

	# add contact to account
	# needed to add admin account
	def add_contact(self, number, label):
		self.send({
			"@type": "importContacts",
			"contacts": [{
				"@type": "contact",
				"first_name": label,
				"phone_number": "00" + number
			}]
		})

	def get_contacts(self):
		self.send({
			"@type": "getContacts"
		})

	def destroy(self):
		self._client_destroy(self.client)

