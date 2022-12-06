from collections import deque

with open('input.txt') as f:
	lines = f.readlines()

last_n = deque([])
charnum = 1
# sync_len = 4
sync_len = 14

for char in lines[0]:
	if char not in last_n:
		last_n.append(char)
		if len(last_n) == sync_len:
			break
	else:
		while len(last_n) != 0:
			deque.popleft(last_n)
			if char not in last_n:
				last_n.append(char)
				break
		if len(last_n) == 0:
			last_n.append(char)

	charnum += 1

print(last_n)
print(charnum)