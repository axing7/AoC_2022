with open('input.txt') as f:
	lines = f.readlines()

calories_arr = []
curr_cals = 0

for line in lines:
	if line == '\n':
		calories_arr.append(curr_cals)
		curr_cals = 0
	else:
		curr_cals += int(line)

print(max(calories_arr))

calories_arr.sort()
print(sum(calories_arr[-3:]))