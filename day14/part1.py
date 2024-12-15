from typing import List, Tuple

HEIGHT = 103
WIDTH = 101

with open("input.txt") as file:
    lines = file.readlines()

robots: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
for line in lines:
    pos_x = int(line.split('=')[1].split(',')[0])
    pos_y = int(line.split(',')[1].split()[0])
    v_x = int(line.split('=')[2].split(',')[0])
    v_y = int(line.split(',')[2].strip())
    robots.append(((pos_x, pos_y), (v_x, v_y)))

for sec in range(100):
    for i in range(len(robots)):
        robot = robots[i]
        new_px = (robot[0][0] + robot[1][0]) % WIDTH
        new_py = (robot[0][1] + robot[1][1]) % HEIGHT
        robots[i] = ((new_px, new_py), robot[1])

# calculate quadrants
x_mid = (WIDTH - 1)/2
y_mid = (HEIGHT - 1)/2
top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0
for robot in robots:
    x = robot[0][0]
    y = robot[0][1]
    if x < x_mid and y < y_mid:
        top_left += 1
    elif x < x_mid and y > y_mid:
        bottom_left += 1
    elif x > x_mid and y < y_mid:
        top_right += 1
    elif x > x_mid and y > y_mid:
        bottom_right += 1

print(top_left * top_right * bottom_right * bottom_left)
