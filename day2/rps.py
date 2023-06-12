with open('data.txt', 'r') as f:
    data = f.readlines()
key = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
}

score = {
        'X': 1,
        'Y': 2,
        'Z': 3
}

Sum = 0
for match in data:
    buffer = match.split(' ')
    buffer[1] = buffer[1].replace('\n', '')
    if key[buffer[0]] == buffer[1]:
        Sum += score[buffer[1]]
    elif key[buffer[1]] == buffer[0]:
        Sum += 6 + score[buffer[1]]
    else:
        Sum += 3 + score[buffer[1]]
print(Sum)
