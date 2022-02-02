from model.snackinfo import SnackInfo

class SnackProvider():

	snacks = {}

	def register_snack_from_json(self, json, instructions_handler):
		snack_info = SnackInfo(**json)
		self.register_snack(snack_info, instructions_handler)

	def register_snack(self, snack_info, instructions_handler):
		self.snacks[snack_info.mac] = snack_info
		instructions_handler.run_pending(self.available_snacks())

	def available_snacks(self):
		return self.snacks.keys()

	def get_ip_for(self, mac_address):
		return self.snacks[mac_address].ip