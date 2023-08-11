with open('sample.txt', 'r') as f:
    data = [list(item.replace('\n', '')) for item in f.readlines()]
def check(tree, data):
    visible = [True, True, True, True]
    for i in range(len(data[0])):
        #          Left   Right  Top    Bottom
        if tree[1] == i:
            continue
        elif data[tree[0]][i] >= data[tree[0]][tree[1]] and i < tree[1]:
            visible[0] = False
        elif data[tree[0]][i] >= data[tree[0]][tree[1]] and i > tree[1]:
            visible[1] = False

    for i in range(len(data)):
        if tree[0] == i:
            continue
        elif data[i][tree[1]] >= data[tree[0]][tree[1]] and i < tree[0]:
            visible[2] = False
        elif data[i][tree[1]] >= data[tree[0]][tree[1]] and i > tree[0]:
            visible[3] = False

    if True in visible:
        print(f'Visible list: {visible}')
        return 1
    else:
        print(f'Visible list: {visible}')
        return 0
# print(data)

# A tree is visible if it is the greatest number in at least one direction
# First, get xy coord of tree
# Then, check against all other trees where their coords, a and b, are as follows
# a > x or a < x and b > y or b < a
# If at least one of the numbers in all dimensions x+, x-, y+, and y- are >= to the current tree, then the tree is not visible
# Else, add 1 to sum

sum = 0
for indexr, row in enumerate(data):
    for indext, tree in enumerate(row):
        sum += check((indexr, indext), data)

print(sum)
print(len(data) * len(data[0]))
