from handler.operation.handler import AbstractOperationHandler

class ComparisonHandler(AbstractOperationHandler):
	def handle(self, operation, parameter_provider):
		if len(operation) == 3 and isinstance(operation[1], str):
			comparison = operation[1]
			if comparison == '>' or comparison == '<' or comparison == '==' or comparison == '>=' or comparison == '<=':
				lhs = float(operation[0])
				rhs = float(operation[2])
				operation_result = False
				if comparison == '>':
					operation_result = lhs > rhs
				elif comparison == '<':
					operation_result = lhs < rhs
				elif comparison == '==':
					operation_result = lhs == rhs
				elif comparison == '>=':
					operation_result = lhs >= rhs
				elif comparison == '<=':
					operation_result = lhs <= rhs
				parameter_provider.store_result(operation_result)
			else:
				super().handle(operation, parameter_provider)
		else:
			super().handle(operation, parameter_provider)