import os, sys

sys.path.append(os.path.abspath(".."))

from introduction.LinkedList import LinkedList


def has_cycle(head):
    f, s = head, head
    while f is not None and f.next is not None:
        f = f.next.next
        s = s.next
        if s == f:
            return True
        
    return False

print("TEST 1 #######################")
ll = LinkedList()
ll.append(3)
ll.append(2)
ll.append(0)
cycle_start = ll.get(1)
ll.append(-4, cycle_start)

print(has_cycle(ll.head))


print("TEST 2 #######################")
ll2 = LinkedList()
ll2.append(1)
cycle_start = ll2.get(0)
ll2.append(2, cycle_start)

print(has_cycle(ll2.head))


print("TEST 3 #######################")
ll3 = LinkedList()
ll3.append(1)

print(has_cycle(ll3.head))