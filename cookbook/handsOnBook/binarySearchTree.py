class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
    
    def __str__(self):
        return f"{self.data}"

class BinarySearchTree:
    def __init__(self):
        self.root_node = None
    
    def find_min(self):
        """The minimum node is the furthest to the left
        """
        current = self.root_node

        while current.left_child:
            current = current.left_child

        # return current.data
        return current
        
    def find_max(self):
        """max node is furthest down to the right
        """
        current = self.root_node

        while current.right_child:
            current = current.right_child
        
        # return current.data
        return current

    def insert (self, data):
        node = Node(data)
        #first node entered into tree
        if self.root_node is None:
            self.root_node = node
            return
        else:
            current = self.root_node
            parent = None

            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
        
    
    def insertRecursive(self, val):
        node = Node(val)
        if self.root_node is None:
            self.root_node = node
        else:
            self.insertNodeRecursive(self.root_node, val)

    def insertNodeRecursive(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNodeRecursive(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNodeRecursive(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def in_order_traverse(self, current=None, visited=None):
        """[summary]

        Args:
            current This is the current node. Defaults to None, and then after the first call---it will be set to the root and then each child.
            visited ([type], optional): A list that collects the data. Defaults to None. 
        """
        # This is the first time the function is called---initializes the list, sets current node to root
        if visited is None:
            visited = []
            self.in_order_traverse(self.root_node, visited)
        
        #base case
        if current is None:
            return visited
        
        self.in_order_traverse(current.left_child, visited)
        # print(current.data)
        visited.append(current.data)
        self.in_order_traverse(current.right_child, visited)
        return visited

    def sorted_array_to_bst(self, arr):
        """This function takes a sorted array and turns it into a bst recursively finding the root (i.e. the mid)

        Args:
            arr ([type]): sorted array
        """

        #find the middle of the array and then make it the root
        mid = len(arr) // 2

        node = Node(arr[mid])

        #the left subtree is all the values to the left (i.e. smaller) of root
        node.left = self.sorted_array_to_bst(arr[:mid])

        #the right subtree is all the values to the right (i.e. larger) of root
        node.right = self.sorted_array_to_bst(arr[mid+1:])

        return node
        

if __name__ == "__main__":
    
    print("TESTING THE ITERATIVE INSERTION VERSION")
    my_bst = BinarySearchTree()
    my_bst.insert(5)
    my_bst.insert(3)
    my_bst.insert(7)
    my_bst.insert(1)

    max_node = my_bst.find_max()
    print("max:", max_node)

    min_node = my_bst.find_min()
    print("min:", min_node)

    my_bst.in_order_traverse()

    bst_list = my_bst.in_order_traverse()
    print(f"In Order:{bst_list}")

    print("TESTING THE RECURSIVE INSERTION VERSION")
    my_rec_bst = BinarySearchTree()
    my_rec_bst.insert(15)
    my_rec_bst.insert(13)
    my_rec_bst.insert(17)
    my_rec_bst.insert(11)

    max_node = my_rec_bst.find_max()
    print("max:", max_node)

    min_node = my_rec_bst.find_min()
    print("min:", min_node)

    recur_bst_list = my_rec_bst.in_order_traverse()
    print(f"In Order:{recur_bst_list}")
    
    print("TESTING THE SORTED ARRAY TO BST")
    arr1 = [1,2,3,4,5,6,7,8,9]

    sorted_bst = BinarySearchTree()
    root = sorted_bst.sorted_array_to_bst(arr1)
    print(root)