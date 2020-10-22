import json
from handler.type.client import InstructionClient
from handler.snack.client import SnackInputClient
from handler.time.client import EventTimeClient
from provider.parameter import ParameterProvider
from model.instruction import SnackInstruction
from provider.i2c import I2CProvider

import schedule
import time

snack_json = '{"instruction": {"type": "request","payload": {"url": "https://api.bitso.com/v3/ticker/?book=btc_mxn","headers": null,"parameters": null,"method": "GET","request_modifiers": null,"response_modifiers": {"parameters_source": [["payload", "book"],["payload", "high"],["payload", "low"]],"operations": [["v0", "split", "_"],["r0", "textcase", "uppercase"],["r1", "textcase", "uppercase"],["v1", "+", "v2"],["r4", "*", 0.5],["r5", "truncate", 2],["r5", ">", 239787]]}}},"event_time": {"type": "timer","parameters": {"time_interval": 10}},"snacks": {"inputs": [{"address": 8,"device": 1,"parameters": {"cursor": [0, 0],"text_size": 1,"dinamic_value": "r2","clear": true}},{"address": 8,"device": 1,"parameters": {"cursor": [0, 10],"text_size": 2,"dinamic_value": "r6"}},{"address": 8,"device": 1,"parameters": {"cursor": [110, 25],"text_size": 1,"dinamic_value": "r3"}},{"address": 8,"device": 2,"parameters": {"dinamic_value": "r7"}}]}}'
instructions_string = [snack_json]

def handle_instructions():
	i2c_provider = I2CProvider()
	for instruction_string in instructions_string:
		#Loads single set of instructions from JSON
		snack_instruction_dictionary = json.loads(snack_json)
		snack_instruction = SnackInstruction(**snack_instruction_dictionary)
		#Object to store and provide all the dynamic parameters
		parameter_provider = ParameterProvider()
		handle_time(snack_instruction, parameter_provider, i2c_provider)


def handle_time(snack_instruction, parameter_provider, i2c_provider):
	event_time_client = EventTimeClient()
	event_time_client.handle(snack_instruction.event_time, handlle_instruction_inputs, snack_instruction, parameter_provider, i2c_provider)

def handle_snacks_outputs():
	return

def handlle_instruction_inputs(snack_instruction, parameter_provider, i2c_provider):
	handle_instruction(snack_instruction.instruction, parameter_provider)
	handle_snacks_inputs(snack_instruction.snacks.inputs, parameter_provider, i2c_provider)

def handle_instruction(instruction, parameter_provider):
	#Object to manage all the instructions and generate the data to storage it in parameter_provider
	instruction_client = InstructionClient()
	instruction_client.handle(instruction, parameter_provider)

def handle_snacks_inputs(inputs, parameter_provider, i2c_provider):
	#Object to send the parameter_provider data to the snacks
	snack_input_client = SnackInputClient()
	snack_input_client.handle(inputs, parameter_provider, i2c_provider)

handle_instructions()

while True:
    schedule.run_pending()
    time.sleep(1)