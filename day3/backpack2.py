with open('data.txt', 'r') as f:
    data = f.readlines()
data = [string.replace('\n', '') for string in data]
buffer = []
j = 0
sum = 0
for i in range(100):
    temp = data[j:j + 3]
    buffer.append(temp)
    for item in temp[0]:
        if item in temp[1] and item in temp[2]:
            if item.islower():
                sum += ord(item) - 96
                break
            elif item.isupper():
                sum += ord(item) - 38
                break
    j += 3

length = 0
for i in buffer:
    for k in i:
        print(k)
print(length)
print(sum)
# sum = 0
# for ruck in data:
#     for item in ruck[0]:
#         if item in ruck[1]:
#             if item.islower():
#                 sum += ord(item) - 96
#                 print(f'String: {ruck}\nItem: {item}\nPriority: {ord(item) - 96}')
#                 break
#             elif item.isupper():
#                 sum += ord(item) - 38
#                 print(f'String: {ruck}\nItem: {item}\nPriority: {ord(item) - 38}')
#                 break
# print(sum)
