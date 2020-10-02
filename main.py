import json
from requestHandler import *

snackJSON = '{"instruction": "request","payload": {"url": "https://api.bitso.com/v3/ticker/?book=btc_mxn","trees": [["payload", "book"], ["payload", "high"], ["payload", "low"]],"operations": [["v1", "+", "v2"], ["r0", "*", "0.5"]],"snacks": [{"address": 8,"device": 1,"cursor": [0, 0],"textSize": 1,"text": null,"textKey": "v0"}, {"address": 8,"device": 1,"cursor": [0, 10],"textSize": 2,"text": null,"textKey": "r1"},{"address": 8,"device": 1,"cursor": [110, 25],"textSize": 1,"text": "MXN","textKey": null}]}}'

def start1():
	#monkey.set_next(squirrel).set_next(dog)
	requestHandler = RequestHandler()
	snackDictionary = json.loads(snackJSON)
	requestHandler.handle(snackDictionary)

start1()