from typing import Dict

with open("input.txt") as file:
    line = file.readline().strip().split()

stones: Dict[str, int] = {}
for stone in line:
    if stone in stones:
        stones[stone] = stones[stone] + 1
    else:
        stones[stone] = 1


def blink(rocks: Dict[str, int]) -> Dict[str, int]:
    new_rocks = {}
    for rock_type in rocks:
        if rock_type == '0':
            new_rocks['1'] = (new_rocks['1'] if '1' in new_rocks else 0) + rocks[rock_type]
        elif len(rock_type) % 2 == 0:
            midpoint = int(len(rock_type) / 2)
            new_rocks[rock_type[:midpoint]] = (new_rocks[rock_type[:midpoint]] if rock_type[:midpoint] in new_rocks
                                               else 0) + rocks[rock_type]
            new_rocks[str(int(rock_type[midpoint:]))] = (new_rocks[str(int(rock_type[midpoint:]))]
                                                         if str(int(rock_type[midpoint:])) in new_rocks
                                                         else 0) + rocks[rock_type]
        else:
            new_rocks[str(int(rock_type) * 2024)] = (new_rocks[str(int(rock_type) * 2024)]
                                                     if str(int(rock_type) * 2024) in new_rocks
                                                     else 0) + rocks[rock_type]
    return new_rocks


print(stones)
for i in range(75):
    stones = blink(stones.copy())
    print(stones)

total_stones = 0
for stone in stones:
    total_stones += stones[stone]

print(total_stones)
