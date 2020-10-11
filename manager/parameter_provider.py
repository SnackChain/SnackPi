class ParametersData:
    result_key = 'r'
    values_key = 'v'
    sensor_key = 's'

    operatorsKeys = [result_key, values_key, sensor_key]

    data = {result_key: {}, values_key: {}, sensor_key: {}}

    def add(self, key, value):
        if key in self.operatorsKeys:
            lenght = len(self.data[key])
            parameterKey = key + str(lenght)
            self.data[key][parameterKey] = value

# This replace dynamic values, such as v0, v1, v2, r0, r1, s1, s2... for the real values
class ParameterProvider():
    parameters = ParametersData()

    def get_value_from_dynamic(self, _operation):
        real_value = _operation
        #["v0", "split", "_"]
        # for index = 0
        for index, operation in enumerate(_operation):
            if isinstance(operation, str):
                #operator = 'v'
                operator = operation[0]
                #if operator in self.parameters.operatorsKeys:
                if operator in self.parameters.operatorsKeys and operation in self.parameters.data[operator]:
                    #newOperations[0] = parameters.data['v']['v0']
                    real_value[index] = self.parameters.data[operator][operation]
        return real_value

    def store_value(self, value):
        self.parameters.add(self.parameters.values_key, value)

    def store_result(self, value):
        self.parameters.add(self.parameters.result_key, value)

    def store_sensor(self, value):
        self.parameters.add(self.parameters.sensor_key, value)