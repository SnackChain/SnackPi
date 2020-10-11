import time
try:
    import smbus2 as smbus
except ImportError:
    from mock import smbus2 as smbus

class I2CProvider():
	i2c_bus = smbus.SMBus(1)

	def write(self, snack_address, bytes):
		if bytes:
			self.i2c_bus.write_i2c_block_data(snack_address, 0, bytes)
			time.sleep(0.5)
		else:
			print("Nothing to write to i2c bus")
