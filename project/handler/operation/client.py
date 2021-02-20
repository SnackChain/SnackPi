from handler.operation.adittion import AdittionHandler
from handler.operation.multiplication import MultiplicationHandler
from handler.operation.split import SplitHandler
from handler.operation.subtraction import SubtractionHandler
from handler.operation.textcase import TextcaseHandler
from handler.operation.comparison import ComparisonHandler
from handler.operation.truncate import TruncateHandler
from handler.directive.handler import AbstractDirectiveHandler

class OperationClient(AbstractDirectiveHandler):
    handler = None

    def __init__(self):
        adittion_handler = AdittionHandler()
        subtraction_handler = SubtractionHandler()
        multiplication_handler = MultiplicationHandler()
        split_handler = SplitHandler()
        textcase_handler = TextcaseHandler()
        comparison_handler = ComparisonHandler()
        truncate_handler = TruncateHandler()

        adittion_handler.set_next(subtraction_handler)
        subtraction_handler.set_next(multiplication_handler)
        multiplication_handler.set_next(split_handler)
        split_handler.set_next(textcase_handler)
        textcase_handler.set_next(comparison_handler)
        comparison_handler.set_next(truncate_handler)

        self.handler = adittion_handler

    def handle(self, directive, parameter_provider, snack_manager):
        if directive.type == "operation":
            for operation in directive.data:
                value = parameter_provider.get_values_from_dynamic(operation)
                self.handler.handle(operation, parameter_provider)
        else:
            super().handle(directive, parameter_provider, snack_manager)