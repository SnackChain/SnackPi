class SnackInfo():
	def __init__(self, ip, id, mac, spec):
		self.ip = ip
		self.id = id
		self.mac = mac
		self.spec = spec

class AddressChecker():
	PENDING = 'P'
	FIRED = 'F'
	READY = 'R'

	require_addresses = None
	start_closure = None
	status = PENDING

	def __init__(self, require_addresses, start_closure):
		self.require_addresses = require_addresses
		self.start_closure = start_closure

	def check(self, available_snacks):
		if self.status == self.FIRED:
			return
		for address in self.require_addresses:
			if address not in available_snacks:
				return
		self.status = self.READY

	@staticmethod
	def checkAll(address_checkers, available_snacks):
		for address_checker in address_checkers:
			address_checker.check(available_snacks)

	@staticmethod
	def run_pending(address_checkers):
		for address_checker in address_checkers:
			if address_checker.status == AddressChecker.READY:
				print("empezo")
				address_checker.start_closure()
				print("termino")
				address_checker.status = AddressChecker.FIRED


class SnackProvider():

	address_checkers = []

	try:
		import sys
		board = sys.platform
		if board == "esp8266" or board == "esp32":
			snacks = {}
		else:
			snacks = {"5C:CF:7F:36:E3:33": SnackInfo("192.168.4.2", "62DFBD97-9E7A-422F-8EBA-B15970F9D173", "5C:CF:7F:36:E3:33", "https://raw.githubusercontent.com/SnackChain/SnackChainDefinitions/master/spec.json")}
	except:
			snacks = {"5C:CF:7F:36:E3:33": SnackInfo("192.168.4.2", "62DFBD97-9E7A-422F-8EBA-B15970F9D173", "5C:CF:7F:36:E3:33", "https://raw.githubusercontent.com/SnackChain/SnackChainDefinitions/master/spec.json")}

	def addChecker(self, address_checker):
		self.address_checkers.append(address_checker)

	def process(self, data):
		snack_info = SnackInfo(**data)
		self.register_snack(snack_info)

	def register_snack(self, snack_info):
		self.snacks[snack_info.mac] = snack_info
		AddressChecker.checkAll(self.address_checkers, self.available_snacks())

	def get_ip_for(self, mac_address):
		return self.snacks[mac_address].ip

	def available_snacks(self):
		return self.snacks.keys()

	def run_pending(self):
		AddressChecker.run_pending(self.address_checkers)