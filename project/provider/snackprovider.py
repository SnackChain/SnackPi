from model.snackinfo import SnackInfo

class SnackProvider():

	instructions = []
	snacks = {}

	def register_snack_from_json(self, json):
		snack_info = SnackInfo(**json)
		self.register_snack(snack_info)

	def register_snack(self, snack_info):
		self.snacks[snack_info.mac] = snack_info
		self.set_ready_status_if_requirements_met()
		self.run_pending()

	def get_ip_for(self, mac_address):
		return self.snacks[mac_address].ip

	def add_instruction(self, instruction):
		self.instructions.append(instruction)

	# def check_address(self):
	def set_ready_status_if_requirements_met(self)
		available_snacks = self.snacks.keys()
		for instruction in self.instructions:
			instruction.set_ready_status_if_requirements_met(available_snacks)

	def run_pending(self):
		for instruction in self.instructions:
			instruction.fire_instruction_if_ready()
