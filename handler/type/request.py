import requests
from stringToBytes import *
from i2cManager import *

from handler.type.handler import AbstractInstructionHandler
from handler.operation.client import OperationClient

class RequestModifiers():
	def __init__(self, parameters_source, operations):
		self.parameters_source = parameters_source
		self.operations = operations

class ResponseModifiers():
	def __init__(self, parameters_source, operations):
		self.parameters_source = parameters_source
		self.operations = operations

class RequestInstruction():
	def __init__(self, url, method, headers = None, parameters = None, request_modifiers = None, response_modifiers = None):
		self.http_request = HTTPRequest(url, method, headers, parameters)
		if request_modifiers:
			self.request_modifiers = RequestModifiers(**request_modifiers)
		if response_modifiers:
			self.response_modifiers = ResponseModifiers(**response_modifiers)

class HTTPRequest():
	def __init__(self, url, method, headers = None, parameters = None):
		self.url = url
		self.headers = headers
		self.parameters = parameters
		self.method = method

	def is_get(self):
		if self.method == 'GET':
			return True
		else:
			return False

	def is_post(self):
		if self.method == 'GET':
			return True
		else:
			return False

class Network():
	def do_request(self, request: HTTPRequest):
		parameters = {}
		headers = {}
		if request.parameters:
			parameters = request.parameters
		if request.headers:
			headers = request.headers
		if request.is_get():
			response = requests.get(request.url)
			return self.json(response)
		elif request.is_post():
			response = requests.post(
				request.url,
				params = parameters,
				headers = headers
				)
			return self.verify(response)
		

	def json(self, response):
		if response.status_code == requests.codes.ok:
			return response.json()
		else:
			print("Request failed")

class RequestHandler(AbstractInstructionHandler):

	def handle(self, instructions, parameter_provider):
		if instructions.type == "request":
			payload = instructions.payload
			request_instructions = RequestInstruction(**payload)
			network = Network()
			json = network.do_request(request_instructions.http_request)

			if json is None:
				print("error")
				return

			response_modifiers = request_instructions.response_modifiers
			parameters_source = response_modifiers.parameters_source

			#Get values based on the paths from json response
			for parameter_source in parameters_source:
				value = json
				for key in parameter_source:
					value = value[key]
				parameter_provider.store_value(value)

			#Do operations
			operation_client = OperationClient()
			operations = response_modifiers.operations

			for operation in operations:
				value = parameter_provider.get_values_from_dynamic(operation)
				operation_client.handle(operation, parameter_provider)

			print(parameter_provider.parameters.data['r'])

			#Snacks
			#snacks = requestInstructions.snacks
			#print(snacks)
			#for index, _snack in enumerate(snacks):
			#	snack = SnackOLED(**_snack)
			#	clear = 1 if index == 0 else 0
			#	i2cDataString = snack.i2cDataString(clear, values, results)
			#	i2cDataBytes = stringToBytes(i2cDataString)
			#	i2cManager.writei2c(snack.address, i2cDataBytes)


			#payload = json['payload']
			#currency = payload['book']
			#high = payload['high']
			#last = payload['last']
			#avergae = (float(high) + float(last)) / 2
		else:
			super().handle(request)