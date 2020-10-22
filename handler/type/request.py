import requests
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

	def handle(self, instruction, parameter_provider):
		if instruction.type == "request":
			payload = instruction.payload
			request_instruction = RequestInstruction(**payload)
			network = Network()
			json = network.do_request(request_instruction.http_request)

			if json is None:
				print("error")
				return

			response_modifiers = request_instruction.response_modifiers
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
		else:
			super().handle(request)