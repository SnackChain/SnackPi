import json
from handler.type.client import InstructionClient
from manager.parameter_provider import ParameterProvider

snack_json = '{"instructions": {"type": "request","event_time": {"type": "timer","time_interval": 60},"payload": {"url": "https://api.bitso.com/v3/ticker/?book=btc_mxn","headers": null,"parameters": null,"method": "GET","request_modifiers": null,"response_modifiers": {"parameters_source": [["payload", "book"],["payload", "high"],["payload", "low"]],"operations": [["v0", "split", "_"],["r0", "textcase", "uppercase"],["r1", "textcase", "uppercase"],["v1", "+", "v2"],["r4", "*", 0.5]]}}},"snacks": {"outputs": [{"address": 8,"device": 1,"parameters": {"cursor": [0, 0],"textSize": 1,"dinamic_value": "r0"}},{"address": 8,"device": 1,"parameters": {"cursor": [0, 10],"textSize": 2,"dinamic_value": "r5"}},{"address": 8,"device": 1,"parameters": {"cursor": [110, 25],"textSize": 1,"text": "MXN1"}}]}}'

def start1():
	parameter_provider = ParameterProvider()
	snack_instruction_dictionary = json.loads(snack_json)
	instruction_client = InstructionClient()
	instruction_client.handle(snack_instruction_dictionary, parameter_provider)

start1()