from handler.snack.handler import AbstractSnackInputHandler
from provider.byte import ByteProvider

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
			return self.generate_data(snack, oled, parameter_provider)
		else:
			return super().handle(snack_device_id, snack, parameter_provider)

	def generate_data(self, snack, oled, parameter_provider):
		cursor_x = str(oled.cursor[0])
		cursor_y = str(oled.cursor[1])
		for _ in range(3 - len(cursor_x)):
			cursor_x = "0" + cursor_x
		for _ in range(2 - len(cursor_y)):
			cursor_y = "0" + cursor_y

		final_text = ""
		if oled.is_dynamic():
			final_text = parameter_provider.get_value_from_dynamic(oled.dinamic_value)
			final_text = str(final_text)
		else:
			final_text = oled.static_value

		string_data = "{" + str(snack.device) + "[" + str(oled.clear_value()) + str(oled.text_size) + cursor_x + cursor_y + "~" + final_text
		#Example
		#{1[1100000~BTC
		bytes_to_send = ByteProvider().from_string(string_data)
		return bytes_to_send