with open('input.txt') as f:
	lines = f.readlines()

prio_sum = 0
prio_sum2 = 0

for idx, line in enumerate(lines):
	# split in 2
	first, second = line[:len(line)//2], line[len(line)//2:]

	# find common item
	common = set(first).intersection(set(second))
	# add to sum
	prio = ord(common.pop()) - ord('`')
	if prio < 0:
		# capital letter
		prio_sum += (prio + 58)
	else:
		prio_sum += prio

	if (idx % 3) == 0:
		common2 = set(lines[idx].strip()).intersection(set(lines[idx+1].strip()).intersection(set(lines[idx+2])))
		prio2 = ord(common2.pop()) - ord('`')
		if prio2 < 0:
			prio_sum2 += (prio2 + 58)
		else:
			prio_sum2 += prio2

print(prio_sum)
print(prio_sum2)
