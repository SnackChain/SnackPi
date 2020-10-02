#import smbus2 as smbus
import time

class I2CManager():
	#i2cBus = smbus.SMBus(1)
	def writei2c(self, device, data):
		print(device)
		print(data)
		#Create the i2c bus
		#data = "{1[1100000~BTC]}"
		#bytesToSend = convertStringToBytes(data)
		#self.i2cBus.write_i2c_block_data(device, 0, data)
		#time.delay(500)

i2cManager = I2CManager()
