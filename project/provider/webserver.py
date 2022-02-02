import requests
from aiohttp import web

app = web.Application()

class RegisterSnack(web.View):

    def __init__(self, snack_provider):
        self.snack_provider = snack_provider

    async def __call__(self, request):
        json = await request.json()
        print("Registering device:")
        print(json)
        self.snack_provider.register_snack_from_json(json)
        return web.Response(text="registered", status=201)

class UpdateInstructions(web.View):

    def __init__(self, instructions_handler, snack_provider):
        self.instructions_handler = instructions_handler
        self.snack_provider = snack_provider

    async def __call__(self, request):
        json = await request.json()
        print("Update instructions:")
        print(json)
        self.instructions_handler.update_instructions_from_json(json, self.snack_provider.available_snacks())
        return web.Response(text="registered", status=201)

def runner(snack_provider, instructions_handler):
    app.router.add_route("POST", "/registersnack", RegisterSnack(snack_provider))
    app.router.add_route("POST", "/updateinstructions", UpdateInstructions(instructions_handler, snack_provider))
    return web.AppRunner(app)

def site(runner):
    site = web.TCPSite(runner, host="snackbase.local", port=5000)   
    return site

# def send_instruction():
# 	url = ip + "/instruction"
# 	response = requests.post(
# 		url,
# 		data = '{1[1100000~BTC:}{1[0200009~239,764.5}{1[0111025~MXN}{2[1}{3[1}'
# 		)