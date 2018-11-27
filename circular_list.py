class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = ListNode(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.tail.next = self.head
        self.size += 1
    def delete(self, data):
        current = self.head
        prev = None
        while(current != self.tail):
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        if current != None and current.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                prev.next = self.head
                self.tail = prev
            self.size -= 1
            return




    def __iter__(self):
        current = self.head
        while current != self.tail:
            data = current.data
            current = current.next
            yield data
        if self.tail is not None:
            yield self.tail.data

circular_list = CircularList()
for country in ('China', 'USA', 'Canada', 'Brazil', 'France'):
    circular_list.append(country)
for value in iter(circular_list):
    print(value, end = ' ')
circular_list.delete('China')
circular_list.delete('Franc')
print('\n')
for value in iter(circular_list):
    print(value, end = ' ')
