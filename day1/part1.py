from typing import List

with open("input.txt") as file:
    lines = file.readlines()

list_1: List[int] = []
list_2: List[int] = []

for line in lines:
    id1 = int(line.split()[0].strip())
    list_1.append(id1)
    id2 = int(line.split()[1].strip())
    list_2.append(id2)

list_1.sort()
list_2.sort()

total_distance = 0
for i in range(len(list_1)):
    total_distance += abs(list_1[i] - list_2[i])

print(total_distance)
