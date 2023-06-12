with open('data.txt', 'r') as f:
    data = f.readline()
data = data.replace("\n", "")
data = data.split(',')
j = 0
overlaps = 0
filtered = [data[i:i+2] for i in range(0, int(len(data)), 2)]
filtered = [[list(map(int, filtered[int(i/2)][0].split('-'))), list(map(int, filtered[int(i/2)][1].split('-')))] for i in range(0, int(len(data)), 2)]

for i, pair in enumerate(filtered):
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1] or pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
        overlaps += 1
    elif pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1] or pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1] or pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1] or pair[1][1] >= pair[0][0] and pair[1][1] <= pair[0][1]:
        overlaps += 1
print(filtered)
print(overlaps)
