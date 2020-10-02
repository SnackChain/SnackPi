class SnackOLED():
	def __init__(self, address, device, cursor, textSize, text, textKey):
		self.address = address
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