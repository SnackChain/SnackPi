# SMBus mock
# This helps to develop in a computer without having the i2c interface that raspberry pi has
class SMBus():
	def __init__(self, address):
		self.address = address

	def write_i2c_block_data(self, slave_address, memory, bytes):
		description = "Master address: " + str(self.address) + ", Slave address: " + str(slave_address)
		print("-----------------------------------------")
		print(description)
		print(bytes)
		print("-----------------------------------------")