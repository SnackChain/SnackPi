from handler.operation.handler import AbstractOperationHandler
import math

class TruncateHandler(AbstractOperationHandler):
	def handle(self, operation, parameter_provider):
		if len(operation) == 3 and isinstance(operation[1], str) and operation[1] == 'truncate':
			lhs = float(operation[0])
			rhs = operation[2]
			number = self.truncate(lhs, rhs)
			parameter_provider.store_result(number)
		else:
			super().handle(operation, parameter_provider)

	def truncate(self, number, digits) -> float:
		stepper = 10.0 ** digits
		return math.trunc(stepper * number) / stepper