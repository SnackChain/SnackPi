import json
import schedule
import time
import provider.wlan as wlan
import provider.webserver as webserver
import asyncio

from provider.snackprovider import SnackProvider
from manager.instructionmanager import InstructionManager
from model.instruction import SnackSetOfInstructions
from manager.snackcommunicatior import SnackCommunicatior

instruction_mock_1 = open('instruction_mock_1.json')
snack_json = json.load(instruction_mock_1)
instructions_jsons = [snack_json]
snack_provider = SnackProvider()
snack_communicator = SnackCommunicatior(snack_provider)

def handle_instructions(snack_communicator, snack_provider):
	for snack_instruction_dictionary in instructions_jsons:
		handle_instruction(snack_instruction_dictionary, snack_communicator, snack_provider)

def handle_instruction(snack_instruction_dictionary, snack_communicator, snack_provider):
	snack_set_of_instructions = SnackSetOfInstructions(**snack_instruction_dictionary)
	snack_instruction_handler = InstructionManager(snack_set_of_instructions, snack_communicator)
	snack_provider.addChecker(snack_instruction_handler.address_checker())

wlan.connect_to_wifi()
# wlan.create_access_point()
handle_instructions(snack_communicator, snack_provider)

# async def run_loop():
# 	while True:
# 		print("cycle")
# 		# snack_provider.run_pending -> address_checker.start_closure() (fire_instruction from SnackInstructionManager)
# 		# snack_provider.run_pending()
# 		# schedule.run_pending()
# 		await asyncio.sleep(5)

event_loop = asyncio.get_event_loop()
runner = webserver.runner(snack_provider)
event_loop.run_until_complete(runner.setup())
site = webserver.site(runner)    
event_loop.run_until_complete(site.start())
# event_loop.create_task(run_loop())

event_loop.run_forever()

