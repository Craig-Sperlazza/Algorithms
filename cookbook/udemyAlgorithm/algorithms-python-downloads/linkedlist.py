class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None


class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0

	def __str__(self):
		result = "["
		node = self.head
		if node != None:
			result += str(node.data)
			node = node.nextNode
			while node:
				result += " -> " + str(node.data)
				node = node.nextNode
		result += "]"
		return result


	def insertStart(self, data):

		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			#first link the new node to the previous first node
			newNode.nextNode = self.head
			self.head = newNode

	def remove(self, data):

		if self.head is None:
			return

		self.size = self.size - 1

		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode

	# O(1)
	def size1(self):
		return self.size

	# O(N) not good !!!
	def size2(self):

		actualNode = self.head
		size = 0

		while actualNode is not None:
			size += 1
			actualNode = actualNode.nextNode

		return size

	# O(N)
	def insertEnd(self, data):

		self.size = self.size + 1
		newNode = Node(data)
		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode

	def traverseList(self):

		actualNode = self.head

		while actualNode is not None:
			print("%d " % actualNode.data)
			actualNode = actualNode.nextNode


linkedlist = LinkedList()

linkedlist.insertStart(12);
linkedlist.insertStart(122);
linkedlist.insertStart(3);
linkedlist.insertEnd(31);
print(linkedlist)

linkedlist.traverseList();

linkedlist.remove(3);
linkedlist.remove(12);
linkedlist.remove(122);
linkedlist.remove(31);

print(linkedlist.size1());
