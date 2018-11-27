class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None


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
#wrong!!!
#def reverse(my_list):
#    reversed_list = LinkedList()
#    tem_last = tem = Node(-1)
#    curr = my_list.head
#    while curr:
#        node = Node(curr.value)
#        node.pointer = tem
#        tem = node
#        curr = curr.pointer
#        tem_last.value = None
#    reversed_list.head = tem
#    return reversed_list

def reverse(my_list):
    reversed_list = LinkedList()
    curr = my_list.head
    while curr:
        if not reversed_list.head:
            reversed_list.head = Node(curr.value)
        else:
            node = Node(curr.value)
            node.pointer = reversed_list.head
            reversed_list.head = node
        curr = curr.pointer
    return reversed_list

def remove_duplicates(my_list):
    new_list = LinkedList()
    curr = my_list.head
    while curr:
        if not new_list.find(curr.value):
            new_list.append(curr.value)
        curr = curr.pointer
    return new_list

def add_linked_list(list_a, list_b):
    curr_a = list_a.head
    curr_b = list_b.head
    multiple = 1
    carry = 0
    sum = 0
    while curr_a and curr_b:
        sum = sum + (curr_a.value + curr_b.value) * multiple
        curr_a = curr_a.pointer
        curr_b = curr_b.pointer
        multiple = multiple * 10
    while curr_a:
        sum = sum + curr_a.value * multiple
        curr_a = curr_a.pointer
        multiple = multiple * 10
    while curr_b:
        sum = sum + curr_b.value * multiple
        curr_b = curr_b.pointer
        multiple = multiple * 10
    return sum

foo = LinkedList()
foo.append(1)
foo.append(2)
foo.append(3)
foo.append(2)
foo.append(5)
foo2 = LinkedList()
foo2.append(1)
foo2.append(2)
foo2.append(3)
print_linked_list(foo)
print_linked_list(reverse(foo))
print(add_linked_list(foo, foo2))
print_linked_list(remove_duplicates(foo))
