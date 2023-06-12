with open('data.txt', 'r') as f:
    data = f.readlines()
data = [list(map(int, item.replace('\n', '').replace('move ', '').replace(' from', '').replace(' to', '').split(' '))) for item in data]
temp = []
first = second = third = 0

stacks = [['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
          ['Z', 'S', 'M', 'G', 'V', 'P'],
          ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
          ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
          ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
          ['R', 'G', 'C', 'D'],
          ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
          ['P', 'F', 'V'],
          ['D', 'R', 'S', 'T', 'J']]

for move in data:
    first = move[1] - 1
    if len(stacks[first]) == 0:
        continue

    elif move[0] > len(stacks[first]):
        second = len(stacks[first])
    else:
        second = move[0]

    if move[2]  > len(stacks):
        third = len(stacks) - 1
    else:
        third = move[2] - 1

    # print(f'First: {first}\nSecond: {second}\nThird: {third}')
    length = len(stacks[first][-second:])
    temp = [stacks[first].pop() for i in range(length)]
    temp.reverse()
    print(f'Current stack: #{first + 1}')
    print(stacks[first])
    print(f'Moving {second + 1} item(s) from {first + 1} to {third + 1}')
    print(f'{temp} -> {stacks[third]}')
    stacks[third].extend(temp)
    # print(f'New stack arrangement:\n{stacks}')
    # print(f'Current move: {temp}')

print(stacks)
items = [item[len(item) - 1] for item in stacks if len(item) > 0]
print(stacks)
print(len(stacks))
for item in items:
 print(f'{item}', end='')
print()
