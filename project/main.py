import ujson as json
import schedule
import time
import provider.wlan as wlan
import provider.webserver as webserver
import uasyncio as asyncio
from handler.time.client import EventTimeClient
from provider.parameter import ParameterProvider
from provider.snackprovider import SnackProvider, AddressChecker
from model.instruction import SnackSetOfInstructions
from model.instruction import SnackDirective
from manager.snackmanager import SnackManager
from handler.directive.client import DirectiveClient


# snack_json = '{"event_time":{"type":"timer","parameters":{"time_interval":10}},"require":{"addresses":["5C:CF:7F:36:E3:33"]},"directives":[{"type":"instruction","data":{"type":"request","payload":{"url":"https://api.bitso.com/v3/ticker/?book=btc_mxn","headers":null,"parameters":null,"method":"GET","request_source":null,"response_source":[["payload","book"],["payload","high"],["payload","low"]]}}},{"type":"operation","data":[["v0","split","_"],["r0","textcase","uppercase"],["r1","textcase","uppercase"],["v1","+","v2"],["r4","*",0.5],["r5","truncate",2],["r5",">",239787]]},{"type":"snack.input","data":[{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[1100000~"},{"dynamic_value":"r2"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[0200010~"},{"dynamic_value":"r6"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[0111025~"},{"dynamic_value":"r3"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{2["},{"dynamic_value":"r7"}]}]}]}'
snack_json = '{"event_time":{"type":"timer","parameters":{"time_interval":10}},"require":{"addresses":["5C:CF:7F:36:E3:33"]},"directives":[{"type":"instruction","data":{"type":"request","payload":{"url":"https://api.bitso.com/v3/ticker/?book=xrp_mxn","headers":null,"parameters":null,"method":"GET","request_source":null,"response_source":[["payload","book"],["payload","last"]]}}},{"type":"operation","data":[["v0","split","_"],["r0","textcase","uppercase"],["r1","textcase","uppercase"],["v1",">",850000]]},{"type":"snack.input","data":[{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[1100000~"},{"dynamic_value":"r2"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[0200010~"},{"dynamic_value":"v1"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{1[0111025~"},{"dynamic_value":"r3"}]},{"address":"5C:CF:7F:36:E3:33","values":[{"static_value":"{2["},{"dynamic_value":"r4"}]}]}]}'
instructions_string = [snack_json]
snack_provider = SnackProvider()
snack_manager = SnackManager(snack_provider)

def start_snack(snack_set_of_instructions, snack_manager):
	def start():
		print("Start called")
		#It stores and provide all the dynamic parameters
		handle_time(snack_set_of_instructions, snack_manager)
	return start

def handle_instructions(snack_manager, snack_provider):
	for instruction_string in instructions_string:
		#Loads single set of instructions from JSON
		snack_instruction_dictionary = json.loads(instruction_string)
		snack_set_of_instructions = SnackSetOfInstructions(**snack_instruction_dictionary)
		require_addresses = snack_set_of_instructions.require.addresses
		start_snack_closure = start_snack(snack_set_of_instructions, snack_manager)
		addressChecker = AddressChecker(require_addresses, start_snack_closure)
		snack_provider.addChecker(addressChecker)

def handle_time(snack_set_of_instructions, snack_manager):
	event_time_client = EventTimeClient()
	event_time_client.handle(
		snack_set_of_instructions.event_time,
		handlle_directive,
		snack_set_of_instructions.directives,
		snack_manager
		)

def handlle_directive(directives, snack_manager):
	print("Directive started")
	directive_client = DirectiveClient()
	parameter_provider = ParameterProvider()
	values = parameter_provider.parameters.data['v']
	print("values", values)
	for directive_data in directives:
		directive = SnackDirective(**directive_data)
		directive_client.handle(directive, parameter_provider, snack_manager)

wlan.connect_to_wifi()
wlan.create_access_point()
handle_instructions(snack_manager, snack_provider)

async def run_webserver():
	await webserver.run(snack_provider)

async def run_loop():
	while True:
		print("cycle")
		snack_provider.run_pending()
		schedule.run_pending()
		await asyncio.sleep_ms(5_000)

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