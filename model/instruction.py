from __future__ import annotations

## Main structure for any snack instruction
class SnackInstruction():
	def __init__(self, instruction, snacks, event_time):
		self.instruction = Instruction(**instruction)
		self.snacks = Snacks(**snacks)
		self.event_time = EventTime(**event_time)

class Instruction():
	def __init__(self, type, payload = None):
		self.type = type
		self.payload = payload

class EventTime():
	def __init__(self, type, parameters = None):
		self.type = type
		self.parameters = parameters

class Snacks():
	def __init__(self, outputs = None, inputs = None):
		self.outputs = outputs
		self.inputs = inputs

class Snack():
	def __init__(self, address, device, parameters):
		self.address = address
		self.device = device
		self.parameters = parameters