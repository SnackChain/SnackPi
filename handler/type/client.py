from handler.type.request import RequestHandler
from handler.type.handler import InstructionHandler
from model.instruction import Instruction
from handler.directive.handler import AbstractDirectiveHandler

class InstructionClient(AbstractDirectiveHandler):
    handler: InstructionHandler

    def __init__(self):
        request_handler = RequestHandler()
        self.handler = request_handler

    def handle(self, directive, parameter_provider, i2c_provider):
        if directive.type == "instruction":
            instruction = Instruction(**directive.data)
            self.handler.handle(instruction, parameter_provider)
        else:
            super().handle(directive, parameter_provider, i2c_provider)