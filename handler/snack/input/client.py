from model.instruction import SnackInput
from handler.snack.input.handler import SnackInputHandler
from handler.snack.input.input import InputHandler
from handler.directive.handler import AbstractDirectiveHandler

class SnackInputClient(AbstractDirectiveHandler):

	handler: SnackInputHandler

	def __init__(self):
		input_handler = InputHandler()
		self.handler = input_handler

	def handle(self, directive, parameter_provider, i2c_provider):
		if directive.type == "snack.input":
			for snack_input_dictionary in directive.data:
				snack_input = SnackInput(**snack_input_dictionary)
				bytes_to_send = self.handler.handle(snack_input, parameter_provider)
				i2c_provider.write(snack_input.address, bytes_to_send)
		else:
			super().handle(directive, parameter_provider, i2c_provider)