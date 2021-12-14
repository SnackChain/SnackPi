import requests
try:
    from flask import Flask, request
    from flask_restful import Resource, Api
except ImportError:
    import mock.tinyweb as tinyweb

app = Flask(__name__)
api = Api(app)

class RegisterSnack(Resource):

    def __init__(self, **kwargs):
        self.snack_provider = kwargs['provider']

    def get(self, data):
        """Return list of all customers"""
        print(data)
        return "", 200

    def post(self, data):
        print(data)
        self.snack_provider.process(data)
        return "", 201

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def run(snack_provider):
    api.add_resource(HelloWorld, '/')
    api.add_resource(RegisterSnack, '/registersnack', resource_class_kwargs={ 'provider': snack_provider })
    app.run(debug=True)

# def send_instruction():
# 	url = ip + "/instruction"
# 	response = requests.post(
# 		url,
# 		data = '{1[1100000~BTC:}{1[0200009~239,764.5}{1[0111025~MXN}{2[1}{3[1}'
# 		)