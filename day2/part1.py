with open("input.txt") as file:
    reports = file.readlines()

num_safe = 0
for report in reports:
    levels = report.split()
    increase_found = False
    decrease_found = False
    safe = True
    for i in range(1, len(levels)):
        prev = int(levels[i-1])
        new = int(levels[i])
        if new > prev:
            increase_found = True
        elif new < prev:
            decrease_found = True
        if increase_found and decrease_found:
            safe = False
            break
        diff = abs(new - prev)
        if diff > 3 or diff == 0:
            safe = False
            break
    if safe is True:
        num_safe += 1

print(num_safe)
