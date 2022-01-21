from manager.instructionstatusmanager import InstructionStatusManager
from handler.time.client import EventTimeClient
from handler.directive.client import DirectiveClient
from provider.parameter import ParameterProvider
from model.instruction import SnackDirective

class InstructionManager():
	instruction_status_manager = None
	snack_set_of_instructions = None
	snack_communicator = None
	cancellables = None

	# init -> fire_instruction -> handle_time -> handle_directive ->? cancel
	def __init__(self, snack_set_of_instructions, snack_communicator):
		self.snack_set_of_instructions = snack_set_of_instructions
		self.snack_communicator = snack_communicator
		self.instruction_status_manager = InstructionStatusManager(self.snack_set_of_instructions.require)

	def set_ready_status_if_requirements_met(self, available_snacks):
		self.instruction_status_manager.set_ready_status_if_requirements_met(available_snacks)

	def fire_instruction_if_ready(self):
		if self.instruction_status_manager.is_ready_to_fire():
			self.instruction_status_manager.set_fired_status()
			print("Fire")
			self.handle_time()

	def fire_instruction(self):
		def start():
			print("Start")
			self.handle_time()
		return start

	def handle_time(self):
		print("Handle time")
		event_time_client = EventTimeClient()
		self.cancellable = event_time_client.handle(self.snack_set_of_instructions.event_time, self.handle_directive)

	# This is called within the EventTimeClient every time the event conditions are met.
	def handle_directive(self):
		print("Handle directive")
		directive_client = DirectiveClient()
		parameter_provider = ParameterProvider()
		for directive_data in self.snack_set_of_instructions.directives:
			directive = SnackDirective(**directive_data)
			directive_client.handle(directive, parameter_provider, self.snack_communicator)

	# TODO: call cancel when the snacks are disconnected
	def cancel(self):
		self.cancellable()