from model.instruction import Snack
from provider.snack import SnackProvider
from handler.snack.output.handler import SnackOutputHandler
from handler.snack.output.output import OutputHandler

class SnackOutputClient():

	handler: SnackOutputHandler

	def __init__(self):
		output_handler = OutputHandler()
		self.handler = output_handler

	def handle(self, outputs, parameter_provider, i2c_provider):
		snack_provider = SnackProvider()
		if outputs != None:
			for snack_dictionary in outputs:
				snack = Snack(**snack_dictionary)
				snack_output_info = snack_provider.get_output_device_length(snack)
				buffers = i2c_provider.read(snack.address, snack_output_info.length)
				self.handler.handle(snack_output_info, buffers, parameter_provider)