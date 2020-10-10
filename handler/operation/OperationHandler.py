from __future__ import annotations
from abc import ABC, abstractmethod

class OperationClient():
    handler: OperationHandler

    def __init__(self):
        adittion_handler = AdittionHandler()
        subtraction_handler = SubtractionHandler()
        multiplication_handler = MultiplicationHandler()
        split_handler = SplitHandler()

        multiplication_handler.set_next(split_handler)
        subtraction_handler.set_next(multiplication_handler)
        adittion_handler.set_next(subtraction_handler)

        self.handler = adittion_handler

    def do_operation(self, operation, parameters: ParametersData):
        self.handler.handle(operation, parameters)

class OperationHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, operation, result):
        pass

class AbstractOperationHandler(OperationHandler):
    _next_handler: OperationHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, operation, result):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class AdittionHandler(AbstractOperationHandler):
    def handle(self, operation, parameters: ParametersData):
        if operation.len() == 3 and operation[1] == '+':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs + rhs
            parameters.add(parameters.result_key, operation_result)
        else:
            super().handle(request)

class SubtractionHandler(AbstractOperationHandler):
    def handle(self, operation, parameters: ParametersData):
        if operation.len() == 3 and operation[1] == '-':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs - rhs
            parameters.add(parameters.result_key, operation_result)
        else:
            super().handle(request)

class MultiplicationHandler(AbstractOperationHandler):
    def handle(self, operation, parameters: ParametersData):
        if operation.len() == 3 and operation[1] == '*':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs * rhs
            parameters.add(parameters.result_key, operation_result)
        else:
            super().handle(request)

class SplitHandler(AbstractOperationHandler):
    def handle(self, operation, parameters: ParametersData):
        if operation.len() == 3 and operation[1] == 'split':
            lhs = peration[0]
            rhs = operation[2]
            operation_results = lhs.split(rhs)
            for operation_result in operation_results:
                parameters.add(parameters.result_key, operation_result)
        else:
            super().handle(request)