from __future__ import annotations
from abc import ABC, abstractmethod

class SnackOutputHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, snack_output, buffers, parameter_provider):
        pass

class AbstractSnackOutputHandler(SnackOutputHandler):
    _next_handler: SnackOutputHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, snack_output, buffers, parameter_provider):
        if self._next_handler:
            self._next_handler.handle(snack_output, buffers, parameter_provider)
        else:
            return