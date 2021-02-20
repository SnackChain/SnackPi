from model.instruction import SnackInput
from handler.snack.input.input import InputHandler
from handler.directive.handler import AbstractDirectiveHandler

class SnackInputClient(AbstractDirectiveHandler):

	handler = None

	def __init__(self):
		input_handler = InputHandler()
		self.handler = input_handler

	def handle(self, directive, parameter_provider, snack_manager):
		if directive.type == "snack.input":
			instructions = {}
			for snack_input_dictionary in directive.data:
				snack_input = SnackInput(**snack_input_dictionary)
				string_to_send = self.handler.handle(snack_input, parameter_provider)
				string_to_send += "}"
				if snack_input.address in instructions:
					instructions[snack_input.address] += string_to_send
				else:
					instructions[snack_input.address] = string_to_send
			for address, instruction in instructions.items():
				snack_manager.write(address, instruction)
		else:
			super().handle(directive, parameter_provider, snack_manager)