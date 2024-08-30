class Node:
    def __init__(self, data):
        """
        a node in a singly linked list
        """
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        # create a new singly linked list
        # takes O(1) time
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        # insert a new node at the beginning of the linked list
        # takes O(1) time
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def append(self, data, cycle_node = None):
        # insert a new node at the end of the linked list
        #  takes O(1) time
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            if cycle_node:
                self.tail.next = cycle_node
        self.size += 1

    def get(self, index):
        # get the value of index-th node in the linked list
        # return None if node not found
        # takes O(n) time
        if index < 0 or self.head is None or index >= self.size:
            return None
        if self.head is None:
            return None

        current = self.head
        for i in range(index):
            current = current.next
        return current

    def add_at_index(self, index, data):
        # insert a new node at the index-th node of the linked list
        # takes O(n) time

        if index < 0 or index > self.size:
            return print(f"index {index} is out of boundaries")
        elif index == self.size:
            self.append(data)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def delete_at_index(self, index):
        # delete the index-th node of the linked list
        # takes O(n) time
        if index < 0 or index >= self.size:
            return print(f"index {index} is out of boundaries")
        elif index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            if current.next is None:
                current.next = None
                self.tail = current
            else:
                current.next = current.next.next
        self.size -= 1


# ll = LinkedList()
# ll.prepend(4)
# ll.prepend(9)
# print(ll.size)
# ll.prepend(10)
# print(ll.size)
# ll.append(1)
# print(ll.size)
# print(ll.get(1))
