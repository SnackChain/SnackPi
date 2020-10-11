from handler.operation.adittion import AdittionHandler
from handler.operation.handler import *

class OperationClient():
    handler: OperationHandler

    def __init__(self):
        adittion_handler = AdittionHandler()
        subtraction_handler = SubtractionHandler()
        multiplication_handler = MultiplicationHandler()
        split_handler = SplitHandler()
        textcase_handler = TextcaseHandler()

        adittion_handler.set_next(subtraction_handler)
        subtraction_handler.set_next(multiplication_handler)
        multiplication_handler.set_next(split_handler)
        split_handler.set_next(textcase_handler)

        self.handler = adittion_handler

    def handle(self, operation, parameter_provider):
        self.handler.handle(operation, parameter_provider)