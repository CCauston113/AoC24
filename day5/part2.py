import math
from typing import Dict, List
from functools import cmp_to_key

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


def check_update(page_list: List[str]) -> bool:
    for page in range(len(page_list) - 1):
        for other in range(page, len(page_list)):
            if page_list[other] in rules:
                if page_list[page] in list(rules.get(page_list[other])):
                    return False
    return True


def compare(page1, page2) -> int:
    if page1 in rules:
        if page2 in rules.get(page1):
            return 1  # page 2 comes after
    if page2 in rules:
        if page1 in rules.get(page2):
            return -1  # page 1 comes after
    return 0


total = 0
for update in updates:
    pages = update.strip().split(',')
    if check_update(pages) is False:
        new_list = sorted(pages, key=cmp_to_key(compare))
        middle_index = math.floor(len(new_list) / 2)
        total += int(new_list[middle_index])

print(total)
