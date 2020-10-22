from __future__ import annotations
from abc import ABC, abstractmethod

class EventTimeHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, event_time, method):
        pass

class AbstractEventTimeHandler(EventTimeHandler):
    _next_handler: EventTimeHandler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, event_time, method, *args):
        if self._next_handler:
            self._next_handler.handle(event_time, method, *args)
        else:
            return