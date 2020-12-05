import requests
from handler.type.handler import AbstractInstructionHandler
from handler.operation.client import OperationClient

class RequestInstruction():
	def __init__(self, url, method, headers = None, parameters = None, request_source = None, response_source = None):
		self.http_request = HTTPRequest(url, method, headers, parameters)
		self.request_source = request_source
		self.response_source = response_source

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

			#Get values based on the paths from json response
			for parameter_source in request_instruction.response_source:
				value = json
				for key in parameter_source:
					value = value[key]
				parameter_provider.store_value(value)
		else:
			super().handle(request)