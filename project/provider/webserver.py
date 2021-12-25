import requests
from aiohttp import web

class WebServer():

    app = web.Application()
    routes = web.RouteTableDef()
    snack_provider = None

    def __init__(self, snack_provider):
        self.snack_provider = snack_provider

    @routes.post('/registersnack')
    async def registersnack(self, request):
        await self.snack_provider.process(request.json())
        return web.Response(text="registered", status=200)

    def runner(self):
        self.app.add_routes(self.routes)
        return web.AppRunner(self.app)

    def site(self, runner):
        site = web.TCPSite(runner, host="snackbase.local")   
        return site


# def send_instruction():
# 	url = ip + "/instruction"
# 	response = requests.post(
# 		url,
# 		data = '{1[1100000~BTC:}{1[0200009~239,764.5}{1[0111025~MXN}{2[1}{3[1}'
# 		)