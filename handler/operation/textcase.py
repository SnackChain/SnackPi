from handler.operation.handler import AbstractOperationHandler

class TextcaseHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) == 3 and isinstance(operation[1], str) and operation[1] == 'textcase':
            lhs = operation[0]
            rhs = operation[2]
            if rhs == 'uppercase':
                parameter_provider.store_result(lhs.upper())
            elif rhs == 'lowercase':
                parameter_provider.store_result(lhs.lower())
        else:
            super().handle(operation, parameter_provider)