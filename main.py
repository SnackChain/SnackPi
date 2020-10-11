import json
from handler.type.client import InstructionClient
from handler.snack.client import SnackInputClient
from provider.parameter import ParameterProvider
from model.instruction import SnackInstructions

snack_json = '{"instructions": {"type": "request","event_time": {"type": "timer","time_interval": 60},"payload": {"url": "https://api.bitso.com/v3/ticker/?book=btc_mxn","headers": null,"parameters": null,"method": "GET","request_modifiers": null,"response_modifiers": {"parameters_source": [["payload", "book"],["payload", "high"],["payload", "low"]],"operations": [["v0", "split", "_"],["r0", "textcase", "uppercase"],["r1", "textcase", "uppercase"],["v1", "+", "v2"],["r4", "*", 0.5]]}}},"snacks": {"inputs": [{"address": 8,"device": 1,"parameters": {"cursor": [0, 0],"text_size": 1,"dinamic_value": "r2","clear": true}},{"address": 8,"device": 1,"parameters": {"cursor": [0, 10],"text_size": 2,"dinamic_value": "r5"}},{"address": 8,"device": 1,"parameters": {"cursor": [110, 25],"text_size": 1,"dinamic_value": "r3"}}]}}'

def handle():
	
	#Load single set of instructions from JSON
	snack_instruction_dictionary = json.loads(snack_json)
	snack_instructions = SnackInstructions(**snack_instruction_dictionary)

	#Object to store and provide all the dynamic parameters
	parameter_provider = ParameterProvider()

	#Object to manage all the instructions and generate the data to storage it in parameter_provider
	instruction_client = InstructionClient()
	instruction_client.handle(snack_instructions.instructions, parameter_provider)

	#Object to send the parameter_provider data to the snacks
	snack_output_client = SnackInputClient()
	snack_output_client.handle(snack_instructions.snacks.inputs, parameter_provider)

handle()