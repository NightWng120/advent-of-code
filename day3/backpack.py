with open('data.txt', 'r') as f:
    data = f.readlines()
data = [string.replace('\n', '') for string in data]
data = [[string[:int(len(string)/2)],
         string[int(len(string)/2):]] for string in data]
sum = 0
for ruck in data:
    for item in ruck[0]:
        if item in ruck[1]:
            if item.islower():
                sum += ord(item) - 96
                print(f'String: {ruck}\nItem: {item}\nPriority: {ord(item) - 96}')
                break
            elif item.isupper():
                sum += ord(item) - 38
                print(f'String: {ruck}\nItem: {item}\nPriority: {ord(item) - 38}')
                break
print(sum)
