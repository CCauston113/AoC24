from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


with open("input.txt") as file:
    lines = file.readlines()

x_pos: int = 0
y_pos = 0
for i in range(len(lines)):
    for j in range(len(lines[0])-1):
        if lines[i][j] == '^':
            x_pos = j
            y_pos = i

facing = Direction.NORTH
lines[y_pos] = lines[y_pos][:x_pos] + 'X' + lines[y_pos][x_pos+1:]
while True:
    match facing:
        case Direction.NORTH:
            if y_pos == 0:
                break
            if lines[y_pos-1][x_pos] == '#':
                facing = Direction.EAST
            else:
                y_pos -= 1
                lines[y_pos] = lines[y_pos][:x_pos] + 'X' + lines[y_pos][x_pos+1:]
        case Direction.EAST:
            if x_pos == len(lines[0]) - 2:
                break
            if lines[y_pos][x_pos+1] == '#':
                facing = Direction.SOUTH
            else:
                x_pos += 1
                lines[y_pos] = lines[y_pos][:x_pos] + 'X' + lines[y_pos][x_pos+1:]
        case Direction.SOUTH:
            if y_pos == len(lines) - 1:
                break
            if lines[y_pos + 1][x_pos] == '#':
                facing = Direction.WEST
            else:
                y_pos += 1
                lines[y_pos] = lines[y_pos][:x_pos] + 'X' + lines[y_pos][x_pos+1:]
        case Direction.WEST:
            if x_pos == 0:
                break
            if lines[y_pos][x_pos - 1] == '#':
                facing = Direction.NORTH
            else:
                x_pos -= 1
                lines[y_pos] = lines[y_pos][:x_pos] + 'X' + lines[y_pos][x_pos+1:]

visited = 0
for line in lines:
    for column in line:
        if column == 'X':
            visited += 1

print(visited)
