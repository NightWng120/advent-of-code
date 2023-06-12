with open('adventofcode.com_2022_day_1_input.txt','r') as my_file:
    my_file = my_file.readlines()
calories = []
sum_ = 0
for i in my_file:
    if i != '\n':
        sum_ += int(i)
    else:
        calories.append(sum_)
        sum_ = 0
calories.sort(reverse=True)
print(calories[0])
print(calories[:3])
print(sum(calories[:3]))
