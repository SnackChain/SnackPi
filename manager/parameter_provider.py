class ParametersData:
    result_key = 'r'
    values_key = 'v'
    sensor_key = 's'

    operatorsKeys = [result_key, values_key, sensor_key]

    data = {result_key: {}, values_key: {}, sensor_key: {}}

    def add(key, value):
        if key in operatorsKeys:
            lenght = len(self.data[key])
            parameterKey = key + str(lenght - 1)
            self.data[parameterKey] = value

# This replace dynamic values, such as v0, v1, v2, r0, r1, s1, s2... for the real values
class ParametersDataProvider():
    def get_operation(parameters: ParametersData, _operation):
        newOperation = _operation
        #["v0", "split", "_"]
        # for index = 0
        for index, operation in enumerate(_operation):
            #operator = 'v'
            operator = operation[0]
            if operator in parameters.operatorsKeys:
                #newOperations[0] = parameters.data['v']['v0']
                newOperation[index] = parameters.data[operator][operation]
        return newOperation