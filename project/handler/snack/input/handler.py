from __future__ import annotations
from abc import ABC, abstractmethod

class SnackInputHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, snack_input, parameter_provider):
        pass

class AbstractSnackInputHandler(SnackInputHandler):
    _next_handler: SnackInputHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, snack_input, parameter_provider):
        if self._next_handler:
            return self._next_handler.handle(snack_input, parameter_provider)
        else:
            return None