import numpy as np

with open('input.txt') as f:
	lines = f.readlines()

dim = len(lines[0].strip())
trees = np.zeros((dim,dim), dtype=int)
visible = np.zeros((dim,dim), dtype=int)
scenic = np.ones((dim,dim), dtype=int)

for i in range(0, dim):
	trees[i] = np.fromiter(lines[i].strip(), dtype=int)

for i in range(0, dim):
	for j in range(0, dim):
		curr_tree = trees[i,j]
		if i == 0 or i == (dim - 1):
			visible[i,j] = 1
			scenic[i,j] = 0
		elif j == 0 or j == (dim - 1):
			visible[i,j] = 1
			scenic[i,j] = 0
		elif curr_tree > max(trees[i,:j]):
			visible[i,j] = 1
		elif curr_tree > max(trees[i,j+1:]):
			visible[i,j] = 1
		elif curr_tree > max(trees[:i,j]):
			visible[i,j] = 1
		elif curr_tree > max(trees[i+1:,j]):
			visible[i,j] = 1

		up = down = left = right = 0

		if scenic[i,j] != 0:
			#up
			i2 = i-1
			curr_tree = trees[i,j]
			while (i2 >= 0):
				next_tree = trees[i2, j]
				if (curr_tree > next_tree):
					up += 1
					i2 -= 1
				else:
					up += 1
					break
			scenic[i,j] *= up

			#down
			i2 = i+1
			curr_tree = trees[i,j]
			while (i2 < dim):
				next_tree = trees[i2, j]
				if (curr_tree > next_tree):
					down += 1
					i2 += 1
				else:
					down += 1
					break
			scenic[i,j] *= down

			#left
			j2 = j-1
			curr_tree = trees[i,j]
			while (j2 >= 0):
				next_tree = trees[i, j2]
				if (curr_tree > next_tree):
					left += 1
					j2 -= 1
				else:
					left += 1
					break
			scenic[i,j] *= left

			#right
			j2 = j+1
			while (j2 < dim):
				next_tree = trees[i, j2]
				if (curr_tree > next_tree):
					right += 1
					j2 += 1
				else:
					right += 1
					break
			scenic[i,j] *= right

			# print("i,j,scenic: %d,%d,%d" % (i,j,scenic[i,j]))
			# print("up,down,left,right: %d,%d,%d,%d" % (up,down,left,right))


# print(visible)
# print(trees)
# print(scenic)
print(sum(sum(visible)))
print(np.amax(scenic))
