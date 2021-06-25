import urequests as requests
try:
    import tinyweb
except ImportError:
    import mock.tinyweb as tinyweb

class RegisterSnack():

    def __init__(self, snack_provider):
        self.snack_provider = snack_provider

    def get(self, data):
        """Return list of all customers"""
        print(data)
        return "", 200

    def post(self, data):
        print(data)
        self.snack_provider.process(data)
        return "", 201

def run(snack_provider):
    app = tinyweb.webserver()
    app.add_resource(RegisterSnack(snack_provider), '/registersnack')
    app.run(host='192.168.4.1', port=80)

# def send_instruction():
# 	url = ip + "/instruction"
# 	response = requests.post(
# 		url,
# 		data = '{1[1100000~BTC:}{1[0200009~239,764.5}{1[0111025~MXN}{2[1}{3[1}'
# 		)