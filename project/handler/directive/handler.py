from __future__ import annotations
from abc import ABC, abstractmethod

class DirectiveHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, directive, parameter_provider, i2c_provider):
        pass

class AbstractDirectiveHandler(DirectiveHandler):
    _next_handler: OperationHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, directive, parameter_provider, i2c_provider):
        if self._next_handler:
            self._next_handler.handle(directive, parameter_provider, i2c_provider)