with open('data.txt', 'r') as f:
    data = [list(item.replace('\n', '')) for item in f.readlines()]

def check(tree, data):
    scenic = [0,0,0,0]
    loop = True
    edge = 0
    i = 0
    while loop:
        i += 1
        if edge == 0:
            if (tree[1] - i) > 0 and data[tree[0]][tree[1]] > data[tree[0]][tree[1] - i]:
                print(f'Tree {data[tree[0]][tree[1]]}, at postion {tree} > tree {data[tree[0]][tree[1] - i]}, at position {[tree[0], tree[1] - i]}')
                scenic[0] += 1
            else:
                scenic[0] += 1
                edge += 1

        elif edge == 1:
            if (tree[1] + i) < 98 and data[tree[0]][tree[1]] > data[tree[0]][tree[1] + i]:
                print(f'Tree {data[tree[0]][tree[1]]}, at postion {tree} > tree {data[tree[0]][tree[1] + i]}, at position {data[tree[0]][tree[1] + i]}')
                scenic[1] += 1
            else:
                scenic[1] += 1
                edge += 1

        elif edge == 2:
            if (tree[0] - i) > 0 and data[tree[0]][tree[1]] > data[tree[0] - i][tree[1]]:
                print(f'Tree {data[tree[0]][tree[1]]}, at postion {tree} > tree {data[tree[0] - i][tree[1]]}, at position {[tree[0] - i, tree[1]]}')
                scenic[2] += 1
            else:
                scenic[2] += 1
                edge += 1
        elif edge == 3:
            if (tree[0] + i) < 98 and data[tree[0]][tree[1]] > data[tree[0] + i][tree[1]]:
                print(f'Tree {data[tree[0]][tree[1]]}, at postion {tree} > tree {data[tree[0] + i][tree[1]]}, at position {[tree[0] + i, tree[1]]}')
                scenic[3] += 1
            else:
                scenic[3] += 1
                edge += 1
                loop = False
    return scenic


max = 0
scenic = []
scenicMax = []
current = 0
treeMax = []
wasMax = False
for indexr, row in enumerate(data):
    for indext, tree in enumerate(row):
        scenic = check([indexr, indext], data)
        current = scenic[0] * scenic[1] * scenic[2] * scenic[3]
        if current > max:
            treeMax = [indexr, indext]
            scenicMax = scenic
            # print(f"Position {indexr},{indext} has scenic numbers {scenic}\nIt's number is {data[indexr][indext]}")
            max = current

for indexr, row in enumerate(data):
    for indext, tree in enumerate(row):
        if [indexr, indext] == treeMax:
            print(f'[{data[indexr][indext]}]',end='')
            wasMax = True
        else:
            if wasMax:
                print(f'{data[indexr][indext]}',end='')
                wasMax = False
            else:
                print(' ',end='')
                print(f'{data[indexr][indext]}',end='')
    print()


print(max)
print(scenicMax)
print(treeMax)
