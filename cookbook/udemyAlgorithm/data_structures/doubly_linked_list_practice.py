class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return self.data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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

    def get_size(self):
        return self.size

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

    def insert_first(self, data):
        node = Node(data)
        self.size += 1

        if not self.head:
            self.head = node
            self.tail = node
            return
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
            return

    def append(self, data):
        self.size += 1
        node = Node(data)

        if not self.head:
            self.head = node
            self.tail = node
            return
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def pop_end(self):
        if self.size == 0:
            return None
        else:
            last = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.size -= 1
            return last.data

    def remove_end(self):
        if self.size == 0:
            return None
        else:
            last = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.size -= 1
            return

    def pop_begin(self):
        if self.size == 0:
            return None
        else:
            first = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.size -= 1
            return first.data
    #need to test
    def remove_begin(self):
        if self.size == 0:
            return None
        else:
            first = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.size -= 1
            return


    def pop_index(self, index):
        if self.size == 0:
            return None
        else:
            #pop the first node (0th index)
            if index == 0:
                return self.pop_begin()
            else:
                node = self.head
                prev_node = self.head
                index_remove = index

                #traverse to find the correct node
                while index_remove > 0:
                    node = node.next
                    index_remove -= 1
                    print (node.data)

                # pop the last node
                if node.next is None:
                    remove_node = node
                    self.tail = node.prev
                    node.prev.next = None
                    self.size -= 1
                    return remove_node.data


                #pop all other nodes
                else:
                    remove_node = node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.size -= 1
                    return remove_node.data








if __name__ == "__main__":
    test_list = DoublyLinkedList()

    #############################test insert at beginning
    test_list.insert_first(11)
    test_list.insert_first(22)
    test_list.insert_first(33)
    test_list.insert_first(44)
    print(test_list)

    #############################test append at end
    test_list.append(66)
    test_list.append(77)
    print(test_list)

    # ##############################test pop
    # print(test_list.pop())
    # print(test_list)
    #
    # test_list.traverse()

    print(test_list.pop_index(4))
    print(test_list)
    print(test_list.pop_index(4))
    print(test_list)
    print(test_list.pop_index(0))
    print(test_list)

    # #############################test remove specific value
    # test_list.remove(11)
    # print(test_list)
    #
    # test_list.remove(44)
    # print(test_list)
    # test_list.remove(33)
    # print(test_list)
    #
    # test_list.remove(36)
    # print(test_list)
    #
    # test_list.remove(22)
    # print(test_list)
    #
    # test_list.remove(11)
    # print(test_list)
    #
    # #############################test append at end
    # test_list.append(111)
    # test_list.append(222)
    # test_list.append(333)
    # print(test_list.get_size())
    # test_list.append(444)
    # print(test_list)