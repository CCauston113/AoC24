import math
from typing import Dict, List

with open("instructions.txt") as file:
    updates = file.readlines()

rules: Dict[str, List[str]] = {}
with open("rules.txt") as file:
    rule_strings = file.readlines()
for rule in rule_strings:
    first, second = rule.strip().split('|')
    if first in rules:
        rules[first].append(second)
    else:
        rules[first] = [second]
print(rules)


def check_update(page_list: List[str]) -> bool:
    for page in range(len(page_list) - 1):
        for compare in range(page, len(page_list)):
            if page_list[compare] in rules:
                if page_list[page] in list(rules.get(page_list[compare])):
                    return False
    return True


total = 0
for update in updates:
    pages = update.strip().split(',')
    middle_index = math.floor(len(pages)/2)
    if check_update(pages):
        print(pages)
        total += int(pages[middle_index])

print(total)
