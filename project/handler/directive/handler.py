class AbstractDirectiveHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, directive, parameter_provider, snack_manager):
        if self._next_handler:
            self._next_handler.handle(directive, parameter_provider, snack_manager)