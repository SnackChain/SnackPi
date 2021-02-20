from handler.type.request import RequestHandler
from model.instruction import Instruction
from handler.directive.handler import AbstractDirectiveHandler

class InstructionClient(AbstractDirectiveHandler):
    handler = None

    def __init__(self):
        request_handler = RequestHandler()
        self.handler = request_handler

    def handle(self, directive, parameter_provider, snack_manager):
        if directive.type == "instruction":
            instruction = Instruction(**directive.data)
            self.handler.handle(instruction, parameter_provider)
        else:
            super().handle(directive, parameter_provider, snack_manager)