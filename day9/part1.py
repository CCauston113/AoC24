with open("input.txt") as file:
    disk_map = file.readline()

disk = []

# Get disk layout
for i in range(len(disk_map)):
    if i % 2 == 0:  # file
        for block in range(int(disk_map[i])):
            disk.append(str(i//2))
    else:   # free space
        for block in range(int(disk_map[i])):
            disk.append('.')

free_spaces = disk.count('.')
finished = False

while not finished:
    end_index = len(disk) - 1
    while disk[end_index] == '.':
        end_index -= 1
        if end_index <= len(disk) - free_spaces - 1:
            finished = True     # All the free spaces are at the end
    if finished:
        break
    free_space = 0
    while disk[free_space] != '.':
        free_space += 1
    disk[free_space] = disk[end_index]
    disk[end_index] = '.'

print(disk)

checksum = 0
for i in range(len(disk)):
    if disk[i] == '.':
        break
    checksum += i * int(disk[i])

print(checksum)
