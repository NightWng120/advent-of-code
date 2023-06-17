with open('data.txt', 'r') as f:
    data = f.readline()
data = list(data)
buffer = []
processed = []
length = 0
index = 0
for i in range(len(data)):
    if len(buffer) == 14:
        length = i
        processed.extend(buffer)
        break
    elif data[i] not in buffer:
        buffer.append(data[i])
        print(f'Current Buffer: {buffer}')
    elif data[i] in buffer:
        print(f'{data[i]} is in {buffer}')
        processed.extend(buffer)
        buffer = []
        if data[i] != data[i - 1]:
            buffer.append(data[i - 1])
            buffer.append(data[i])
        


# for i in range(len(data)):
#     if i >= 3:
#         buffer = data[i-3:i]
#         print(f'Data: {data[i-3:i]}')
#         if data[i] not in buffer:
#             buffer.extend(data[i])
#             break

# for index, char in enumerate(data):
#     if len(buffer) == 4:
#         length = index
#         processed.extend(buffer)
#         break
#     elif char not in buffer:
#         buffer.append(char)
#         print(f'Current Buffer: {buffer}')
#     elif char in buffer:
#         print(f'{char} is in {buffer}')
#         processed.extend(buffer)
#         buffer = []
#         buffer.append(char)

# print(data)
# print(len(processed))


# print(processed)
print(buffer)
print(length)
