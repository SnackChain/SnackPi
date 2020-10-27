from __future__ import annotations

## Main structure for any snack instruction
class SnackSetOfInstructions():
	def __init__(self, event_time, directives):
		self.event_time = EventTime(**event_time)
		self.directives = directives

class SnackDirective:
	def __init__(self, type, data):
		self.type = type
		self.data = data

class EventTime():
	def __init__(self, type, parameters = None):
		self.type = type
		self.parameters = parameters

class Instruction():
	def __init__(self, type, payload = None):
		self.type = type
		self.payload = payload

#Snacks

#Snack outputs
class SnackOutput():
	def __init__(self, address, devices, types, length):
		self.address = address
		self.devices = devices
		self.types = types
		self.length = length

#Snack inputs
class SnackInput():
	def __init__(self, address, values):
		self.address = address
		self.values = values

class SnackInputValue():
	def __init__(self, static_value = None, dynamic_value = None):
		self.static_value = static_value
		self.dynamic_value = dynamic_value