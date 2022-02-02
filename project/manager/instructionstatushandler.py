class InstructionStatus():
	PENDING = 'P'
	FIRED = 'F'
	READY = 'R'
	current = PENDING

	def set_fired(self):
		print("set fired")
		self.current = self.FIRED

	def set_ready(self):
		print("set ready")
		self.current = self.READY	

	def is_fired(self):
		return self.current == self.FIRED

	def is_ready(self):
		return self.current == self.READY

class InstructionStatusHandler():

	required_parameters = None
	status = None

	def __init__(self, required_parameters):
		self.required_parameters = required_parameters
		self.status = InstructionStatus()

	def all_addresses_available(self, available_snacks):
		all_addresses_available = True
		for address in self.required_parameters.addresses:
			if address not in available_snacks:
				all_addresses_available = False
		return all_addresses_available

	def set_ready_status_if_requirements_met(self, available_snacks):
		if self.status.is_fired():
			return
		all_addresses_available = self.all_addresses_available(available_snacks)
		if all_addresses_available:
			self.status.set_ready()

	def is_ready_to_fire(self):
		return self.status.is_ready()

	def set_fired_status_if_ready(self):
		if self.status.is_ready():
			self.status.set_fired()
			return True
		return False
