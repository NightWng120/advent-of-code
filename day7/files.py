memo = {}
def recursion(dir, directs):
    if dir in memo:
        return 0
    sum = 0
    for item in directs[dir]:
        if 'dir' in item:
            sum += recursion(item[1], directs)
        else:
            sum += int(item[0])
    print(f'Sum of {dir}: {sum}')
    memo[dir] = sum
    return sum





with open('data.txt', 'r') as f:
    data = [item.replace('\n', '') for item in f.readlines()]
# Find cd and put directory name in a buffer list
# Put all directories and files after ls in a list(splitting size/dir with name of item) in a dictionary with the last element in the buffer being the key
# if directory is .. or ls, continue

directories = {}
buffer = []
path = ""
first = True
# print(data)
for index, item in enumerate(data):
    if " cd " in item and ".." not in item:
        if path != "":
            directories[path] = buffer
            buffer = []
            path += item.split()[2] + "/"
            first = False
        else:
            # print(item)
            path += item.split()[2]
            # print(f'Parent Directory: {path}')
    elif "$ ls" in item:
        # print(f'ls is in {item}')
        continue
    elif ".." in item:
        # print(f'Old Path: {path}')
        path = path[1:-1]
        path = path.split('/')
        # print(path)
        path = path[:-1]

        path = '/' + '/'.join(path) + '/'
        if path == "//":
            path = '/'
        # print(f'New Path: {path}')
        # print(f'.. is in {item}')
        continue
    else:
        if item.split()[0] == 'dir':
            buffer.append([item.split()[0], path + item.split()[1] + '/'])
        else:
            buffer.append([item.split()[0], path + item.split()[1]])
directories[path] = buffer
for key in directories:
    print(f'Directory: {key}\nFiles: {directories[key]}')
# print(recursion('/', directories))
