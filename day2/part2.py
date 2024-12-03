def check_report(levels) -> (bool, int):
    increase_found = False
    decrease_found = False
    good = True
    for i in range(1, len(levels)):
        prev = int(levels[i - 1])
        new = int(levels[i])
        if new > prev:
            increase_found = True
        elif new < prev:
            decrease_found = True
        if increase_found and decrease_found:
            good = False
            break
        diff = abs(new - prev)
        if diff > 3 or diff == 0:
            good = False
            break
    return good, i


with open("input.txt") as file:
    reports = file.readlines()

num_safe = 0
for report in reports:
    values = report.split()
    safe, pos_stopped = check_report(values)
    recheck_safe = True
    if safe is False:
        # Remove value before failure
        alt1 = (values[:pos_stopped - 1] if pos_stopped > 1 else []) + values[pos_stopped:]
        recheck_safe, _ = check_report(alt1)
        if recheck_safe is False:
            # Remove current value
            alt2 = values[:pos_stopped] + (values[pos_stopped + 1:] if pos_stopped < len(values)-1 else [])
            recheck_safe, _ = check_report(alt2)
            if recheck_safe is False and pos_stopped == 2:
                alt3 = values[1:]
                recheck_safe, _ = check_report(alt3)
    if safe is True or recheck_safe is True:
        num_safe += 1


print(num_safe)
