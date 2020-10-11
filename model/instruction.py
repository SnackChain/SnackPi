from __future__ import annotations

## Main structure for any snack instruction
class SnackInstructions():
	def __init__(self, instructions, snacks):
		self.instructions = Instructions(**instructions)
		self.snacks = Snacks(**snacks)

class Instructions():
	def __init__(self, type, event_time, payload = None):
		self.type = type
		self.event_time = event_time
		self.payload = payload

class Snacks():
	def __init__(self, outputs = None, inputs = None):
		self.outputs = outputs
		self.inputs = inputs

class Snack():
	def __init__(self, address, device, parameters):
		self.address = address
		self.device = device
		self.parameters = parameters