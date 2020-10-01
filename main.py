from __future__ import annotations
import requests
import smbus2 as smbus
import time
import json
from abc import ABC, abstractmethod

i2cBus = smbus.SMBus(1)

def convertStringToBytes(src):
    bytes = []
    for character in src:
        bytes.append(ord(character))
    return bytes

def doRequest(url):
	response = requests.get(url)
	if response.status_code == requests.codes.ok:
		json = response.json()
		return json
	return None

def writei2c(device, data):
    #Create the i2c bus
    #data = "{1[1100000~BTC]}"
    #bytesToSend = convertStringToBytes(data)
    i2cBus.write_i2c_block_data(device, 0, data)
    time.delay(500)

class SnackOLED():
	def __init__(self, id, device, cursor, textSize, text, textKey):
		self.id = id
		self.device = device
		self.cursor = cursor
		self.textSize = textSize
		self.text = text
		self.textKey = textKey

	def i2cDataString(self, clear, values, results):
		cursorX = str(self.cursor[0])
		cursorY = str(self.cursor[1])
		for _ in range(3 - len(cursorX)):
			cursorX = "0" + cursorX
		for _ in range(2 - len(cursorY)):
			cursorY = "0" + cursorY

		finalText: str = self.text
		if self.textKey is not None:
			if self.textKey in values:
				finalText = str(values[self.textKey])
			elif self.textKey in results:
				finalText = str(results[self.textKey])
		stringData = "{" + str(self.device) + "[" + str(clear) + str(self.textSize) + cursorX + cursorY + "~" + finalText + "]}"
		return stringData

class RequestInstruction():
	def __init__(self, url, trees, operations, snacks):
		self.url = url
		self.trees = trees
		self.operations = operations
		self.snacks = snacks

class Handler(ABC):
	@abstractmethod
	def set_next(self, handler: Handler) -> Handler:
		pass

	@abstractmethod
	def handle(self, request) -> Optional[str]:
		pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class RequestHandler(AbstractHandler):
	def doOperation(self, lhs, operator, rhs) -> float:
		if operator == '+':
			return lhs + rhs
		elif operator == '-':
			return lhs - rhs
		elif operator == '*':
			return lhs * rhs
		else:
			return 0

	def handle(self, request: Any) -> str:
		if request['instruction'] == "request":
			payload = request['payload']
			requestInstructions = RequestInstruction(**payload)
			json = doRequest(requestInstructions.url)
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
				i2cDataBytes = convertStringToBytes(i2cDataString)
				writei2c(snack.device, i2cDataBytes)


			#payload = json['payload']
			#currency = payload['book']
			#high = payload['high']
			#last = payload['last']
			#avergae = (float(high) + float(last)) / 2

			return "Monkey: I'll eat the"
		else:
			return super().handle(request)

snackJSON = '{"instruction": "request","payload": {"url": "https://api.bitso.com/v3/ticker/?book=btc_mxn","trees": [["payload", "book"], ["payload", "high"], ["payload", "low"]],"operations": [["v1", "+", "v2"], ["r0", "*", "0.5"]],"snacks": [{"id": 8,"device": 1,"cursor": [0, 0],"textSize": 1,"text": null,"textKey": "v0"}, {"id": 8,"device": 1,"cursor": [0, 10],"textSize": 2,"text": null,"textKey": "r1"},{"id": 8,"device": 1,"cursor": [110, 25],"textSize": 1,"text": "MXN","textKey": null}]}}'

def start1():
	#monkey.set_next(squirrel).set_next(dog)
	requestHandler = RequestHandler()
	snackDictionary = json.loads(snackJSON)
	requestHandler.handle(snackDictionary)

start1()