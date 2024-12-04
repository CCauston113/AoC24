import re

with open("input.txt") as file:
    data = file.read()

regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
instructions = regex.findall(data)

total = 0
for instruction in instructions:
    a = instruction.split(',')[0].split('(')[1]
    b = instruction.split(',')[1].split(')')[0]
    product = int(a) * int(b)
    total += product

print(total)
