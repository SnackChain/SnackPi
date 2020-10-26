import time
import math
import constants
from provider.byte import ByteProvider
try:
    import smbus2 as smbus
except ImportError:
    from mock import smbus2 as smbus

class I2CProvider():
	i2c_bus = smbus.SMBus(1)

	def write(self, snack_address, bytes):
		if bytes:
			self.i2c_bus.write_i2c_block_data(snack_address, 0, bytes)
			time.sleep(0.4)
		else:
			description = "Nothing to write to i2c bus, address: " + str(snack_address)
			print(description)

	def read(self, snack_address, length):
		data_bytes = ''
		times = math.ceil(length / 32)
		byte_provider = ByteProvider()
		for index in range(0, times):
			if index > 0:
				time.sleep(0.2)
			i2c_length = length - 32 * index
			if index != (times - 1):
				i2c_length = 32

			i2c_block = self.i2c_bus.read_i2c_block_data(snack_address, 0, length)
			i2c_block = byte_provider.char_from_byte(i2c_block)
			data_bytes = data_bytes + i2c_block

		buffers = string_buffer.split(I2C_START_CHAR)
		buffers = list(filter(None, buffers))
		return buffers