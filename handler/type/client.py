from handler.type.request import RequestHandler
from handler.type.handler import InstructionHandler

class InstructionClient():
    handler: InstructionHandler

    def __init__(self):
        request_handler = RequestHandler()
        self.handler = request_handler

    def handle(self, instructions, parameter_provider):
        self.handler.handle(instructions, parameter_provider)