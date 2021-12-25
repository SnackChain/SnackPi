import requests
from aiohttp import web

app = web.Application()
routes = web.RouteTableDef()

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

@routes.post('/registersnack')
async def registersnack(request):
    """Return list of all customers"""
    print(request.match_info)
    return web.Response(text="registered", status=200)

def runner(snack_provider):
    # api.add_resource(RegisterSnack, '/registersnack', resource_class_kwargs={ 'provider': snack_provider })
    # app.run(host="0.0.0.0", port=5000)
    app.add_routes(routes)
    return web.AppRunner(app)

def site(runner):
    site = web.TCPSite(runner, host="snackbase.local")   
    return site

# def send_instruction():
# 	url = ip + "/instruction"
# 	response = requests.post(
# 		url,
# 		data = '{1[1100000~BTC:}{1[0200009~239,764.5}{1[0111025~MXN}{2[1}{3[1}'
# 		)