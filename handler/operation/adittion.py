from handler.operation.handler import AbstractOperationHandler

class AdittionHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) == 3 and operation[1] == '+':
            lhs = float(operation[0])
            rhs = float(operation[2])
            operation_result = lhs + rhs
            parameter_provider.store_result(operation_result)
        else:
            super().handle(operation, parameter_provider)