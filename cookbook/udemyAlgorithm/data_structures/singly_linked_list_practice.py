class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.data)
            node = node.next
            while node:
                result += " -> " + str(node.data)
                node = node.next
        result += "]"
        return result

    def get_size(self):
        return f"The current size is {self.size}"

    def insert_start(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def remove(self, data):
        if self.head is None:
            return

        current = self.head
        previous = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return
            if current.next is None:
                return
            previous = current
            current = current.next



if __name__ == "__main__":
    test_list = LinkedList()

    #############################test insert at beginning
    test_list.insert_start(11)
    test_list.insert_start(22)
    test_list.insert_start(33)
    test_list.insert_start(44)
    print(test_list)

    #############################test remove specific value
    test_list.remove(11)
    print(test_list)

    test_list.remove(44)
    print(test_list)
    test_list.remove(33)
    print(test_list)

    test_list.remove(36)
    print(test_list)

    test_list.remove(22)
    print(test_list)

    test_list.remove(11)
    print(test_list)

    #############################test append at end
    test_list.append(111)
    test_list.append(222)
    test_list.append(333)
    print(test_list.get_size())
    test_list.append(444)
    print(test_list)