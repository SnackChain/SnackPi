from handler.operation.handler import OperationHandler
from handler.operation.adittion import AdittionHandler
from handler.operation.multiplication import MultiplicationHandler
from handler.operation.split import SplitHandler
from handler.operation.subtraction import SubtractionHandler
from handler.operation.textcase import TextcaseHandler
from handler.operation.comparison import ComparisonHandler

class OperationClient():
    handler: OperationHandler

    def __init__(self):
        adittion_handler = AdittionHandler()
        subtraction_handler = SubtractionHandler()
        multiplication_handler = MultiplicationHandler()
        split_handler = SplitHandler()
        textcase_handler = TextcaseHandler()
        comparison_handler = ComparisonHandler()

        adittion_handler.set_next(subtraction_handler)
        subtraction_handler.set_next(multiplication_handler)
        multiplication_handler.set_next(split_handler)
        split_handler.set_next(textcase_handler)
        textcase_handler.set_next(comparison_handler)

        self.handler = adittion_handler

    def handle(self, operation, parameter_provider):
        self.handler.handle(operation, parameter_provider)