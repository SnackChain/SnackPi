from handler.type.request import RequestHandler
from handler.type.handler import InstructionHandler

class InstructionClient():
    handler: InstructionHandler

    def __init__(self):
        request_handler = RequestHandler()
        self.handler = request_handler

    def handle(self, instruction, parameter_provider):
        return self.handler.handle(instruction, parameter_provider)