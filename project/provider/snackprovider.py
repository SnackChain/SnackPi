class SnackInfo():
	def __init__(self, ip, id, mac, spec):
		self.ip = ip
		self.id = id
		self.mac = mac
		self.spec = spec

# This class contains the necessary Snacks addresses for 1 set of instructions
# Once all addresses are available, it can fire
class AddressChecker():
	PENDING = 'P'
	FIRED = 'F'
	READY = 'R'

	required_addresses = None
	start_closure = None
	status = PENDING

	def __init__(self, required_addresses, start_closure):
		self.required_addresses = required_addresses
		self.start_closure = start_closure

	def check(self, available_snacks):
		if self.status == self.FIRED:
			return
		for address in self.required_addresses:
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
	snacks = {}

	def addChecker(self, address_checker):
		self.address_checkers.append(address_checker)

	def process(self, json):
		snack_info = SnackInfo(**json)
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