class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CyclicLinkedList:
    def __init__(self):
        self.head = None


def cyclic_list(head):
    if head is None:
        return True

    node = head.next
    i = 0

    while (node is not None) and (node is not head):
        i = i + 1
        node = node.next
    return node == head


clist = CyclicLinkedList()
clist.head = Node(3)
second = Node(2)
third = Node(2)
fourth = Node(0)
five = Node(-4)

clist.head.next = second
second.next = third
third.next = fourth
fourth.next = five
five.next = clist.head

if cyclic_list(clist.head):
    print('Yes')
else:
    print('No')
