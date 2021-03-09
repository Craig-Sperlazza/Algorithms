class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def __str__(self):
        if not self.head:
            return "Empty"
        else:
            current = self.head
            last = self.tail
            out = "["
            while current.next is not None:
                out = out + str(current.data) + " <-> "
                current = current.next
            out = out + str(current.data) + "]"
            return out
    
    def get_count(self):
        return self.count
    
    def get_head(self):
        return self.head.data
    
    def get_tail(self):
        return self.tail.data
    
    def insert(self, data):
        node = Node(data)
        self.count += 1
        if not self.head:
            self.head = node
            self.tail = node
            return
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
    
    def traverse(self):
        if not self.head:
            return
        else:
            current = self.head
            while current.next is not None:
                print(current.data)
                current = current.next
            print(current.data)
            return
    
    def reverse(self):
        if not self.head:
            return
        else:
            current = self.head
            self.tail = current
            prev = None
            while current is not None:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            self.head = prev

            

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(11)
    ll.insert(6)
    ll.insert(5)
    ll.insert(4)
    ll.insert(2)

    print(ll.count)
    print(ll)
    print(ll.get_head())
    print(ll.get_tail())

    ll.reverse()
    print(ll)
    print(ll.get_head())
    print(ll.get_tail())
