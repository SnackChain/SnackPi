class AbstractSnackInputHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, snack_input, parameter_provider):
        if self._next_handler:
            return self._next_handler.handle(snack_input, parameter_provider)
        else:
            return None