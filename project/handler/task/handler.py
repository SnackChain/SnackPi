class AbstractInstructionHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, snack_instruction, parameter_provider):
        if self._next_handler:
            self._next_handler.handle(snack_instruction, parameter_provider)