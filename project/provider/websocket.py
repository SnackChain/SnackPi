import websockets
import asyncio
import json

class InstructionsUpdater():

    operation_type = "snackbase.update.instruction"

    def __init__(self, instructions_handler, snack_provider):
        self.instructions_handler = instructions_handler
        self.snack_provider = snack_provider

    def handle(self, data):
        self.instructions_handler.update_instructions_from_json(data, self.snack_provider.available_snacks())
        return "done"

class SnackRegister():

    operation_type = "snackbase.register.snackchain"

    def __init__(self, instructions_handler, snack_provider):
        self.instructions_handler = instructions_handler
        self.snack_provider = snack_provider

    def handle(self, data):
        self.snack_provider.register_snack_from_json(data, self.instructions_handler)
        return "done"

class SocketPayloadHandler():

    handlers = {}

    def __init__(self, instructions_handler, snack_provider):
        snack_register = SnackRegister(instructions_handler, snack_provider)
        instructions_updater = InstructionsUpdater(instructions_handler, snack_provider)
        handlers = [snack_register, instructions_updater]

        for handler in handlers:
            self.handlers[handler.operation_type] = handler

    def handle(self, json_object):
        operation_type = json_object["type"]
        data = json_object["data"]
        return self.handlers[operation_type].handle(data)

class SocketHandler():

    PORT = 7890
    connected = set()

    def __init__(self, instructions_handler, snack_provider):
        self.socket_payload_handler = SocketPayloadHandler(instructions_handler, snack_provider)

    async def handle_payload(self, snacksocket, message):
        json_object = json.loads(message)
        ip, _ = snacksocket.remote_address
        json_object["data"]["ip"] = ip
        print("Received message from client ip: " + ip)
        resolution = self.socket_payload_handler.handle(json_object)
        await snacksocket.send("Resolution: " + resolution)

    async def handle_event(self, snacksocket, path):
        self.connected.add(snacksocket)
        try:
            async for message in snacksocket:
                await self.handle_payload(snacksocket, message)
        except websockets.exceptions.ConnectionClosed as e:
            print("A client just disconnected")
        finally:
            self.connected.remove(snacksocket)

    def server():
        return websockets.serve(handle_event, "localhost", self.PORT)
