from typing import List

reg_A = 0
reg_B = 0
reg_C = 0
instruction_pointer = 0


def get_combo(operand: int):
    match operand:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return reg_A
        case 5:
            return reg_B
        case 6:
            return reg_C
        case _:
            print("ERROR")
            SystemExit()


def adv(operand: int):
    global reg_A
    numerator = reg_A
    denominator = pow(2, get_combo(operand))
    result = numerator//denominator
    reg_A = result


def bxl(operand: int):
    global reg_B
    reg_B = reg_B ^ operand


def bst(operand: int):
    global reg_B
    combo = get_combo(operand)
    reg_B = combo % 8


def jnz(operand: int):
    global reg_A
    global instruction_pointer
    if reg_A == 0:
        return False
    else:
        instruction_pointer = operand
        return True


def bxc(operand: int):
    global reg_B
    global reg_C
    reg_B = reg_B ^ reg_C
    return operand  # but don't use it


def out(operand: int, output: List[str]):
    value = get_combo(operand) % 8
    output.append(str(value))
    return output


def bdv(operand: int):
    global reg_A
    global reg_B
    numerator = reg_A
    denominator = pow(2, get_combo(operand))
    result = numerator//denominator
    reg_B = result


def cdv(operand: int):
    global reg_A
    global reg_C
    numerator = reg_A
    denominator = pow(2, get_combo(operand))
    result = numerator//denominator
    reg_C = result


with open("input.txt") as file:
    file.readline()  # ignore A
    b = int(file.readline().split()[2].strip())
    c = int(file.readline().split()[2].strip())
    file.readline()  # blank
    program = file.readline().split()[1].strip().split(',')
    print(program) 

a = 100142915
output: List[str] = []
while True:
    reg_A = a
    reg_B = b
    reg_C = c
    print(f"A={str(reg_A)}")
    output: List[str] = []
    while instruction_pointer < len(program) - 1:
        opcode = int(program[instruction_pointer])
        operand = int(program[instruction_pointer+1])
        match opcode:
            case 0:
                adv(operand)
                instruction_pointer += 2
            case 1:
                bxl(operand)
                instruction_pointer += 2
            case 2:
                bst(operand)
                instruction_pointer += 2
            case 3:
                jumped = jnz(operand)
                if jumped is False:
                    instruction_pointer += 2
            case 4:
                bxc(operand)
                instruction_pointer += 2
            case 5:
                output = out(operand, output[:])
                instruction_pointer += 2
            case 6:
                bdv(operand)
                instruction_pointer += 2
            case 7:
                cdv(operand)
                instruction_pointer += 2
    if output == program:
        break
    a += 1
    output.clear()
    instruction_pointer = 0
