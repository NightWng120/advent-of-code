with open('data.txt', 'r') as f:
    data = f.readline()

buffer = []
length = 0

for index, char in enumerate(data):

    if len(buffer) == 4:
        length = index + 1
        break
    elif char not in buffer:
        buffer.append(char)
    elif char in buffer:
        # print(f'{char} is in {buffer}')
        buffer = []
        buffer.append(char)

print(buffer)
print(length)
