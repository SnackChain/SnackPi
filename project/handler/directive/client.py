from handler.type.client import InstructionClient
from handler.snack.input.client import SnackInputClient
from handler.snack.output.client import SnackOutputClient
from handler.operation.client import OperationClient
from handler.directive.handler import DirectiveHandler

class DirectiveClient():

    handler: DirectiveHandler

    def __init__(self):
        snack_output = SnackOutputClient()
        instruction = InstructionClient()
        operation = OperationClient()
        snack_input = SnackInputClient()

        snack_output.set_next(instruction)
        instruction.set_next(operation)
        operation.set_next(snack_input)
        
        self.handler = snack_output

    def handle(self, directive, parameter_provider, i2c_provider):
        self.handler.handle(directive, parameter_provider, i2c_provider)