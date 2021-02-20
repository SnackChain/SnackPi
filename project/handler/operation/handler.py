class AbstractOperationHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, operation, parameter_provider):
        if self._next_handler:
            self._next_handler.handle(operation, parameter_provider)