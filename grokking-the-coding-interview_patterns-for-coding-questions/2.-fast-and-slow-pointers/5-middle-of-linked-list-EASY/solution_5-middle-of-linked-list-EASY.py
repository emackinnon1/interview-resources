import os, sys

sys.path.append(os.path.abspath(".."))

from introduction.LinkedList import LinkedList

def middleNode(head):
    f, s = head, head
    while f is not None and f.next is not None:
        f = f.next.next
        s = s.next
    return s


print("TEST 1 #######################")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(middleNode(ll.head))