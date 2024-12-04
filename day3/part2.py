import re

with open("input.txt") as file:
    data = file.read()

multiply = r'mul\(\d{1,3},\d{1,3}\)'
do = r'do\(\)'
do_not = r'don\'t\(\)'
regex = re.compile(r'(%s|%s|%s)' % (multiply, do, do_not))
instructions = regex.findall(data)

total = 0
enabled = True
for instruction in instructions:
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled is True:
            a = instruction.split(',')[0].split('(')[1]
            b = instruction.split(',')[1].split(')')[0]
            product = int(a) * int(b)
            total += product

print(total)
