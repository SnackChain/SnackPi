from model.instruction import SnackInstructionsDataModel
from handler.type.request import RequestHandler
from handler.type.handler import InstructionHandler

class InstructionClient():
    handler: InstructionHandler

    def __init__(self):
        request_handler = RequestHandler()
        self.handler = request_handler

    def handle(self, snack_instruction_dictionary, parameter_provider):
        snack_instructions = SnackInstructionsDataModel(**snack_instruction_dictionary)
        self.handler.handle(snack_instructions, parameter_provider)