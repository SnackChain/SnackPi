from model.instruction import SnackOutput
from handler.snack.output.handler import SnackOutputHandler
from handler.directive.handler import AbstractDirectiveHandler
from handler.snack.output.output import OutputHandler

class SnackOutputClient(AbstractDirectiveHandler):

	handler: SnackOutputHandler

	def __init__(self):
		output_handler = OutputHandler()
		self.handler = output_handler

	def handle(self, directive, parameter_provider, i2c_provider):
		if directive.type == "snack.output":
			for snack_output_dictionary in directive.data:
				snack_output = SnackOutput(**snack_output_dictionary)
				buffers = i2c_provider.read(snack_output.address, snack_output.length)
				self.handler.handle(snack_output, buffers, parameter_provider)
		else:
			super().handle(directive, parameter_provider, i2c_provider)
		