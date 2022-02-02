import json
import schedule
import time
import provider.wlan as wlan
import provider.webserver as webserver
import asyncio

from provider.snackprovider import SnackProvider
from manager.singleinstructionhandler import SingleInstructionHandler
from model.instruction import Instruction
from manager.snackcommunicatior import SnackCommunicatior

class InstructionProvider():

	handlers = {}
	snack_communicator = None

	def __init__(self, snack_communicator):
		self.snack_communicator = snack_communicator
		self.load_instructions_from_local()

	def mock_instructions(self):
		instruction_mock_1 = open('instruction_mock_1.json')
		instructions_jsons = json.load(instruction_mock_1)
		return instructions_jsons

	def load_instructions_from_local(self):
		instructions_jsons = self.mock_instructions()
		self.update_instructions_handlers(instructions_jsons)

	def update_instructions_handlers(self, instructions_jsons):
		for instruction_json in instructions_jsons:
			instruction_id, single_instruction_handler = self.create_instruction_handler(instruction_json)
			if instruction_id in handlers:
				self.handlers[instruction_id].cancel()
			self.handlers[instruction_id] = single_instruction_handler

	def create_instruction_handler(self, instruction_json):
		instruction = Instruction(**instruction_json)
		single_instruction_handler = SingleInstructionHandler(instruction, self.snack_communicator)
		return instruction.id, single_instruction_handler
		
	def update_instructions_from_json(self, json):
		self.update_instructions_handlers(json)

class InstructionsHandler():

	instruction_provider = None

	def __init__(self, instruction_provider):
		self.instruction_provider = instruction_provider

	def run_pending(self, available_snacks):
		for single_instruction_handler in self.instruction_provider.handlers:
			single_instruction_handler.set_ready_status_if_requirements_met(available_snacks)
			single_instruction_handler.fire_instruction_if_ready()

	def update_instructions_from_json(self, json, available_snacks):
		self.instruction_provider.update_instructions_from_json(json)
		self.run_pending(available_snacks)

snack_provider = SnackProvider()
snack_communicator = SnackCommunicatior(snack_provider)
instruction_provider = InstructionProvider(snack_communicator)
instructions_handler = InstructionsHandler(instruction_provider) 

wlan.connect_to_wifi()
# wlan.create_access_point()

async def run_loop():
	while True:
		print("schedule.run_pending")
		schedule.run_pending()
		await asyncio.sleep(2)

event_loop = asyncio.get_event_loop()
runner = webserver.runner(snack_provider, instructions_handler)
event_loop.run_until_complete(runner.setup())
site = webserver.site(runner)    
event_loop.run_until_complete(site.start())
event_loop.create_task(run_loop())

event_loop.run_forever()

