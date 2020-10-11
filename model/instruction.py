from __future__ import annotations

## Main structure for any snack instruction
class SnackInstructionsDataModel():
	def __init__(self, instructions, snacks):
		self.instructions = InstructionDataModel(**instructions)
		self.snacks = SnacksDataModel(**snacks)

class InstructionDataModel():
	def __init__(self, type, event_time, payload = None):
		self.type = type
		self.event_time = event_time
		self.payload = payload

class SnacksDataModel():
	def __init__(self, outputs = None, inputs = None):
		self.outputs = outputs
		self.inputs = inputs