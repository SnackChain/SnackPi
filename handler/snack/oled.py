from handler.snack.handler import AbstractSnackInputHandler

class OLED():
	def __init__(self, cursor, text_size, dinamic_value = None, static_value = None, clear = False):
		self.cursor = cursor
		self.text_size = text_size
		self.dinamic_value = dinamic_value
		self.static_value = static_value
		self.clear = clear

	def is_dynamic(self):
		if self.dinamic_value:
			return True
		else:
			return False

	def clear_value(self):
		if self.clear:
			return 1
		else:
			return 0

class OLEDHandler(AbstractSnackInputHandler):

	def handle(self, snack_device_id, snack, parameter_provider):
		if snack_device_id == 'oled':
			oled = OLED(**snack.parameters)
			self.i2cDataString(snack, oled, parameter_provider)
		else:
			super().handle(snack_device_id, snack, parameter_provider)

	def i2cDataString(self, snack, oled, parameter_provider):
		cursorX = str(oled.cursor[0])
		cursorY = str(oled.cursor[1])
		for _ in range(3 - len(cursorX)):
			cursorX = "0" + cursorX
		for _ in range(2 - len(cursorY)):
			cursorY = "0" + cursorY

		finalText = ""
		if oled.is_dynamic():
			finalText = parameter_provider.get_value_from_dynamic(oled.dinamic_value)
			finalText = str(finalText)
		else:
			finalText = oled.static_value

		stringData = "{" + str(snack.device) + "[" + str(oled.clear_value()) + str(oled.text_size) + cursorX + cursorY + "~" + finalText + "]}"
		print(stringData)
		return stringData