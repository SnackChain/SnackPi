import requests
from aiohttp import web

app = web.Application()

class RegisterSnack(web.View):

    async def post(self):
        print(self.request.json())
        self.snack_provider.process(self.request.json())
        return web.Response(text="registered", status=200)

def runner(snack_provider):
    app.add_route("/registersnack", RegisterSnack, snack_provider)
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