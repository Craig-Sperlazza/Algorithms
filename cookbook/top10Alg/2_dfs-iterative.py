class Node:
    def __init__(self, data):
        self.data = data
        self.neighborsList = []
        self.visited = False
        self.predecessor = None
    
    def __repr__(self):
        return f"{self.data}"
    
class DepthFirstSearch:

    def dfs(self, node):

        #stack is LIFO
        stack = []
        stack.append(node)

        while stack:
            actualNode = stack.pop()
            actualNode.visited = True
            print(actualNode)

            for neighbor in actualNode.neighborsList:
                if not neighbor.visited:
                    stack.append(neighbor)
                    neighbor.visited = True
            




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