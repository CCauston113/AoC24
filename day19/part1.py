import re

with open("patterns.txt") as file:
    desired_patterns = file.readlines()

with open("options.txt") as file:
    options = file.readline().strip().split(', ')

regex_string = r"("
for option in options:
    regex_string = regex_string + '(' + option + ')' + '|'
regex_string = regex_string[:-1]
regex_string = regex_string + ")*$"
regex = re.compile(regex_string)

possible = 0
for pattern in desired_patterns:
    match = regex.match(pattern.strip())
    if match is not None:
        possible += 1
        print(possible)

print(possible)
