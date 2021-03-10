class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.neighborsList = []
        self.predecessor = None
    
    def __repr__(self):
        return f"{self.data}"

class DepthFirstSearch:
    
    def dfs(self, node):

        print(node)
        node.visited = True

        for neighbor in node.neighborsList:
            if not neighbor.visited:
                self.dfs(neighbor)

if __name__ == "__main__":
    node1 = Node("A");
    node2 = Node("B");
    node3 = Node("C");
    node4 = Node("D");
    node5 = Node("E");
    

    node1.neighborsList.append(node2);
    node1.neighborsList.append(node3);
    node2.neighborsList.append(node4);
    node4.neighborsList.append(node5);

    dfs = DepthFirstSearch();
    dfs.dfs(node1);

    print("###############################################################")
    nodeA = Node("A");
    nodeB = Node("B");
    nodeC = Node("C");
    nodeD = Node("D");
    nodeE = Node("E");
    nodeF = Node("F");
    nodeG = Node("G");
    nodeH = Node("H");
    

    nodeA.neighborsList.append(nodeB);
    nodeA.neighborsList.append(nodeF);
    nodeA.neighborsList.append(nodeG);
    nodeB.neighborsList.append(nodeC);
    nodeB.neighborsList.append(nodeD);
    nodeD.neighborsList.append(nodeE);
    nodeG.neighborsList.append(nodeH);

    dfs2 = DepthFirstSearch();
    dfs2.dfs(nodeA);