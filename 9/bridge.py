import copy
import math

def update_knots(knot1, knot2):
	# find the direction vector from knot2 to knot1
	diff = []
	for item1, item2 in zip(knot1, knot2):
		item = item1 - item2
		diff.append(item)

	# move knot2 towards knot1 based on the direction vector
	if diff[0] > 0:
		knot2[0] += 1
	elif diff[0] < 0:
		knot2[0] -= 1

	if diff[1] > 0:
		knot2[1] += 1
	elif diff[1] < 0:
		knot2[1] -= 1

	return knot2

if __name__ == "__main__":

	with open('input.txt') as f:
		lines = f.readlines()

	# ropelen = 2 		# part 1
	ropelen = 10 		# part 2
	rope = []

	# create a rope of desired length
	for i in range(0, ropelen):
		rope.append([0,0])

	# create a list to track visited locations by the tail, append it's starting position (0,0)
	visited = []
	visited.append(copy.deepcopy(rope[-1]))

	for line in lines:

		line.replace("\n", "")
		direc, num = line.split(" ")
		num = int(num)

		for i in range(0, num):
			# move the head of the rope
			if direc == "R":
				rope[0][0] += 1
			elif direc == "L":
				rope[0][0] -= 1
			elif direc == "U":
				rope[0][1] += 1
			elif direc == "D":
				rope[0][1] -= 1

			# iterate through the rest of the rope and update the other knot(s)
			# if the tail is in a new spot, add it to the visited list
			for j in range(0, ropelen):
				if j == (ropelen - 1):
					if rope[-1] not in visited:
						visited.append(copy.deepcopy(rope[-1]))
				elif math.dist(rope[j], rope[j+1]) >= 2:
					knot1 = rope[j]
					knot2 = rope[j+1]
					rope[j+1] = copy.deepcopy(update_knots(knot1,knot2))

			# print(rope[0])
			# print(rope[-1])
			# print("rope"), print(rope)
			# print("visited"), print(visited)

	print(len(visited))
