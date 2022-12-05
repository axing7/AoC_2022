import copy

with open('input.txt') as f:
	lines = f.readlines()

stack_lines = lines[:8]
stack_lines.reverse()

stacks = [[] for i in range(9)]

for line in stack_lines:
	idx = 1
	for i in range(9):
		if line[idx] != ' ':
			stacks[i].append(line[idx])
		idx += 4

stacks2 = copy.deepcopy(stacks)

proc_lines = lines[10:]

for line in proc_lines:
	nums = [int(s) for s in line.split() if s.isdigit()]
	nums[1] -= 1
	nums[2] -= 1

	for i in range(nums[0]):
		crate = stacks[nums[1]].pop()
		stacks[nums[2]].append(crate)

	crates = stacks2[nums[1]][-nums[0]:]
	for i in range(len(crates)):
		stacks2[nums[2]].append(crates[i])
		stacks2[nums[1]].pop()

string = ''
string2 = ''
for i in range(9):
	if stacks[i]:
		string += stacks[i][-1]
	if stacks2[i]:
		string2 += stacks2[i][-1]
print(string)
print(string2)
