with open('input.txt') as f:
	lines = f.readlines()

score = 0
score2 = 0

for line in lines:
	them = line[0]
	mine = line[2]

	if mine == 'X':
		if them == 'A':
			score += (3 + 1)
			score2 += 3
		elif them == 'B':
			score += 1
			score2 += 1
		elif them == 'C':
			score += (6 + 1)
			score2 += 2
	elif mine == 'Y':
		if them == 'A':
			score += (6 + 2)
			score2 += (1 + 3)
		elif them == 'B':
			score += (3 + 2)
			score2 += (2 + 3)
		elif them == 'C':
			score += 2
			score2 += (3 + 3)

	elif mine == 'Z':
		if them == 'A':
			score += 3
			score2 += (2 + 6)
		elif them == 'B':
			score += (6 + 3)
			score2 += (3 + 6)
		elif them == 'C':
			score += (3 + 3)
			score2 += (1 + 6)

print(score)
print(score2)
