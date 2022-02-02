from manager.instructionstatushandler import InstructionStatusHandler
from handler.time.client import EventTimeClient
from handler.directive.client import DirectiveClient
from provider.parameter import ParameterProvider
from model.instruction import Directive

class SingleInstructionHandler():
	instruction_status_handler = None
	snack_instruction_data = None
	snack_communicator = None
	cancellables = None

	# init -> fire_instruction -> handle_time -> handle_directive ->? cancel
	def __init__(self, snack_instruction_data, snack_communicator):
		self.snack_instruction_data = snack_instruction_data
		self.snack_communicator = snack_communicator
		self.instruction_status_handler = InstructionStatusHandler(self.snack_instruction_data.require)

	def set_ready_status_if_requirements_met(self, available_snacks):
		self.instruction_status_handler.set_ready_status_if_requirements_met(available_snacks)

	def fire_instruction_if_ready(self):
		print("fire_instruction_if_ready")
		if self.instruction_status_handler.set_fired_status_if_ready():
			print("about to handle time")
			self.handle_event_time()

	def handle_event_time(self):
		print("Handle time")
		event_time_client = EventTimeClient()
		self.cancellable = event_time_client.handle(self.snack_instruction_data.event_time, self.handle_directives)

	# This is called within the EventTimeClient every time the event conditions are met.
	def handle_directives(self):
		print("Handle directive")
		directive_client = DirectiveClient()
		parameter_provider = ParameterProvider()
		for directive in self.snack_instruction_data.directives:
			directive_client.handle(directive, parameter_provider, self.snack_communicator)

	# TODO: call cancel when the snacks are disconnected
	def cancel(self):
		self.cancellable()