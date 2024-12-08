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


def maths_with_concat(values, operators: str, target_value) -> bool:
    if do_the_maths(values, operators, target_value):
        return True
    for operator in range(len(operators)):
        temp_operators = operators[:operator] + '2' + operators[operator+1:]
        val = int(values[0])
        for bit in range(len(temp_operators)):
            if temp_operators[bit] == '0':
                val = val + int(values[bit+1])
            elif temp_operators[bit] == '1':
                val = val * int(values[bit+1])
            elif temp_operators[bit] == '2':
                val = int(str(val) + values[bit+1])
        if val == int(target_value):
            return True
    return False


with open("input.txt") as file:
    equations = file.readlines()

total = 0
solved = []
for equation in equations:
    success = False
    test_value, rest = equation.split(':')
    calibration_values = rest.strip().split(' ')
    num_operators = len(calibration_values) - 1
    for i in range(pow(2, num_operators)):
        binary = numpy.binary_repr(i, num_operators)
        success = maths_with_concat(calibration_values, binary, test_value)
        if success:
            total += int(test_value)
            solved.append(equation)
            break
    if success is False:
        with open("bad_equations.txt", "a") as file:
            file.writelines(equation)

print(total)
