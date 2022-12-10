from collections import defaultdict


def update_cycle(cycle, x, signal_strength, pixels):
	cycle += 1
	if ((cycle - 20) % 40) == 0:
		signal_strength.append(cycle*x)

	if abs(x - ((cycle-1) % 40)) <= 1:
		pixels.append("#")
	else:
		pixels.append(".")

	return cycle, signal_strength, pixels

if __name__ == "__main__":

	with open('input.txt') as f:
		lines = f.readlines()

	x = 1
	cycle = 0
	signal_strength = []
	pixels = []

	for line in lines:
		line = line.replace("\n", "")

		if line == "noop":
			cycle, signal_strength, pixels = update_cycle(cycle, x, signal_strength, pixels)

		else:
			val = int(line.split()[1])
			cycle, signal_strength, pixels = update_cycle(cycle, x, signal_strength, pixels)
			cycle, signal_strength, pixels = update_cycle(cycle, x, signal_strength, pixels)
			x += val

print(sum(signal_strength[:6]))

for i in range(0, (len(pixels)//40)):
	print(" ".join(pixels[(40 * i):(40 * (1 + i))]))
