import json
import schedule
import time
import provider.wlan as wlan
import provider.webserver as webserver
import asyncio
from handler.time.client import EventTimeClient
from provider.parameter import ParameterProvider
from provider.snackprovider import SnackProvider, AddressChecker
from model.instruction import SnackSetOfInstructions
from model.instruction import SnackDirective
from manager.snackcommunicatior import SnackCommunicatior
from handler.directive.client import DirectiveClient


# snack_json = '{"event_time":{"type":"timer","parameters":{"time_interval":10}},"require":{"addresses":["5C:CF:7F:36:E3:33"]},"directives":[{"type":"instruction","data":{"type":"request","payload":{"url":"https://api.bitso.com/v3/ticker/?book=btc_mxn","headers":null,"parameters":null,"method":"GET","request_source":null,"response_source":[["payload","book"],["payload","high"],["payload","low"]]}}},{"type":"operation","data":[["v0","split","_"],["r0","textcase","uppercase"],["r1","textcase","uppercase"],["v1","+","v2"],["r4","*",0.5],["r5","truncate",2],["r5",">",239787]]},{"type":"snack.input","data":[{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[1100000~"},{"dynamic_value":"r2"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[0200010~"},{"dynamic_value":"r6"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[0111025~"},{"dynamic_value":"r3"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{2["},{"dynamic_value":"r7"}]}]}]}'
instruction_mock_1 = open('instruction_mock_1.json')
snack_json = json.load(instruction_mock_1)
instructions_jsons = [snack_json]
snack_provider = SnackProvider()
snack_communicator = SnackCommunicatior(snack_provider)


class SnackInstructionHandler():
	snack_set_of_instructions = None
	address_checker = None
	snack_communicator = None
	cancellable = None

	def __init__(self, snack_set_of_instructions, snack_communicator):
		self.snack_set_of_instructions = snack_set_of_instructions
		self.snack_communicator = snack_communicator
		self.address_checker = AddressChecker(snack_set_of_instructions.require.addresses, self.start_snack())
		# snack_provider.addChecker(addressChecker)

	def start_snack(self):
		def start():
			print("Start called")
			#It stores and provide all the dynamic parameters
			handle_time(self.snack_set_of_instructions)
		return start

	def handle_time(snack_set_of_instructions):
		event_time_client = EventTimeClient()
		self.cancellable = event_time_client.handle(self.snack_set_of_instructions.event_time, handle_directive)

	# This is called within the EventTimeClient every time the event conditions are met.
	def handle_directive():
		print("Directive started")
		directive_client = DirectiveClient()
		parameter_provider = ParameterProvider()
		# values = parameter_provider.parameters.data['v']
		# print("values", values)
		for directive_data in self.snack_set_of_instructions.directives:
			directive = SnackDirective(**directive_data)
			directive_client.handle(directive, parameter_provider, self.snack_communicator)

		# TODO: ccall ancel when the snacks are disconnected
	def cancel():
		cancellable()

def handle_instructions(snack_communicator, snack_provider):
	for snack_instruction_dictionary in instructions_jsons:
		handle_instruction(snack_instruction_dictionary, snack_communicator, snack_provider)

def handle_instruction(snack_instruction_dictionary, snack_communicator, snack_provider):
	snack_set_of_instructions = SnackSetOfInstructions(**snack_instruction_dictionary)
	SnackInstructionHandler(snack_set_of_instructions, snack_communicator)

wlan.connect_to_wifi()
wlan.create_access_point()
handle_instructions(snack_communicator, snack_provider)

async def run_webserver():
	webserver.run(snack_provider)

async def run_loop():
	while True:
		print("cycle")
		snack_provider.run_pending()
		schedule.run_pending()
		await asyncio.sleep(5)

event_loop = asyncio.get_event_loop()
event_loop.create_task(run_webserver())
event_loop.create_task(run_loop())

event_loop.run_forever()
# times = 0


# import network
# def start(quiet=False):
# 	network.WLAN(network.AP_IF).active(False)
# 	wlan = network.WLAN(network.STA_IF)
# 	wlan.active(True)
# 	if not wlan.isconnected():
# 		if not quiet: print('connecting to network...')
# 		wlan.connect('GV 2.4', '311153978')
# 		while not wlan.isconnected():
# 			pass
# 		wlan.config(dhcp_hostname="SnackBase")
# 	if not quiet: print('network config:', wlan.ifconfig())
# 	return(wlan)

# start()
# while True:
# 	pass