class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None

print('定义 Node 完成')

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.pointer = node2
node2.pointer = node3

def print_linked_list(node):
    if node.pointer:
        print(node.value, end='->')
    else:
        print(node.value,)
    if (node.pointer):
        print_linked_list(node.pointer)

print_linked_list(node1)

node4 = Node(4)
node4.pointer = node1.pointer
node1.pointer = node4
print_linked_list(node1)

node4.pointer = node2.pointer
print_linked_list(node1)

def print_linked_list_length(node): #######################mark
    n = 0
    ptr = node
    while ptr:
        n = n + 1
        ptr = ptr.pointer
    return n

print(print_linked_list_length(node1))

def is_value_in_linked_list(linkedlist, value):
    flag = False
    ptr = linkedlist
    while ptr:
        if ptr.value == value:
            flag = True
        ptr = ptr.pointer
    return flag

print(is_value_in_linked_list(node1, 3))

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        curr = self.head
        while curr.pointer:
            curr = curr.pointer
        curr.pointer = Node(value)

    def find(self, value):
        curr = self.head
        while curr and curr.value != value:
            curr = curr.pointer
        return curr

    def remove(self, value):    ####################################
        tem_head = tem = Node(-1)
        curr = self.head
        while curr:
            if curr.value != value:
                tem.pointer = curr
                tem = tem.pointer
            curr = curr.pointer
        tem.pointer = None
        self.head = tem_head.pointer
        return
    def count (self):
        curr = self.head
        n = 0
        while curr:
            n += 1
            curr = curr.pointer
        return  n
def print_linked_list(linkedList):
    curr = linkedList.head
    while curr:
        print(curr.value, end='->')
        curr = curr.pointer
    print('\n')

foo = LinkedList()
print(foo.count(),'\n')
foo.append(3)
print(foo.count(),'\n')
print_linked_list(foo)
foo.append(1)
print(foo.count(),'\n')
print_linked_list(foo)
foo.append(2)
foo.append(3)
print_linked_list(foo)
foo.remove(3)
print_linked_list(foo)
print(foo.count(),'\n')
