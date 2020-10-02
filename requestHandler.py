from handler import *
import requests
from snackOLED import *
from stringToBytes import *
from i2cManager import *

class RequestInstruction():
	def __init__(self, url, trees, operations, snacks):
		self.url = url
		self.trees = trees
		self.operations = operations
		self.snacks = snacks

class RequestHandler(AbstractHandler):
	def doRequest(self, url):
		response = requests.get(url)
		if response.status_code == requests.codes.ok:
			json = response.json()
			return json
		return None

	def doOperation(self, lhs, operator, rhs) -> float:
		if operator == '+':
			return lhs + rhs
		elif operator == '-':
			return lhs - rhs
		elif operator == '*':
			return lhs * rhs
		else:
			return 0

	def handle(self, request) -> str:
		if request['instruction'] == "request":
			payload = request['payload']
			requestInstructions = RequestInstruction(**payload)
			json = self.doRequest(requestInstructions.url)
			values = {}
			results = {}

			if json is None:
				print("error")
				return

			#Trees
			trees = requestInstructions.trees
			for index, tree in enumerate(trees):
				value = json
				for jsonKey in tree:
					value = value[jsonKey]

				key = 'v' + str(index)
				values[key] = value
			print(values)

			#Operations
			operations = requestInstructions.operations
			for index, operation in enumerate(operations):
				result = 0.0
				operator = None
				for modifier in operation:
					firstChar = modifier[0]
					lastIndex = len(modifier)
					if firstChar == '+' or firstChar == '-' or firstChar == '*':
						operator = firstChar
					elif firstChar == 'v':
						value = float(values[modifier])
						if operator is None:
							result = value
						else:
							result = self.doOperation(result, operator, value)
					elif firstChar == 'r':
						value = float(results[modifier])
						if operator is None:
							result = value
						else:
							result = self.doOperation(result, operator, value)
					else:
						value = float(modifier)
						if operator is None:
							result = value
						else:
							result = self.doOperation(result, operator, value)
				key = 'r' + str(index)
				results[key] = result
			print(results)

			#Snacks
			snacks = requestInstructions.snacks
			#print(snacks)
			for index, _snack in enumerate(snacks):
				snack = SnackOLED(**_snack)
				clear = 1 if index == 0 else 0
				i2cDataString = snack.i2cDataString(clear, values, results)
				i2cDataBytes = stringToBytes(i2cDataString)
				i2cManager.writei2c(snack.address, i2cDataBytes)


			#payload = json['payload']
			#currency = payload['book']
			#high = payload['high']
			#last = payload['last']
			#avergae = (float(high) + float(last)) / 2

			return "Monkey: I'll eat the"
		else:
			return super().handle(request)