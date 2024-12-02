from typing import List, Dict

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

appearances: Dict[int, int] = {}
i = 0
while i < len(list_2):
    num = list_2[i]
    times = 1
    if i < len(list_2) - 1:
        while list_2[i+1] == num:
            i += 1
            times += 1
            if i == len(list_2) - 1:
                break
    appearances[num] = times
    i += 1

similarity_score = 0
for j in list_1:
    if j in appearances:
        similarity_score += j * appearances[j]

print(similarity_score)
