try:
	import urequests as requests
except ImportError:
    import requests
from handler.task.handler import AbstractInstructionHandler
from handler.operation.client import OperationClient
from manager.networkclient import HTTPRequest, NetworkClient

class RequestInstruction():
	def __init__(self, url, method, headers = None, parameters = None, request_source = None, response_source = None):
		self.http_request = HTTPRequest(url, method, headers, parameters)
		self.request_source = request_source
		self.response_source = response_source

class RequestHandler(AbstractInstructionHandler):

	def handle(self, instruction, parameter_provider):
		if instruction.type == "request":
			payload = instruction.payload
			request_instruction = RequestInstruction(**payload)
			network_client = NetworkClient()
			json = network_client.request(request_instruction.http_request)

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