from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


with open("input.txt") as file:
    rows = file.readlines()

start_x: int = 0
start_y = 0
for i in range(len(rows)):
    for j in range(len(rows[0])-1):
        if rows[i][j] == '^':
            start_x = j
            start_y = i


def check_loop(lines, x_pos: int, y_pos: int, x_block, y_block) -> bool:
    if x_block == x_pos and y_block == y_pos:
        return False
    if lines[y_block][x_block] == '#':
        return False
    lines[y_block] = lines[y_block][:x_block] + '#' + lines[y_block][x_block+1:]
    path: List[Tuple[Tuple[int, int], Direction]] = []
    facing = Direction.NORTH
    while True:
        if ((x_pos, y_pos), facing) in path:
            return True
        path.append(((x_pos, y_pos), facing))
        match facing:
            case Direction.NORTH:
                if y_pos == 0:
                    return False
                clear_exit = True
                for pos in range(y_pos):
                    if lines[pos][x_pos] == '#':
                        clear_exit = False
                        break
                if clear_exit is True:
                    return False
                if lines[y_pos-1][x_pos] == '#':
                    facing = Direction.EAST
                else:
                    y_pos -= 1
            case Direction.EAST:
                if x_pos == len(lines[0]) - 2:
                    return False
                clear_exit = True
                for pos in range(x_pos, len(lines[0])-1):
                    if lines[y_pos][pos] == '#':
                        clear_exit = False
                        break
                if clear_exit is True:
                    return False
                if lines[y_pos][x_pos+1] == '#':
                    facing = Direction.SOUTH
                else:
                    x_pos += 1
            case Direction.SOUTH:
                if y_pos == len(lines) - 1:
                    return False
                clear_exit = True
                for pos in range(y_pos+1, len(lines)):
                    if lines[pos][x_pos] == '#':
                        clear_exit = False
                        break
                if clear_exit is True:
                    return False
                if lines[y_pos + 1][x_pos] == '#':
                    facing = Direction.WEST
                else:
                    y_pos += 1
            case Direction.WEST:
                if x_pos == 0:
                    return False
                clear_exit = True
                for pos in range(x_pos):
                    if lines[y_pos][pos] == '#':
                        clear_exit = False
                        break
                if clear_exit is True:
                    return False
                if lines[y_pos][x_pos - 1] == '#':
                    facing = Direction.NORTH
                else:
                    x_pos -= 1


options = 0
for i in range(len(rows)):
    for j in range(len(rows[0])-1):
        print(f"checking {j} {i}")
        loop = check_loop(rows[:], start_x, start_y, j, i)
        if loop:
            options += 1

print(options)
