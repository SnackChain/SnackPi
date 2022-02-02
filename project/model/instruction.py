## Main structure for any snack instruction
class Instruction():
	def __init__(self, id, event_time, directives, require):
		self.id = id
		self.event_time = EventTime(**event_time)
		self.directives = []
		for directive in directives:
			self.directives.append(Directive(**directives))
		self.require = Require(**require)

class Directive:
	def __init__(self, type, data):
		self.type = type
		self.data = data

class EventTime():
	def __init__(self, type, parameters = None):
		self.type = type
		self.parameters = parameters

class Task():
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

class Require():
	def __init__(self, addresses):
		self.addresses = addresses