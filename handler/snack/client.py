from model.instruction import Snack
from provider.snack import SnackProvider
from handler.snack.handler import SnackInputHandler
from handler.snack.oled import OLEDHandler

class SnackInputClient():

	handler: SnackInputHandler

	def __init__(self):
		oled_handler = OLEDHandler()
		self.handler = oled_handler

	def handle(self, inputs, parameter_provider, i2c_provider):
		snack_provider = SnackProvider()
		for snack_dictionary in inputs:
			snack = Snack(**snack_dictionary)
			snack_device_id = snack_provider.get_device_id(snack)
			bytes_to_send = self.handler.handle(snack_device_id, snack, parameter_provider)
			i2c_provider.write(snack.address, bytes_to_send)

			