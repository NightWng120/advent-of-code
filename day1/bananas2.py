data = ""
elves = list()
elf = list()
max = [[0, 0], [0, 0], [0, 0]]
totals = []
with open('adventofcode.com_2022_day_1_input.txt', 'r') as f:
    data = f.readlines()
print(len(data))

for item in data:
    if item == '\n':
        elves.append(elf)
        elf = list()
    else:
        elf.append(item)
for i, elf in enumerate(elves):
    elf = list(map(int, elf))
    elf = sum(elf)
    totals.append(elf)
    if elf > max[0][1]:
        max.insert(0, [i, elf])
        max.pop(3)
        #print(f'New Ranking\n#1 {max[0][1]}\n#2 {max[1][1]}\n#3 {max[2][1]}')
    elif elf > max[1][1]:
        max.insert(1, [i, elf])
        max.pop(3)
        #print(f'New Ranking\n#1 {max[0][1]}\n#2 {max[1][1]}\n#3 {max[2][1]}')
    elif elf > max[2][1]:
        max.insert(2, [i, elf])
        max.pop(3)
        #print(f'New Ranking\n#1 Calores: {max[0][1]} Elf: {max[0][0]}\n#2 Calories: {max[1][1]} Elf: {max[1][0]}\n#3 Calories: {max[2][1]} Elf: {max[2][0]}')
print(f'Total = {max[2][1] + max[1][1] + max[0][1]}')
print(totals)
