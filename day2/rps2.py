with open('data.txt', 'r') as f:
    data = f.readlines()

'''
if x, get key and use value for score
if y, use key for score
if z, you must loop through keys to find
a value that matches the input and use the key for the score
'''

keys = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
}

score = {
        'A': 1,
        'B': 2,
        'C': 3,
}

Sum = 0
for match in data:
    buffer = match.split(' ')
    meme = match.replace('\n', '')
    buffer[1] = buffer[1].replace('\n', '')
    if buffer[1] == 'X':
        Sum += score[keys[buffer[0]]]
        print(f'{meme}: {score[keys[buffer[0]]]}')

    elif buffer[1] == 'Y':
        Sum += 3 + score[buffer[0]]
        print(f'{meme}: {3 + score[buffer[0]]}')
    else:
        for key in keys:
            if keys[key] == buffer[0]:
                Sum += 6 + score[key]
                print(f'{meme}: {6 + score[key]}')
                break
print(Sum)
