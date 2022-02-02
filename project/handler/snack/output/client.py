from model.instruction import SnackOutput
from handler.directive.handler import AbstractDirectiveHandler
from handler.snack.output.output import OutputHandler

class SnackOutputClient(AbstractDirectiveHandler):

	handler = None

	def __init__(self):
		output_handler = OutputHandler()
		self.handler = output_handler

	def handle(self, directive, parameter_provider, snack_communicator):
		if directive.type == "snack.output":
			for snack_output_dictionary in directive.data:
				snack_output = SnackOutput(**snack_output_dictionary)
				buffers = snack_communicator.read(snack_output.mac_address, snack_output.length)
				self.handler.handle(snack_output, buffers, parameter_provider)
		else:
			super().handle(directive, parameter_provider, snack_communicator)
		