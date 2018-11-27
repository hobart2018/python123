class Node:
    def __init__(self, value = None):
        self.value = value
        self.pre = None
        self.next = None

def print_list_backward(node):
    curr = node
    while curr:
        print(curr.value, end='->')
        curr = curr.next
    print('\n')
    return

def print_list_forward(node):
    curr = node
    while curr:
        print(curr.value, end='->')
        curr = curr.pre
    print('\n')
    return

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def append(self, value):
        node = Node(value)
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        node.next = self.tail
        self.tail.pre = node

    def count(self):
        length = 0
        node = self.head
        while node.next != self.tail:
            length += 1
            node = node.next
        return length

    def get(self, index):
        length = self.count()
        if index >= length or index < 0:
            return None
        node = self.head
        for  i in range(index+1):
            node = node.next
        return node

    def delete(self, index):
        length = self.count()
        if index >= length or index < 0:
            return
        node = self.head
        for  i in range(index+1):
            node = node.next
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        return

    def insert(self, index, data):
        length = self.count()
        if index >= length or index < 0:
            return None
        node = self.head
        for  i in range(index+1):
            node = node.next
        pre = node.pre
        node_insert = Node(data)
        pre.next = node_insert
        node_insert.next = node
        node.pre = node_insert
        node_insert.pre = pre

def exchange(doublist, index_i, index_j):
    if index_j < index_i:
        t = index_i
        index_i = index_j
        index_j = t
    length = doublist.count()
    if index_i < 0 or index_j >= length or index_i == index_j:
        return False

    node_i = doublist.get(index_i)
    node_j = doublist.get(index_j)
    value_i = node_i.value
    value_j = node_j.value
    print(value_i,'\n',value_j)
    if index_j - index_i == 1:
        pre = node_i.pre
        next = node_j.next
        pre.next = node_j
        node_j.pre = pre
        node_j.next = node_i
        node_i.pre = node_j
        node_i.next = next
        next.pre = node_i
    else:
        doublist.delete(index_i)
        doublist.insert(index_i, value_j)
        print_list_backward(l.head.next)
        doublist.insert(index_j, value_i)
        doublist.delete(index_j+1)
        print_list_backward(l.head.next)
    return True

def do_reverse(doublist):
    pre_node = doublist.head
    node = pre_node.next
    pre_node.next = None
#    next_node = node.next
#    pre_node.next = None
#    pre_node.pre = node
#    pre_node = node
#    node = next_node
    while(node != None):
        next_node = node.next
        node.next = pre_node
        pre_node.pre = node
        pre_node = node
        node = next_node
    pre_node.pre = None
    t = doublist.head
    doublist.head = doublist.tail
    doublist.tail = t
#    next_node = node.next
#    next_node.pre = None
#    next_node.next = node
    return

l = DoublyLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5) # 初始化一个测试双向链表

print_list_backward(l.head.next) # 打印原始双向链表
#exchange(l,0,4) # 交换 index=0 和 index=4 两处的元素
#print_list_backward(l.head.next) # 打印经交换操作后的双向链表
do_reverse(l)
print_list_backward(l.head.next) # 打印经交换操作后的双向链表
