from handler.operation.handler import AbstractOperationHandler

class SplitHandler(AbstractOperationHandler):
    def handle(self, operation, parameter_provider):
        if len(operation) >= 3 and operation[1] == 'split':
            lhs = operation[0]
            rhs = operation[2]
            operation_results = lhs.split(rhs)
            for operation_result in operation_results:
                parameter_provider.store_result(operation_result)
        else:
            super().handle(operation, parameter_provider)