class InstructionStatusManager():
	PENDING = 'P'
	FIRED = 'F'
	READY = 'R'

	required_parameters = None
	current_status = PENDING

	def __init__(self, required_parameters):
		self.required_parameters = required_parameters

	def set_ready_status_if_requirements_met(self, available_snacks):
		if self.status == self.FIRED:
			return
		all_addresses_available = self.all_addresses_available(available_snacks)
		if all_addresses_available:
			self.status = self.READY

	def all_addresses_available(self, available_snacks):
		all_addresses_available = True
		for address in self.required_parameters.addresses:
			if address not in available_snacks:
				all_addresses_available = False
		return all_addresses_available

	def is_ready_to_fire(self):
		return self.status == self.READY

	def set_fired_status(self):
		self.status = self.FIRED