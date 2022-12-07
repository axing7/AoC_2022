with open('input.txt') as f:
	lines = f.readlines()

class TreeNode:
	def __init__(self, parent=None, name=None, size=0, filetype=None):
		self.parent = parent
		self.children = []
		self.name = name
		self.size = size
		self.filetype = filetype

	def get_children_names(self):
		return [child.name for child in self.children]

	def add_child(self, TreeNode):
		# print("Adding node named: " + TreeNode.name)
		self.children.append(TreeNode)
		# print(self.children[0].name)
		# print(TreeNode.size)

	def find_child(self, name):
		# print("Finding child named: " + name)
		return self.get_children_names().index(next_dir)

	def add_size(self, size):
		# print("Adding size %d" % (size))
		curr = self
		while(curr):
			curr.size += size
			curr = curr.parent

	def get_sizes(self):
		# returns a list of sizes for directories only
		sizes = []
		# print(self.get_children_names())
		for child in self.children:
			# print(child.size)
			# print(child.filetype)
			# print(child.name)
			if child.filetype == "dir":
				sizes.append(child.size)
				# print(sizes)
				sizes.extend(child.get_sizes())
		return sizes

root = TreeNode(name="/")
current_node = root

for line in lines:
	line = line.strip() #remove \n from end

	# print("Current node: " + current_node.name)
	# print(current_node.get_children_names())

	if line[0:5] == "$ cd ":
		# print("cd line")
		next_dir = line.split(" ")[2]
		if next_dir == "..": 
			#traverse back up one
			current_node = current_node.parent 
		else: 
			#else, move down to the specified child'
			# creates the node if it doesn't exist, though this doesn't get used
			# because of how the input is formatted

			# print("Next_dir to cd to: " + next_dir)

			if next_dir not in current_node.get_children_names():
				next_node = TreeNode(name=next_dir, parent=current_node, filetype="dir")
				current_node.add_child(next_node)
				current_node = next_node
			else: 
				# this node has already been created, so just change to it
				next_node_idx = current_node.find_child(next_dir)
				current_node = current_node.children[next_node_idx]
	elif line == "$ ls": 
		#don't need to do anything
		# print("ls line")
		pass
	elif line.split(" ")[0] == "dir": 
		#this is a directory, add to tree if not already existing
		next_dir = line.split(" ")[1]
		if next_dir not in current_node.get_children_names():
			next_node = TreeNode(name=next_dir, parent=current_node, filetype="dir")
			current_node.add_child(next_node)
	else:
		# this is a file, add to tree and update the sizes all the way to the top
		size = int(line.split(" ")[0])
		name = line.split(" ")[1]
		new_file_node = TreeNode(parent=current_node, name=name, size=size, filetype="file")
		current_node.add_child(new_file_node)
		current_node.add_size(size)


sizes = root.get_sizes()
print(sum([x for x in sizes if x < 100000])) #part 1 answer

space_to_free = 30000000 - (70000000 - root.size)
print(min([x for x in sizes if x >= space_to_free])) #part 2 answer
