class Snacks:
    identifiers = {8: {1: "oled"}}

class SnackProvider():
    snacks = Snacks()

    def get_device_id(self, snack):
    	return self.snacks.identifiers[snack.address][snack.device]
