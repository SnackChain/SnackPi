from handler.task.request import RequestHandler
from model.instruction import Task
from handler.directive.handler import AbstractDirectiveHandler

class InstructionClient(AbstractDirectiveHandler):
    handler = None

    def __init__(self):
        request_handler = RequestHandler()
        self.handler = request_handler

    def handle(self, directive, parameter_provider, snack_communicator):
        if directive.type == "task":
            instruction = Task(**directive.data)
            self.handler.handle(instruction, parameter_provider)
        else:
            super().handle(directive, parameter_provider, snack_communicator)