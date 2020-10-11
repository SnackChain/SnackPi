from __future__ import annotations
from abc import ABC, abstractmethod

class OperationHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, operation, parameter_provider):
        pass

class AbstractOperationHandler(OperationHandler):
    _next_handler: OperationHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, operation, parameter_provider):
        if self._next_handler:
            self._next_handler.handle(operation, parameter_provider)

class SubtractionHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) == 3 and operation[1] == '-':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs - rhs
            parameter_provider.store_result(operation_result)
        else:
            super().handle(operation, parameter_provider)

class MultiplicationHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) == 3 and operation[1] == '*':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs * rhs
            parameter_provider.store_result(operation_result)
        else:
            super().handle(operation, parameter_provider)

class SplitHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) >= 3 and operation[1] == 'split':
            lhs = operation[0]
            rhs = operation[2]
            operation_results = lhs.split(rhs)
            for operation_result in operation_results:
                parameter_provider.store_result(operation_result)
        else:
            super().handle(operation, parameter_provider)

class TextcaseHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) == 3 and operation[1] == 'textcase':
            lhs = operation[0]
            rhs = operation[2]
            if rhs == 'uppercase':
                parameter_provider.store_result(lhs.upper())
            elif rhs == 'lowercase':
                parameter_provider.store_result(lhs.lower())
        else:
            super().handle(operation, parameter_provider)