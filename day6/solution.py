with open('data.txt', 'r') as f:
    line = f.readline().strip()

for i in range(len(line)):
    print(line[i],end='')
    if len(set(line[i:i+4]))==4:
        print()
        print(line[i:i+4])
        print(i+4)
        break
