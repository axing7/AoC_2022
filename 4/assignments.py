with open('input.txt') as f:
	lines = f.readlines()

count = 0
count2 = 0

for line in lines:
	[first, second] = line.split(',')
	[range11, range12] = first.split('-')
	[range21, range22] = second.split('-')
	if (int(range11) <= int(range21)) & (int(range12) >= int(range22)):
		count += 1
	elif (int(range21) <= int(range11)) & (int(range22) >= int(range12)):
		count += 1

	if (int(range11) <= int(range21)) & (int(range12) >= int(range21)):
		count2 += 1
	elif (int(range21) <= int(range11)) & (int(range22) >= int(range11)):
		count2 += 1


print(count)
print(count2)