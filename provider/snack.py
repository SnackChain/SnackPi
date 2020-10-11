class Snacks:
    identifiers = {8: {1: "oled", 2: 'boolean'}}

class SnackProvider():
    snacks = Snacks()

    def get_device_id(self, snack):
    	identifier = self.snacks.identifiers[snack.address][snack.device]
    	return identifier
