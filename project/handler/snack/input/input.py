from handler.snack.input.handler import AbstractSnackInputHandler
from model.instruction import SnackInputValue

class InputHandler(AbstractSnackInputHandler):

	def handle(self, snack_input, parameter_provider):
		string_block = ""
		for value in snack_input.values:
			snack_input_values = SnackInputValue(**value)
			if snack_input_values.static_value:
				string_block = string_block + snack_input_values.static_value
			elif snack_input_values.dynamic_value:
				value = parameter_provider.get_value_from_dynamic(snack_input_values.dynamic_value)
				if value != None:
					string_block = string_block + str(value)
		return string_block