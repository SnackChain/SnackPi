import requests
# try:
# from flask import Flask, request
# from flask_restful import Resource, Api
import tinyweb
# except ImportError:
#     import mock.tinyweb as tinyweb

# app = Flask(__name__)
# api = Api(app)

app = tinyweb.webserver()

class RegisterSnack():

    # def __init__(self, **kwargs):
        # self.snack_provider = kwargs['provider']
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
    # api.add_resource(RegisterSnack, '/registersnack', resource_class_kwargs={ 'provider': snack_provider })
    # app.run(host="0.0.0.0", port=5000)
    app.add_resource(RegisterSnack(snack_provider), '/registersnack')
    app.run()

# def send_instruction():
# 	url = ip + "/instruction"
# 	response = requests.post(
# 		url,
# 		data = '{1[1100000~BTC:}{1[0200009~239,764.5}{1[0111025~MXN}{2[1}{3[1}'
# 		)