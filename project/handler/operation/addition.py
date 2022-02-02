from handler.operation.handler import AbstractOperationHandler

class AdditionHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) == 3 and isinstance(operation[1], str) and operation[1] == '+':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs + rhs
            parameter_provider.store_result(operation_result)
        else:
            super().handle(operation, parameter_provider)