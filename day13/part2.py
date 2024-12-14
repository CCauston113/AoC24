from typing import List, Tuple

A_COST = 3
B_COST = 1


class Game:
    button_a: Tuple[int, int]
    button_b: Tuple[int, int]
    prize: Tuple[int, int]

    def __str__(self):
        return f"A: {self.button_a}, B: {self.button_b}, prize: {self.prize}"

    def __repr__(self):
        return f"A: {self.button_a}, B: {self.button_b}, prize: {self.prize}"

    def get_b(self):
        temp_b = (self.prize[0] * self.button_a[1] - self.button_a[0] * self.prize[1])/(
                self.button_a[1] * self.button_b[0] - self.button_a[0] * self.button_b[1])
        if temp_b % 1 == 0:
            return temp_b
        else:
            return -1

    def get_a(self, b):
        temp_a = (self.prize[0] - self.button_b[0] * b)/self.button_a[0]
        if temp_a % 1 == 0:
            return temp_a
        else:
            return -1


games: List[Game] = []


def get_xy(xy_line: str) -> Tuple[int, int]:
    x = xy_line.split('X')[1].split(',')[0]
    x = int(x[1:])
    y = xy_line.split('Y')[1].strip()
    y = int(y[1:])
    return x, y


with open("input.txt") as file:
    line = "\n"
    while line != "":
        game = Game()
        # button a
        line = file.readline()
        game.button_a = get_xy(line[:])
        # button b
        line = file.readline()
        game.button_b = get_xy(line[:])
        # prize
        line = file.readline()
        prize = get_xy(line[:])
        game.prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
        games.append(game)
        # empty line
        line = file.readline()

print(games)

total_tokens = 0
for game in games:
    b = game.get_b()
    if b == -1:
        continue
    a = game.get_a(b)
    if a == -1:
        continue
    tokens = a * A_COST + b * B_COST
    total_tokens += tokens

print(total_tokens)
