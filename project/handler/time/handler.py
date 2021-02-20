class AbstractEventTimeHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, event_time, method, *args):
        if self._next_handler:
            self._next_handler.handle(event_time, method, *args)
        else:
            return