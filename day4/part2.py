def check_up(start_x, start_y) -> int:
    if rows[start_y+1][start_x] != 'M':
        return 0
    if rows[start_y-1][start_x] != 'S':
        return 0
    return 1


def check_down(start_x, start_y) -> int:
    if rows[start_y-1][start_x] != 'M':
        return 0
    if rows[start_y+1][start_x] != 'S':
        return 0
    return 1


def check_right(start_x, start_y) -> int:
    if rows[start_y][start_x-1] != 'M':
        return 0
    if rows[start_y][start_x+1] != 'S':
        return 0
    return 1


def check_left(start_x, start_y) -> int:
    if rows[start_y][start_x+1] != 'M':
        return 0
    if rows[start_y][start_x-1] != 'S':
        return 0
    return 1


def check_up_right(start_x, start_y) -> int:
    if rows[start_y+1][start_x-1] != 'M':
        return 0
    if rows[start_y-1][start_x+1] != 'S':
        return 0
    return 1


def check_up_left(start_x, start_y) -> int:
    if rows[start_y+1][start_x+1] != 'M':
        return 0
    if rows[start_y-1][start_x-1] != 'S':
        return 0
    return 1


def check_down_right(start_x, start_y) -> int:
    if rows[start_y-1][start_x-1] != 'M':
        return 0
    if rows[start_y+1][start_x+1] != 'S':
        return 0
    return 1


def check_down_left(start_x, start_y) -> int:
    if rows[start_y-1][start_x+1] != 'M':
        return 0
    if rows[start_y+1][start_x-1] != 'S':
        return 0
    return 1


with open("input.txt") as file:
    rows = file.readlines()

max_row = len(rows) - 1
max_col = len(rows[0]) - 2
num_found = 0
for row in range(1, max_row):
    for col in range(1, max_col):
        if rows[row][col] == 'A':
            found = (((check_up(col, row) or check_down(col, row)) and
                     (check_left(col, row) or check_right(col, row))) +
                     ((check_up_left(col, row) or check_down_right(col, row)) and
                     (check_down_left(col, row) or check_up_right(col, row))))
            num_found += found

print(num_found)
