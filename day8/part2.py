from typing import Dict, List, Tuple

antennas: Dict[str, List[Tuple[int, int]]] = {}

with open("input.txt") as file:
    contents = file.readlines()

max_y = len(contents) - 1
max_x = len(contents[0]) - 2


def check_in_grid(x, y) -> bool:
    if 0 <= x <= max_x and 0 <= y <= max_y:
        return True
    else:
        return False


for y in range(max_y + 1):
    for x in range(max_x + 1):
        if contents[y][x] != '.':
            freq = contents[y][x]
            if freq in antennas:
                antennas[freq].append((x, y))
            else:
                antennas[freq] = [(x, y)]

antinodes = set()
for freq in antennas:
    if len(antennas[freq]) > 1:
        for first in range(len(antennas[freq])-1):
            for second in range(first + 1, len(antennas[freq])):
                x_distance = antennas[freq][second][0] - antennas[freq][first][0]
                y_distance = antennas[freq][second][1] - antennas[freq][first][1]
                potential1 = antennas[freq][first]
                while check_in_grid(potential1[0], potential1[1]):
                    antinodes.add(potential1)
                    potential1 = (potential1[0] - x_distance, potential1[1] - y_distance)
                potential2 = antennas[freq][second]
                while check_in_grid(potential2[0], potential2[1]):
                    antinodes.add(potential2)
                    potential2 = (potential2[0] + x_distance, potential2[1] + y_distance)
    print(antinodes)

print(len(antinodes))
