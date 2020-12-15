
class Node(object):

	def __init__(self, name):
		self.name = name;
		self.adjacencyList = [];
		self.visited = False;
		#previous vertext in the breadth first order ---useful when we use shortest path, not used here
		self.predecessor = None;
		
class BreadthFirstSearch(object):

	def bfs(self, startNode):
		
		# queue must be underlying ADT
		queue = [];
		queue.append(startNode);
		startNode.visited = True;
		
		######################    BFS -> queue  ########################    DFS --> stack BUT usually we implement it with recursion !!!
		#queue must be FIFO (append at end, pop(0) at the beginning)
		#while loop will iterate until the queue is empty
		while queue:
			
			#pop the first index since the queue has a FIFO structure
			actualNode = queue.pop(0);
			# print("%s " % actualNode.name);
			print(f"{actualNode.name}")
			
			for n in actualNode.adjacencyList:
				if not n.visited:
					n.visited = True;
					queue.append(n);
					
node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");

node1.adjacencyList.append(node2);
node1.adjacencyList.append(node3);
node2.adjacencyList.append(node4);
node4.adjacencyList.append(node5);

bfs = BreadthFirstSearch();
bfs.bfs(node1);