try:
	import urequests as requests
    #from urequests.adapters import HTTPAdapter
    #from urequests.exceptions import ConnectionError
except ImportError:
    import requests
    #from requests.adapters import HTTPAdapter
    #from requests.exceptions import ConnectionError

class HTTPRequest():
	def __init__(self, url, method, headers = None, parameters = None, parameter_encoding = 'json'):
		self.url = url
		self.headers = headers
		self.parameters = parameters
		self.method = method
		self.parameter_encoding = parameter_encoding

	def is_get(self):
		if self.method == 'GET':
			return True
		else:
			return False

	def is_post(self):
		if self.method == 'POST':
			return True
		else:
			return False

class NetworkLoader:
	next_loader = None

	def __init__(self):
		self.next_loader = SessionLoader()

	def load(self, request):
		return self.next_loader.load(request)

class SessionLoader():
	next_loader = None

	#session = requests.Session()

	#def __init__(self):
		#adapter = HTTPAdapter(max_retries=2)
		#self.session.mount("https://", adapter)
		#self.session.mount("http://", adapter)

	def load(self, request: HTTPRequest):
		parameters = {}
		headers = {}
		if request.parameters is not None:
			parameters = request.parameters
		if request.headers is not None:
			headers = request.headers
		if "Content-Type" not in headers and request.parameter_encoding == 'json':
			headers["Content-Type"] = "application/json"
		print("------------------- Request -------------------")
		print("--- url: ", request.url)
		print("--- method: ", request.method)
		print("--- parameters: ", parameters)
		print("--- headers: ", headers)
		if request.is_get():
			response = requests.get(
				request.url,
				headers = headers
				)
			return response
		elif request.is_post():
			response = requests.post(
				request.url,
				data = parameters,
				headers = headers
				)
			return response

class NetworkClient:

	http_loader = NetworkLoader()

	def request(self, request):
		response = self.http_loader.load(request)
		if request.is_get():
			json = self.handle_json_response(response)
			return json
		else:
			print("--- status: POST succeed")
			print("-----------------------------------------------")

	def handle_json_response(self, response):
		if response is not None and response.status_code >= 200 and response.status_code <= 299:
			print("--- status: GET succeed")
			try:
				json = response.json()
				print("--- response:", json)
				print("-----------------------------------------------")
				return json
			except ValueError:
				print("--- response: None")
				print("-----------------------------------------------")
		else:
			print("--- status: failed")
			print("-----------------------------------------------")
