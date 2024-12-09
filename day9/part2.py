with open("input.txt") as file:
    disk_map = file.readline()

disk = []

max_fileid = 0
# Get disk layout
for i in range(len(disk_map)):
    if i % 2 == 0:  # file
        for block in range(int(disk_map[i])):
            disk.append(str(i//2))
            max_fileid = i//2
    else:   # free space
        for block in range(int(disk_map[i])):
            disk.append('.')

for file in range(max_fileid, -1, -1):
    print(f"fileid = {file}")
    # find the start index and the length
    start_index = 0
    length = 0
    for block in range(len(disk)):
        if disk[block] == '.':
            if length > 0:
                break
        elif int(disk[block]) == file:
            if length == 0:
                start_index = block
            length += 1
    new_index = 0
    gap = 0
    for block in range(len(disk)):
        if block >= start_index:
            gap = 0
            break
        if disk[block] != '.':
            if gap >= length:
                break
            elif gap > 0:
                gap = 0
        else:
            if gap == 0:
                new_index = block
            gap += 1

    if gap >= length:
        for block in range(new_index, new_index+length, 1):
            disk[block] = str(file)
        for block in range(start_index, start_index+length, 1):
            disk[block] = '.'

checksum = 0
for i in range(len(disk)):
    if disk[i] != '.':
        checksum += i * int(disk[i])

print(checksum)
