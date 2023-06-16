with open('data.txt', 'r') as f:
    data = f.readline()
buffer = []
processed = []
length = 0

for index, char in enumerate(data):
    if len(buffer) == 4:
        length = index
        processed.extend(buffer)
        break
    elif char not in buffer:
        buffer.append(char)
    elif char in buffer:
        # print(f'{char} is in {buffer}')
        processed.extend(buffer)
        buffer = []
        buffer.append(char)

# print(data)
print(len(processed))
print(processed)
print(buffer)
print(length)
