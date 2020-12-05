import json
from handler.time.client import EventTimeClient
from provider.parameter import ParameterProvider
from model.instruction import SnackSetOfInstructions
from model.instruction import SnackDirective
from provider.i2c import I2CProvider
from handler.directive.client import DirectiveClient

import schedule
import time

snack_json = '{"event_time":{"type":"timer","parameters":{"time_interval":10}},"directives":[{"type":"instruction","data":{"type":"request","payload":{"url":"https://api.bitso.com/v3/ticker/?book=btc_mxn","headers":null,"parameters":null,"method":"GET","request_source":null,"response_source":[["payload","book"],["payload","high"],["payload","low"]]}}},{"type":"operation","data":[["v0","split","_"],["r0","textcase","uppercase"],["r1","textcase","uppercase"],["v1","+","v2"],["r4","*",0.5],["r5","truncate",2],["r5",">",239787]]},{"type":"snack.input","data":[{"address":8,"values":[{"static_value":"{1[1100000~"},{"dynamic_value":"r2"}]},{"address":8,"values":[{"static_value":"{1[0200010~"},{"dynamic_value":"r6"}]},{"address":8,"values":[{"static_value":"{1[0111025~"},{"dynamic_value":"r3"}]},{"address":8,"values":[{"static_value":"{2["},{"dynamic_value":"r7"}]}]}]}'
instructions_string = [snack_json]

def handle_instructions():
	i2c_provider = I2CProvider()
	for instruction_string in instructions_string:
		#Loads single set of instructions from JSON
		snack_instruction_dictionary = json.loads(snack_json)
		snack_set_of_instructions = SnackSetOfInstructions(**snack_instruction_dictionary)
		#It stores and provide all the dynamic parameters
		parameter_provider = ParameterProvider()
		handle_time(snack_set_of_instructions, parameter_provider, i2c_provider)


def handle_time(snack_set_of_instructions, parameter_provider, i2c_provider):
	event_time_client = EventTimeClient()
	event_time_client.handle(snack_set_of_instructions.event_time, handlle_directive, snack_set_of_instructions.directives, parameter_provider, i2c_provider)

def handlle_directive(directives, parameter_provider, i2c_provider):
	directive_client = DirectiveClient()
	for directive_data in directives:
		directive = SnackDirective(**directive_data)
		directive_client.handle(directive, parameter_provider, i2c_provider)

handle_instructions()

while True:
    schedule.run_pending()
    time.sleep(1)