from model.instruction import Snack
from provider.snack import SnackProvider
from handler.snack.input.handler import SnackInputHandler
from handler.snack.input.oled import OLEDHandler
from handler.snack.input.boolean import BooleanHandler

class SnackInputClient():

	handler: SnackInputHandler

	def __init__(self):
		oled_handler = OLEDHandler()
		led_handler = BooleanHandler()

		oled_handler.set_next(led_handler)
		
		self.handler = oled_handler

	def handle(self, inputs, parameter_provider, i2c_provider):
		snack_provider = SnackProvider()
		if inputs != None:
			for snack_dictionary in inputs:
				snack = Snack(**snack_dictionary)
				snack_device_id = snack_provider.get_input_device_id(snack)
				bytes_to_send = self.handler.handle(snack_device_id, snack, parameter_provider)
				print(bytes_to_send)
				i2c_provider.write(snack.address, bytes_to_send)