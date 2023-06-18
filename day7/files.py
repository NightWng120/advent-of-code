def recursion(dir, directs):
    sum = 0
    for item in directs[dir]:
        if 'dir' in item:
            sum += recursion(item[1], directs)
        else:
            sum += int(item[0])
    print(f'Sum of {dir}: {sum}')
    return sum





with open('data.txt', 'r') as f:
    data = [item.replace('\n', '') for item in f.readlines()]
# Find cd and put directory name in a buffer list
# Put all directories and files after ls in a list(splitting size/dir with name of item) in a dictionary with the last element in the buffer being the key
# if directory is .. or ls, continue

directories = {}
buffer = []
name = ""
print(data)
for item in data:
    if " cd " in item:
        if name != "":
            directories[name] = buffer
            buffer = []
            print(item)
            name = item.split()[2]
        else:
            print(item)
            name = item.split()[2]
    elif "ls" in item:
        continue
    elif ".." in item:
        continue
    else:
        buffer.append(item.split())
directories[name] = buffer
print(directories['lbz'])
print(recursion('/', directories))
# for key in directories:
#     print(f'Directory: {key}\nFiles: {directories[key]}')
