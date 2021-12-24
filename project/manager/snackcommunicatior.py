from manager.networkclient import HTTPRequest, NetworkClient

class SnackCommunicatior():
	network_client = NetworkClient()

	def __init__(self, snack_provider):
		self.snack_provider = snack_provider

	def write(self, mac_address, body):
		ip = 'http://' + self.snack_provider.get_ip_for(mac_address) + '/instruction'
		if body is not None:
			request = HTTPRequest(ip, 'POST', parameters = body)
			json = network_client.request(request)
		else:
			print('Nothing to write to snack address: ', str(ip))

	def read(self, mac_address):
		ip = self.snack_provider.get_ip_for(mac_address)
		request = HTTPRequest(ip, 'GET')
		json = network_client.request(request)