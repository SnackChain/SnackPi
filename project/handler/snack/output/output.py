from handler.snack.output.handler import AbstractSnackOutputHandler

class OutputHandler(AbstractSnackOutputHandler):

	def handle(self, snack_output, buffers, parameter_provider):
		#['2[123.4', '3[hello']

		#'3[hello'
		for snack_device in snack_output.devices:
			for current_buffer in buffers:
				#                           '3'
				current_device = chr(buffers[0])
				#       '3'             '3'
				if current_device == snack_device:
					#    '3,hello'
					snack_data_lists = current_buffer.split(I2C_DATA_START_CHAR)
					# 'hello'
					snack_value_string = snack_data_lists[1]
					snack_value = self.handle_data_type(snack_value_string, snack_output.type)
					parameter_provider.store_sensor(snack_value)

	def handle_data_type(snack_value, data_type):
		if data_type == 'string':
			return snack_value
		elif data_type == 'integer':
			try:
				integer = int(snack_value)
				return integer
			except:
				return None
		elif data_type == 'float':
			try:
				integer = float(snack_value)
				return integer
			except:
				return None
		elif data_type == 'boolean':
			if snack_value == '1':
				return True
			elif snack_value == '0':
				return False
