def check_up(start_x, start_y) -> int:
    if start_y < 3:
        return 0
    if rows[start_y-1][start_x] != 'M':
        return 0
    if rows[start_y-2][start_x] != 'A':
        return 0
    if rows[start_y-3][start_x] != 'S':
        return 0
    return 1


def check_down(start_x, start_y, max_y) -> int:
    if start_y > max_y - 3:
        return 0
    if rows[start_y+1][start_x] != 'M':
        return 0
    if rows[start_y+2][start_x] != 'A':
        return 0
    if rows[start_y+3][start_x] != 'S':
        return 0
    return 1


def check_right(start_x, start_y, max_x) -> int:
    if start_x > max_x - 3:
        return 0
    if rows[start_y][start_x+1] != 'M':
        return 0
    if rows[start_y][start_x+2] != 'A':
        return 0
    if rows[start_y][start_x+3] != 'S':
        return 0
    return 1


def check_left(start_x, start_y) -> int:
    if start_x < 3:
        return 0
    if rows[start_y][start_x-1] != 'M':
        return 0
    if rows[start_y][start_x-2] != 'A':
        return 0
    if rows[start_y][start_x-3] != 'S':
        return 0
    return 1


def check_up_right(start_x, start_y, max_x) -> int:
    if start_x > max_x - 3 or start_y < 3:
        return 0
    if rows[start_y-1][start_x+1] != 'M':
        return 0
    if rows[start_y-2][start_x+2] != 'A':
        return 0
    if rows[start_y-3][start_x+3] != 'S':
        return 0
    return 1


def check_up_left(start_x, start_y) -> int:
    if start_x < 3 or start_y < 3:
        return 0
    if rows[start_y-1][start_x-1] != 'M':
        return 0
    if rows[start_y-2][start_x-2] != 'A':
        return 0
    if rows[start_y-3][start_x-3] != 'S':
        return 0
    return 1


def check_down_right(start_x, start_y, max_x, max_y) -> int:
    if start_x > max_x - 3 or start_y > max_y - 3:
        return 0
    if rows[start_y+1][start_x+1] != 'M':
        return 0
    if rows[start_y+2][start_x+2] != 'A':
        return 0
    if rows[start_y+3][start_x+3] != 'S':
        return 0
    return 1


def check_down_left(start_x, start_y, max_y) -> int:
    if start_x < 3 or start_y > max_y - 3:
        return 0
    if rows[start_y+1][start_x-1] != 'M':
        return 0
    if rows[start_y+2][start_x-2] != 'A':
        return 0
    if rows[start_y+3][start_x-3] != 'S':
        return 0
    return 1


with open("input.txt") as file:
    rows = file.readlines()

num_found = 0
max_row = len(rows)-1
max_col = len(rows[0])-2
for row in range(max_row+1):
    for column in range(max_col+1):
        if rows[row][column] == 'X':
            found = (check_up(column, row) + check_down(column, row, max_row) +
                     check_right(column, row, max_col) + check_left(column, row) +
                     check_up_right(column, row, max_col) + check_up_left(column, row) +
                     check_down_right(column, row, max_col, max_row) +
                     check_down_left(column, row, max_row))
            num_found += found

print(num_found)
