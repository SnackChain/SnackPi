class Snacks:
    inputs = {8: {1: "oled", 2: 'boolean'}}
    outputs = {8: {'length': 10, 'devices': {3: 'string'}}}

class SnackOutputInfo:
	def __init__(self, length, device_number, data_type):
		self.length = length
		self.device_number = device_number
		self.data_type = data_type

class SnackProvider():
    snacks = Snacks()

    def get_input_device_id(self, snack):
    	device_id = self.snacks.inputs[snack.address][snack.device]
    	return device_id

    def get_output_device_info(self, snack):
    	device_id = self.snacks.outputs[snack.address][snack.device]
    	device_number = snacks.device
    	length = self.snacks.outputs[snack.address]['length']
    	data_type = self.snacks.outputs[snack.address]['devices'][device_number]
    	return SnackOutputInfo(length, device_number, data_type)
