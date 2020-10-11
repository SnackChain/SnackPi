from __future__ import annotations
from abc import ABC, abstractmethod

class InstructionHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, snack_instructions, parameter_provider):
        pass

class AbstractInstructionHandler(InstructionHandler):
    _next_handler: InstructionHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, snack_instructions, parameter_provider):
        if self._next_handler:
            self._next_handler.handle(snack_instructions, parameter_provider)
        