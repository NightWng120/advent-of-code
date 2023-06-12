data = ""
elves = list()
elf = list()
max = [0, 0]
totals = []
with open('adventofcode.com_2022_day_1_input.txt', 'r') as f:
    data = f.readlines()

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
    if elf > max[1]:
        max[0] = i
        max[1] = elf
print(f'Elf #{max[0] + 1} has the most calories with a total of {max[1]} calories!')
print(f'Elf #{max[0] + 1}\'s bananas are {elves[max[0]]}')
print(totals)
