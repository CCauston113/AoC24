from typing import List

with open("input.txt") as file:
    stones: List[str] = file.readline().strip().split()


def blink(rocks: List[str]) -> List[str]:
    new_rocks = []
    for rock in rocks:
        if rock == '0':
            new_rocks.append('1')
        elif len(rock) % 2 == 0:
            midpoint = int(len(rock)/2)
            new_rocks.append(rock[:midpoint])
            new_rocks.append(str(int(rock[midpoint:])))
        else:
            new_rocks.append(str(int(rock) * 2024))
    return new_rocks


for i in range(25):
    stones = blink(stones[:])

print(len(stones))
