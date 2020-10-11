class ByteProvider():
	def from_string(self, string):
	    bytes = []
	    for character in string:
	        bytes.append(ord(character))
	    return bytes