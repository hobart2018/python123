class Stack:
    def __init__(self):
        self.items = []

    # judge whether the stack is empty
    def is_empty(self):
        return self.items == []

    #add item to the Stack
    def push(self, item):
        self.items.append(item)

    #pop an item from the stack
    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items):
            return self.items[len(self.items) - 1]
        return None

    def size(self):
        return len(self.items)

def print_stack(stack):
    print('{:!^11}'.format('top'))
    for i in range(len(stack.items)):
        print('{:^11}'.format(stack.items[len(stack.items) - i - 1]))
    print('{:!^11}'.format('bottom'))

a = Stack()
a.push('a')
a.push('b')
a.push('c')
b = a.pop()
a.push('d')
print(a.peek(),'\n',a.size(),a.is_empty())
print_stack(a)
