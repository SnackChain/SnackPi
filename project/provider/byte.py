class ByteProvider():
	def from_string(self, string):
	    bytes = []
	    for character in string:
	        bytes.append(ord(character))
	    return bytes

	def char_from_byte(self, buffer):
		chars = []
		for byte in buffer:
			chars.append(char(byte))
		return chars