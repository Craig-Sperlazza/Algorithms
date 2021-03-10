#taken from udemy algorithms, bfs----I am going to retireve specific data

class Node:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.visited = False
        #note you could set the neighbors in here as well, but we do it manually below
        self.adjacencyList = []
        #previous vertext in the breadth first order 
        #useful when we use shortest path, not used here
        self.predecessor = None
    
    def __repr__(self):
        return f"{self.name}: {self.data}"
    
class BreadthFirstSearch:
    def bfs(self, startNode):
        #queue is FIFO
        queue = []
        queue.append(startNode)
        startNode.visited = True

        #keep iterating (considering neighbors)until queue becomes empty
        while queue:
            #remove and return first item we inserted (FIFO)
            currentNode = queue.pop(0)
            print(f"{currentNode.name}:{currentNode.data}")

            #need to deal with all neighbors
            for element in currentNode.adjacencyList:
                if not element.visited:
                    queue.append(element)
                    element.visited = True


if __name__ == "__main__":
					
    node1 = Node("A", 33);
    node2 = Node("B", 44);
    node3 = Node("C", 22);
    node4 = Node("D", 11);
    node5 = Node("E", 55);

    node1.adjacencyList.append(node2);
    node1.adjacencyList.append(node3);
    node2.adjacencyList.append(node4);
    node4.adjacencyList.append(node5);

    bfs = BreadthFirstSearch();
    bfs.bfs(node1);
    
    #from book page 211

    nodeA = Node("A");
    nodeB = Node("B");
    nodeC = Node("C");
    nodeD = Node("D");
    nodeE = Node("E");
    nodeF = Node("F");
    nodeG = Node("G");
    nodeH = Node("H");

    nodeA.adjacencyList.append(nodeG);
    nodeA.adjacencyList.append(nodeB);
    nodeA.adjacencyList.append(nodeD);
    nodeB.adjacencyList.append(nodeE);
    nodeB.adjacencyList.append(nodeA);
    nodeB.adjacencyList.append(nodeF);
    nodeC.adjacencyList.append(nodeF);
    nodeC.adjacencyList.append(nodeH);
    nodeD.adjacencyList.append(nodeA);
    nodeD.adjacencyList.append(nodeF);
    nodeE.adjacencyList.append(nodeB);
    nodeE.adjacencyList.append(nodeG);
    nodeF.adjacencyList.append(nodeC);
    nodeF.adjacencyList.append(nodeB);
    nodeF.adjacencyList.append(nodeD);
    nodeG.adjacencyList.append(nodeA);
    nodeG.adjacencyList.append(nodeE);
    nodeH.adjacencyList.append(nodeC);

    bfs2 = BreadthFirstSearch()
    bfs2.bfs(nodeA)