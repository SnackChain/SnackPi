from handler.snack.handler import AbstractSnackInputHandler
from provider.byte import ByteProvider

class BooleanDevice():
	def __init__(self, dinamic_value = None, static_value = None):
		self.dinamic_value = dinamic_value
		self.static_value = static_value

	def is_dynamic(self):
		if self.dinamic_value:
			return True
		else:
			return False

class BooleanHandler(AbstractSnackInputHandler):

	def handle(self, snack_device_id, snack, parameter_provider):
		if snack_device_id == 'boolean':
			boolen_device = BooleanDevice(**snack.parameters)
			return self.generate_data(snack, boolen_device, parameter_provider)
		else:
			return super().handle(snack_device_id, snack, parameter_provider)

	def generate_data(self, snack, boolen_device, parameter_provider):
		bool_value = False
		if boolen_device.is_dynamic():
			bool_value = parameter_provider.get_value_from_dynamic(boolen_device.dinamic_value)
		else:
			bool_value = boolen_device.static_value

		bool_char = '0'
		if bool_value:
			bool_char = '1'

		string_data = "{" + str(snack.device) + "[" + bool_char
		#Example
		#{1[1
		#print(string_data)
		bytes_to_send = ByteProvider().from_string(string_data)
		#print(bytes_to_send)
		return bytes_to_send