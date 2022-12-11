import numpy as np

class Monkey:
	def __init__(self, operation, divisor, if_true, if_false, items=[], interactions=0):
		self.operation = operation
		self.divisor = divisor
		self.if_true = if_true
		self.if_false = if_false
		self.items = items
		self.interactions = interactions

if __name__ == "__main__":

	with open('input.txt') as f:
		
		monkey_blocks = f.read().split("\n\n")
		monkeys = []

		# populate monkey objects
		for i in range(0, len(monkey_blocks)):
			monkey = monkey_blocks[i]
			lines = monkey.split("\n")
			items = lines[1].split(": ")[-1].split(", ")
			items = list(map(int, items))

			operation = lines[2].split("= old ")[-1].strip()
			divisor = int(lines[3].split("by ")[-1])
			if_true = int(lines[4].split("monkey ")[-1])
			if_false = int(lines[5].split("monkey ")[-1])

			monkeys.append(Monkey(operation, divisor, if_true, if_false, items))

		# do the rounds
		part = 2
		lcm = np.prod([x.divisor for x in monkeys])

		for i in range(0, (20 if part == 1 else 10000)):
			print("round: %d" % (i))
			for j in range(0, len(monkeys)):
				this_monkey = monkeys[j]
				for k in range(0, len(this_monkey.items)):
					item = this_monkey.items[0]
					this_monkey.items.remove(item)
					operation = this_monkey.operation
					if (operation == "* old"):
						item *= item
					elif (operation[0] == "*"):
						item *= int(operation.split("* ")[-1])
					else:
						item += int(operation.split("+ ")[-1])

					if part == 1:
						item //= 3
					
					divisor = this_monkey.divisor
					if (item % divisor) == 0:
						item = item % lcm
						monkeys[this_monkey.if_true].items.append(item)
					else:
						item = item % lcm
						monkeys[this_monkey.if_false].items.append(item)

					this_monkey.interactions += 1

		interactions_list = [x.interactions for x in monkeys]
		interactions_list.sort()
		print(interactions_list[-1] * interactions_list[-2])











