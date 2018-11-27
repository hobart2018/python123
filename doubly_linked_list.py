class Node:
    def __init__(self, value = None):
        self.value = value
        self.pre = None
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node2.pre = node1
node3.pre = node2

node1.next = node2
node2.next = node3

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

print_list_backward(node1)
print_list_forward(node3)

node4 = Node(4)
node4.pre = node1
node1.next = node4
node4.next = node2
node2.pre = node4

print_list_backward(node1)

node4.next = node3
node3.pre = node4

print_list_backward(node1)

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

doublist = DoublyLinkedList()
doublist.append(1)
doublist.append(2)
doublist.append(3) # 初始化一个双向链表

print(doublist.count()) # 打印链表长度
print(doublist.get(1).value) # 打印 index=1 处的元素值

doublist.insert(1,4)
doublist.delete(2) # 要补全代码哟

print_list_backward(doublist.head.next) # 打印经上述操作后的双向链表
