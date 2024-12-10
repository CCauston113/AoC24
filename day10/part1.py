from typing import Set

with open("input.txt") as file:
    rows = file.readlines()

max_x = len(rows[0]) - 2
max_y = len(rows) - 1


class Coordinate:
    x: int
    y: int

    def __init__(self, row, column):
        self.x = column
        self.y = row

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self))


def find_set_of_next_height(target: str, current_points: Set[Coordinate]) -> Set[Coordinate]:
    next_points = set()
    for point in current_points:
        # left
        if point.x > 0 and rows[point.y][point.x-1] == target:
            next_points.add(Coordinate(row=point.y, column=point.x-1))
        # right
        if point.x < max_x and rows[point.y][point.x+1] == target:
            next_points.add(Coordinate(point.y, point.x+1))
        # up
        if point.y > 0 and rows[point.y-1][point.x] == target:
            next_points.add(Coordinate(point.y-1, point.x))
        # down
        if point.y < max_y and rows[point.y+1][point.x] == target:
            next_points.add(Coordinate(point.y+1, point.x))
    # print(f"target = {target}, points = {next_points}")
    return next_points


def check_trails(row, column) -> int:
    heights = "123456789"
    current_points = set()
    current_points.add(Coordinate(row=row, column=column))
    for height in heights:
        current_points = find_set_of_next_height(height, current_points)
    return len(current_points)


total_scores = 0
for i in range(max_y + 1):
    for j in range(max_x + 1):
        if rows[i][j] == '0':
            trails = check_trails(i, j)
            # print(trails)
            total_scores += trails

print(total_scores)
