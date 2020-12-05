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