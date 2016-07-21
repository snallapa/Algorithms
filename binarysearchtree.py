import random

class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def addNode(node, value):
	if node.value > value:
		if node.left == None:
			node.left = Node(value, None, None)
		else:
			addNode(node.left, value)
	else:
		if node.right == None:
			node.right = Node(value, None, None)
		else:
			addNode(node.right,value)
def buildTree(data):
	rootNode = Node(data[0], None, None)
	for i in data[1:]:
		addNode(rootNode, i)
	return rootNode

def findInTree(node, value):
	if node == None:
		return False
	if node.value == value:
		return True
	if value < node.value:
		return findInTree(node.left, value)
	else:
		return findInTree(node.right, value)

def printTree(tree):
	if tree != None:
		print tree.value
		printTree(tree.left)
		printTree(tree.right)
		
		

data = list(set([int(10000*random.random()) for _ in xrange(1000)]))
random.shuffle(data)
print data
tree = buildTree(data)
print findInTree(tree, data[50])