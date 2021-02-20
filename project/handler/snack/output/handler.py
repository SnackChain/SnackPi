class AbstractSnackOutputHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, snack_output, buffers, parameter_provider):
        if self._next_handler:
            self._next_handler.handle(snack_output, buffers, parameter_provider)
        else:
            return