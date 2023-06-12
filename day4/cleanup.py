with open('data.txt', 'r') as f:
    data = f.readline()
data = data.replace("\n", "")
data = data.split(',')
buffer = []
contained = 0
pairs = 0
j = 0
for i in range(int(len(data)/2)):
    buffer.append(data[j:j+2])
    buffer[len(buffer) - 1][0] = buffer[len(buffer) - 1][0].split('-')
    buffer[len(buffer) - 1][1] = buffer[len(buffer) - 1][1].split('-')
    pairs += 1
    if (int(buffer[len(buffer) - 1][0][0]) >= int(buffer[len(buffer) - 1][1][0])) and (int(buffer[len(buffer) - 1][0][1]) <= int(buffer[len(buffer) - 1][1][1])) or (int(buffer[len(buffer) - 1][0][0]) == int(buffer[len(buffer) - 1][1][0])) or (int(buffer[len(buffer) - 1][0][1]) == int(buffer[len(buffer) - 1][1][1])) or (int(buffer[len(buffer) - 1][0][1]) == int(buffer[len(buffer) - 1][1][0])) or (int(buffer[len(buffer) - 1][0][0]) == int(buffer[len(buffer) - 1][1][1])):

        contained += 1
        print(f'#{0} {buffer[len(buffer) - 1][0]} is contained in #{1} {buffer[len(buffer) - 1][1]}')
    elif (int(buffer[len(buffer) - 1][1][0]) >= int(buffer[len(buffer) - 1][0][0])) and (int(buffer[len(buffer) - 1][1][1]) <= int(buffer[len(buffer) - 1][0][1])) or (int(buffer[len(buffer) - 1][0][0]) == int(buffer[len(buffer) - 1][1][0])) or (int(buffer[len(buffer) - 1][0][1]) == int(buffer[len(buffer) - 1][1][1])) or (int(buffer[len(buffer) - 1][0][1]) == int(buffer[len(buffer) - 1][1][0])) or (int(buffer[len(buffer) - 1][0][0]) == int(buffer[len(buffer) - 1][1][1])):
        contained += 1
        print(f'#{1} {buffer[len(buffer) - 1][1]} is contained in #{0} {buffer[len(buffer) - 1][0]}')
    j += 2
# for i, item in enumerate(buffer):
#     print(f'#{i + 1}: {item}')
print(contained)
# print(buffer)
