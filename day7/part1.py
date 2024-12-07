import numpy


def do_the_maths(values, operators: str, target_value) -> bool:
    answer = int(values[0])
    for bit in range(len(operators)):
        if operators[bit] == '0':
            answer = answer + int(values[bit+1])
        elif operators[bit] == '1':
            answer = answer * int(values[bit+1])
        if answer > int(target_value):
            return False
    return answer == int(target_value)


with open("input.txt") as file:
    equations = file.readlines()

total = 0
for equation in equations:
    success = False
    test_value, rest = equation.split(':')
    calibration_values = rest.strip().split(' ')
    num_operators = len(calibration_values) - 1
    for i in range(pow(2, num_operators)):
        binary = numpy.binary_repr(i, num_operators)
        success = do_the_maths(calibration_values, binary, test_value)
        if success:
            total += int(test_value)
            break

print(total)
