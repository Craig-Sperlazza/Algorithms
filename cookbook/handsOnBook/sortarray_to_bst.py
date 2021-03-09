class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return f"{self.data}"


def sorted_array_to_bst(arr):
        """This function takes a sorted array and turns it into a bst recursively finding the root (i.e. the mid)

        Args:
            arr ([type]): sorted array
        """
        
        #base case
        if not arr:
            return None

        #find the middle of the array and then make it the root
        mid = len(arr) // 2

        node = Node(arr[mid])

        #the left subtree is all the values to the left (i.e. smaller) of root
        node.left = sorted_array_to_bst(arr[:mid])

        #the right subtree is all the values to the right (i.e. larger) of root
        node.right = sorted_array_to_bst(arr[mid+1:])

        return node

def in_order_traverse(node):
    if not node:
        return
    in_order_traverse(node.left)
    print(node.data)
    in_order_traverse(node.right)

def preOrder(node): 
    if not node: 
        return      
    print(node.data)
    preOrder(node.left) 
    preOrder(node.right)  

if __name__ == "__main__":

    print("TESTING THE SORTED ARRAY TO BST")
    arr1 = [1,2,3,4,5,6,7,8,9]

    sortBST = sorted_array_to_bst(arr1)
    preOrder(sortBST)
    in_order_traverse(sortBST)